from operations.op import Op


class BaseBranchOp(Op):

    ID = 10
    ARGC = 2
    MV_PTR = False

    def __init__(self, *args):
        super().__init__(*args)

    def _execute(self, args):
        self.pc.debug(f"\tPointer before: {self.pc.memory.get_address()}")
        if self._check_branch(*(args[:2])):
            self.pc.memory.set_address(args[-1])
        else:
            self.pc.memory.set_address(
                self.pc.memory.get_address() + self.ARGC + 1)
        self.pc.debug(f"\tPointer after: {self.pc.memory.get_address()}")

    def _check_branch(self, a1, a2):
        return False
