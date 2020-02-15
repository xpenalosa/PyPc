from pypc.operations import BaseOp


class BaseCompareBaseOp(BaseOp):
    ARGC = 3

    def __init__(self, *args):
        super().__init__(*args)

    def _execute(self, args):
        self.pc.memory.set_value(
            address=args[self.ARGC-1],
            value=self._compare(args[0], args[1]),
            modification=self.mods[self.ARGC-1])

    def _compare(self, a1, a2):
        pass
