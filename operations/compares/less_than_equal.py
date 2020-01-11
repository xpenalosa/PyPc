from operations.compares.base_compare import BaseCompareOp


class LteOp(BaseCompareOp):

    ID = 22

    def __init__(self, *args):
        super().__init__(*args)

    def _compare(self, a1, a2):
        return int(a1 <= a2)
