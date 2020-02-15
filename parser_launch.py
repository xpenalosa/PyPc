import sys
import logging

from pypc.operation_parser import UnalignedParser

log_format = "[%(levelname)s] %(name)s - %(message)s"
log_level = logging.INFO
logging.basicConfig(format=log_format,
                    stream=sys.stdout,
                    level=log_level)

parser = UnalignedParser()
parsed_code = parser.parse_file("./pypc/operation_parser/parser_input_2.txt")
print(parsed_code)
