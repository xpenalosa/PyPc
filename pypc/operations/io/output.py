from pypc.operations import BaseOp


class OutOp(BaseOp):
    ARGC = 1

    def __init__(self, *args):
        super().__init__(*args)

    def _execute(self, args):
        self._output_values(args[0])

    def _output_values(self, *args):
        self.LOGGER.info(args[0])
