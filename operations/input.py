from operations.op import Op


class InpOp(Op):

    ID = 3
    ARGC = 1

    def __init__(self, *args):
        super().__init__(*args)

    def _execute(self, args):
        self.pc.memory.set_value(address=args[0], value=int(input()))
