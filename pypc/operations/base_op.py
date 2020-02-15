import logging

from pypc.arguments.utils import ArgumentUtils


class BaseOp:
    ID = 0
    ARGC = 0
    MV_PTR = True
    LOGGER = logging.getLogger(__name__)

    def __init__(self, *mods):
        self.pc = None
        self.mods = mods

    def __str__(self):
        return f"{self.__class__.__name__[:-2]}, Mods={self.mods}"

    def set_pc(self, pc):
        self.pc = pc
        self.LOGGER.debug("-" * 10)
        self.LOGGER.debug(self)

    def parse_args(self):
        args = list()
        if self.ARGC > 0:
            arg_address = self.pc.memory.get_address() + 1
            value = self.pc.memory.get_value(
                address=arg_address, modification=self.mods[0])
            args.append(value)
        if self.ARGC > 1:
            arg_address = self.pc.memory.get_address() + 2
            value = self.pc.memory.get_value(
                address=arg_address, modification=self.mods[1])
            args.append(value)
        if self.ARGC > 2:
            arg_address = self.pc.memory.get_address() + 3
            value = self.pc.memory.get_value(
                address=arg_address, modification=ArgumentUtils.LITERAL_MODE)
            args.append(value)
        self.LOGGER.debug(f"\tArgs: {args}")
        return args

    def execute(self):
        args = self.parse_args()
        self._execute(args)

    def _execute(self, args):
        pass
