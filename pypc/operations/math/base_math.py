from pypc.operations import BaseOp


class BaseMathOp(BaseOp):
    ARGC = 3

    def __init__(self, *args):
        super().__init__(*args)

    def _execute(self, args):
        self.LOGGER.debug(args)
        result = self._calculate(args[0], args[1])
        self.pc.memory.set_value(
            address=args[self.ARGC-1],
            value=result,
            modification=self.mods[self.ARGC-1])

    def _calculate(self, a1, a2):
        pass
