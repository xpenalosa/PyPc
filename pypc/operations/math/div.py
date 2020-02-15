from pypc.operations.math.base_math import BaseMathOp


class DivOp(BaseMathOp):

    def __init__(self, *args):
        super().__init__(*args)

    def _calculate(self, a1, a2):
        return a1 // a2
