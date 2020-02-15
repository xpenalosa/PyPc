from pypc.operations import BaseOp


class MovOp(BaseOp):
    ARGC = 2

    def __init__(self, *args):
        super().__init__(*args)

    def _execute(self, args):
        self.LOGGER.debug(args)
        self.pc.memory.set_value(
            address=args[self.ARGC-1],
            value=args[0],
            modification=self.mods[self.ARGC-1])
