from pypc.arguments.utils import ArgumentUtils
from pypc.operation_parser.base_parser import BaseParser
from pypc.operations import Operations


class UnalignedParser(BaseParser):

    def __init__(self):
        super().__init__()
        self.parsed_instructions = []

    def add_instruction(self, instruction):
        self.LOGGER.debug(f"Parsing instruction [{instruction}]")
        op_name = instruction.split(" ")[0].strip()
        arguments = [arg.rstrip(",") for arg in instruction.split(" ")[1:]]

        op_code = Operations[op_name].value
        padded_op_code = str(op_code).zfill(2)

        new_instruction = ""
        for arg in arguments:
            mode = ArgumentUtils.get_argument_mode(arg)
            # Add argument mode to op code
            padded_op_code = str(mode) + padded_op_code
            stripped_arg = ArgumentUtils.strip_argument_mode(arg, mode)
            new_instruction += f",{stripped_arg}"
        # Strip leading 0s in op code and assemble the whole instruction
        new_instruction = str(int(padded_op_code)) + new_instruction
        self.parsed_instructions.append(new_instruction)

    def update_tags(self, tagged_code):
        self.LOGGER.debug(f"Updating tags: {self.tags.keys()}")
        fields = tagged_code.split(",")
        for i in range(1, len(fields)):
            field = fields[i]
            if ArgumentUtils.is_tag(field):
                tag_address = self.tags.get(field)
                if tag_address is None:
                    raise LookupError(f"Unexpected tag name '{field}'")
                fields[i] = str(tag_address)
        return ','.join(fields)

    def _increase_address(self, instruction, *args):
        self.address += len(instruction.split(" "))

    def _parse_instructions(self, instructions):
        for inst in instructions:
            if ArgumentUtils.is_tag(inst):
                self.LOGGER.debug(f"Adding tag [{inst}]")
                self.add_tag(ArgumentUtils.strip_argument_mode(
                    inst, ArgumentUtils.LITERAL_MODE))
                continue
            self.add_instruction(inst)
            self._increase_address(inst)

        # Join all operations into a single line
        tagged_code = ','.join(self.parsed_instructions)
        # Replace tag references with addresses
        self.parsed_code = self.update_tags(tagged_code)
        self.parsed_code += f",{Operations.END.value}"
