from pypc.operations.branches.base_branch import BaseBranchBaseOp


class BeOp(BaseBranchBaseOp):
    ARGC = 3

    def __init__(self, *args):
        super().__init__(*args)

    def _check_branch(self, a1, a2, *args):
        return a1 == a2
