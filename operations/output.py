from operations.op import Op


class OutOp(Op):

    ID = 4
    ARGC = 1

    def __init__(self, *args):
        super().__init__(*args)

    def _execute(self, args):
        print(">", str(args[0]))
