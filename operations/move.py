from operations.base_op import BaseOp


class MoveOp(BaseOp):
    ARGC = 2

    def __init__(self, *args):
        super().__init__(*args)

    def _execute(self, args):
        self.pc.debug(args)
        self.pc.memory.set_value(address=args[1], value=args[0])
