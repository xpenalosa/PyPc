import logging


class BaseParser:

    LOGGER = logging.getLogger(__name__)

    def __init__(self):
        self.tags = dict()
        self.address = 0
        self.parsed_code = ""

    def add_instruction(self, *args):
        pass

    def add_tag(self, tag):
        self.tags[tag] = self.address

    def parse_file(self, file):
        self.LOGGER.debug(f"Reading from {file}")
        with open(file, 'r') as f:
            contents = f.read()
        return self.parse_string(contents)

    def parse_string(self, string):
        lines = string.split("\n")
        instructions = [line.strip() for line in lines if line]
        self._parse_instructions(instructions)
        return self.parsed_code

    def update_tags(self, *args):
        pass

    def _increase_address(self, *args):
        pass

    def _parse_instructions(self, instructions):
        self.parsed_code = ",".join(instructions)
