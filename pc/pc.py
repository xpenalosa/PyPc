from operations import Operations, errors


class Pc:

    def __init__(self, debug_mode=False):
        self.memory = None
        self.debug_mode = debug_mode

    def read_data(self, data_file, memory_type):
        self.memory = memory_type.instantiate()
        self.memory.read_file(data_file)

    def run(self):
        self.run_until_op(Operations.END)

    def run_until_op(self, op_id):
        try:
            self.debug(self.memory)
            self.__run_until_op(op_id)
        except errors.OpEndError:
            self.debug(f"Found {Operations.END}")
            self.debug(self.memory)

    def __run_until_op(self, op_id):
        current_op_id = self.memory.get_value(modification=1)
        while current_op_id != op_id:
            current_op = Operations.from_id(current_op_id)
            self.debug(current_op)
            self.__execute_op(current_op)
            current_op_id = self.memory.get_value(modification=1)

    def __execute_op(self, op):
        op.set_pc(self)
        op.execute()
        if op.MV_PTR:
            address = self.memory.get_address()
            self.memory.set_address(address + op.ARGC + 1)

    def debug(self, msg):
        if self.debug_mode:
            print(f"[DEBUG] {msg}")
