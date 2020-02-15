import re


class ArgumentUtils:

    LITERAL_RE = re.compile(r"(-?\d+)L")
    RELATIVE_RE = re.compile(r"(-?\d+)R")
    REGISTER_RE = re.compile(r"\$(\d)")
    TAG_RE = re.compile(r"\.(.+)")

    LITERAL_MODE = 1
    RELATIVE_MODE = 2
    REGISTER_MODE = 3

    @staticmethod
    def get_argument_mode(argument):
        if ArgumentUtils.TAG_RE.match(argument) or ArgumentUtils.LITERAL_RE.match(argument):
            return ArgumentUtils.LITERAL_MODE
        elif ArgumentUtils.REGISTER_RE.match(argument):
            return ArgumentUtils.REGISTER_MODE
        elif ArgumentUtils.RELATIVE_RE.match(argument):
            return ArgumentUtils.RELATIVE_MODE
        return 0

    @staticmethod
    def strip_argument_mode(argument, mode):
        if mode == ArgumentUtils.REGISTER_MODE:
            return ArgumentUtils.REGISTER_RE.search(argument).group(1)
        elif mode == ArgumentUtils.LITERAL_MODE:
            tag_matches = ArgumentUtils.TAG_RE.search(argument)
            if tag_matches:
                # Do not remove tag identifiers
                return argument
            else:
                literal_matches = ArgumentUtils.LITERAL_RE.search(argument)
                return literal_matches.group(1)
        elif mode == ArgumentUtils.RELATIVE_MODE:
            return ArgumentUtils.RELATIVE_RE.search(argument).group(1)
        return argument

    @staticmethod
    def is_tag(argument):
        return ArgumentUtils.TAG_RE.match(argument) or False
