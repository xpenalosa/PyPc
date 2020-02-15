from pypc.operations import BaseOp


class InpOp(BaseOp):
    ARGC = 1

    def __init__(self, *args):
        super().__init__(*args)

    def _execute(self, args):
        self.pc.memory.set_value(
            address=args[0],
            value=self._get_input_value(),
            modification=self.mods[self.ARGC - 1])

    def _get_input_value(self):
        return int(input())
