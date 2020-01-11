from operations.op import Op


class MulOp(Op):

    ID = 2
    ARGC = 3

    def __init__(self, *args):
        super().__init__(*args)

    def _execute(self, args):
        self.pc.memory.set_value(address=args[2], value=args[0] * args[1])
