import operations
import memory


class Pc:

    def __init__(self, debug_mode=False):
        self.memory = None
        self.debug_mode = debug_mode

    def read_data(self, data_file, memory_type=0):
        self.memory = memory.from_id(memory_type)
        self.memory.read_file(data_file)

    def run(self):
        self.run_until_op(99)

    def run_until_op(self, op_id):
        try:
            self.debug(self.memory)
            self.__run_until_op(op_id)
        except operations.OpEndError:
            self.debug("Found OP code 99")
            self.debug(self.memory)

    def __run_until_op(self, op_id):
        current_op = operations.from_id(self.memory.get_value(modification=1))
        while current_op.ID != op_id:
            self.debug(current_op)
            current_op.set_pc(self)
            self.__execute_op(current_op)
            current_op = operations.from_id(
                self.memory.get_value(modification=1))

    def __execute_op(self, op):
        op.execute()
        if op.MV_PTR:
            address = self.memory.get_address()
            self.memory.set_address(address + op.ARGC + 1)

    def debug(self, msg):
        if self.debug_mode:
            print(f"[DEBUG] {msg}")
