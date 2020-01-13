from operations.branches.branch_equals import BeOp


class BzOp(BeOp):
    ARGC = 2

    def __init__(self, *args):
        super().__init__(*args)

    def _check_branch(self, a1, a2):
        return super()._check_branch(a1, 0)
