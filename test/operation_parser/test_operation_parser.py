import logging
import sys
import os
from unittest import TestCase

from pypc.operation_parser import UnalignedParser
from pypc.operations import Operations


class TestOperationParser(TestCase):

    def setUp(self) -> None:
        logging.basicConfig(
            format="[%(levelname)s] %(name)s - %(message)s",
            stream=sys.stdout,
            level=logging.WARN)

    @staticmethod
    def parse(text):
        parser = UnalignedParser()
        return parser.parse_string(text)

    def test_parse_file(self):
        # TODO use temporary file
        test_file_name = "./test_parse_file.txt"
        with open(test_file_name, 'w') as file:
            file.write("""ADD 0, 0, 0\nMUL 0, 0, 0""")
        parser = UnalignedParser()
        parsed_text = parser.parse_file(test_file_name)
        os.remove(test_file_name)
        self.assertEqual("1,0,0,0,2,0,0,0,99", parsed_text)

    def test_parse_string(self):
        raw_data = "ADD 0, 0, 0\nMUL 0, 0, 0"
        parser = UnalignedParser()
        parsed_text = parser.parse_string(raw_data)
        self.assertEqual("1,0,0,0,2,0,0,0,99", parsed_text)

    def test_parse_all_instructions(self):
        for op in Operations:
            raw_text = f"{op.name} 0, 0, 0"
            parsed_text = self.parse(raw_text)
            self.assertEqual(f"{op.value},0,0,0,99", parsed_text)

    def test_parse_tag(self):
        raw_data = "ADD 0, 0, 0\n.TAG\nMUL 0, 0, .TAG"
        parser = UnalignedParser()
        parsed_text = parser.parse_string(raw_data)
        self.assertEqual("1,0,0,0,10002,0,0,4,99", parsed_text)

    def test_parse_literal(self):
        raw_data = "ADD 0L, 0, 0"
        parser = UnalignedParser()
        parsed_text = parser.parse_string(raw_data)
        self.assertEqual("101,0,0,0,99", parsed_text)

    def test_parse_relative(self):
        raw_data = "ADD 0R, 0, 0"
        parser = UnalignedParser()
        parsed_text = parser.parse_string(raw_data)
        self.assertEqual("201,0,0,0,99", parsed_text)

    def test_parse_register(self):
        raw_data = "ADD $0, 0, 0"
        parser = UnalignedParser()
        parsed_text = parser.parse_string(raw_data)
        self.assertEqual("301,0,0,0,99", parsed_text)
