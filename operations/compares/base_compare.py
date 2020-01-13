from operations.base_op import BaseOp


class BaseCompareBaseOp(BaseOp):
    ARGC = 3

    def __init__(self, *args):
        super().__init__(*args)

    def _execute(self, args):
        self.pc.memory.set_value(
            address=args[2], value=self._compare(args[0], args[1]))

    def _compare(self, a1, a2):
        pass
