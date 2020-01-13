from operations.branches.base_branch import BaseBranchBaseOp


class BrOp(BaseBranchBaseOp):

    def __init__(self, *args):
        super().__init__(*args)

    def _check_branch(self, a1, a2):
        return True
