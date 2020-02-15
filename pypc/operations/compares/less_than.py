from pypc.operations.compares.base_compare import BaseCompareBaseOp


class LtOp(BaseCompareBaseOp):

    def __init__(self, *args):
        super().__init__(*args)

    def _compare(self, a1, a2):
        return int(a1 < a2)
