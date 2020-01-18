from operation_parser import UnalignedParser

parser = UnalignedParser()
parsed_code = parser.parse_file("./operation_parser/parser_input.txt")
print(parsed_code)
