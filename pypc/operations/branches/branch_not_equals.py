from pypc.operations.branches import BeOp


class BneOp(BeOp):

    def __init__(self, *args):
        super().__init__(*args)

    def _check_branch(self, a1, a2, *args):
        return not super()._check_branch(a1, a2, *args)
