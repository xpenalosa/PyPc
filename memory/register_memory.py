from memory.modified_access_memory import ModifiedAccessMemory


class RegisterMemory(ModifiedAccessMemory):

    REG_SIZE = 8

    def __init__(self):
        super().__init__()
        self.registers = [0] * RegisterMemory.REG_SIZE

    def _handle_modified_read(self, address, modification):
        if modification == 3:
            # Register access
            return self.get_register(address)
        return super()._handle_modified_read(address, modification)

    def _handle_modified_write(self, value, address, modification):
        if modification == 3:
            # Register access
            self.set_register(value, address)
            return True
        return super()._handle_modified_write(value, address, modification)

    def get_register(self, address):
        return self.registers[address]

    def set_register(self, value, address):
        self.registers[address] = value
