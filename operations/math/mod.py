from operations.math.base_math import BaseMathBaseOp


class ModOp(BaseMathBaseOp):

    def __init__(self, *args):
        super().__init__(*args)

    def _calculate(self, a1, a2):
        return a1 % a2
