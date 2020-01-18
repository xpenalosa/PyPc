class BaseParser:

    @staticmethod
    def get_argument_mode(argument):
        # TODO Refactor
        if argument.startswith("."):
            # Tag -> Literal
            return 1
        elif argument.startswith("$"):
            # Register
            return 2
        if argument.endswith("L"):
            # Literal value
            return 1
        elif argument.endswith("R"):
            # Relative access
            return 3
        else:
            # Normal parameter
            return 0

    @staticmethod
    def strip_argument_mode(argument, mode):
        # TODO Refactor
        if mode == 0:
            return argument
        elif mode == 1 and argument.startswith("."):
            # Tag
            return argument
        elif mode == 1 and argument.endswith("L"):
            # Literal
            return argument[:-1]
        elif mode == 2 and argument.startswith("$"):
            # Register
            return argument[1:]
        elif mode == 3 and argument.endswith("R"):
            # Relative
            return argument[:-1]

    @staticmethod
    def is_tag(argument):
        return argument.startswith(".")

    def __init__(self):
        self.tags = dict()
        self.address = 0
        self.parsed_code = ""

    def add_instruction(self, *args):
        pass

    def add_tag(self, tag):
        self.tags[tag] = self.address

    def parse_file(self, file):
        with open(file, 'r') as f:
            instructions = [line.strip() for line in f.readlines() if line]
        self._parse_instructions(instructions)
        return self.parsed_code

    def update_tags(self, *args):
        pass

    def _increase_address(self, *args):
        pass

    def _parse_instructions(self, instructions):
        self.parsed_code = ",".join(instructions)
