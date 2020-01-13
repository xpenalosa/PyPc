from operations.base_op import BaseOp


class BaseMathBaseOp(BaseOp):
    ARGC = 3

    def __init__(self, *args):
        super().__init__(*args)

    def _execute(self, args):
        self.pc.debug(args)
        result = self._calculate(args[0], args[1])
        self.pc.memory.set_value(address=args[2], value=result)

    def _calculate(self, a1, a2):
        pass
