from operations.base_op import BaseOp


class OutOp(BaseOp):
    ARGC = 1

    def __init__(self, *args):
        super().__init__(*args)

    def _execute(self, args):
        print(">", str(args[0]))
