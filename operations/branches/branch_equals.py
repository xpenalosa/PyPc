from operations.branches.base_branch import BaseBranchOp


class BeOp(BaseBranchOp):

    ID = 13
    ARGC = 3

    def __init__(self, *args):
        super().__init__(*args)

    def _check_branch(self, a1, a2):
        return a1 == a2
