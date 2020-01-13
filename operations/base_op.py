class BaseOp:
    ID = 0
    ARGC = 0
    MV_PTR = True

    def __init__(self, mod_a1=0, mod_a2=0):
        self.pc = None
        self.mod_a1 = mod_a1
        self.mod_a2 = mod_a2

    def __str__(self):
        return f"{self.__class__.__name__[:-2]}, {self.mod_a1}, {self.mod_a2}"

    def set_pc(self, pc):
        self.pc = pc
        self.pc.debug("-" * 10)
        self.pc.debug(self)

    def parse_args(self):
        args = list()
        if self.ARGC > 0:
            arg_address = self.pc.memory.get_address() + 1
            value = self.pc.memory.get_value(
                address=arg_address, modification=self.mod_a1)
            args.append(value)
        if self.ARGC > 1:
            arg_address = self.pc.memory.get_address() + 2
            value = self.pc.memory.get_value(
                address=arg_address, modification=self.mod_a2)
            args.append(value)
        if self.ARGC > 2:
            arg_address = self.pc.memory.get_address() + 3
            value = self.pc.memory.get_value(
                address=arg_address, modification=1)
            args.append(value)
        self.pc.debug("\tArgs: " + str(args))
        return args

    def execute(self):
        args = self.parse_args()
        self._execute(args)

    def _execute(self, args):
        pass
