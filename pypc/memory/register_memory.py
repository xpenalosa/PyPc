from pypc.arguments.utils import ArgumentUtils
from pypc.memory.modified_access_memory import ModifiedAccessMemory


class RegisterMemory(ModifiedAccessMemory):
    REG_SIZE = 8

    def __init__(self):
        super().__init__()
        self.registers = [0] * RegisterMemory.REG_SIZE

    def _handle_modified_read(self, address, modification):
        if modification == ArgumentUtils.REGISTER_MODE:
            # Register access
            reg_id = self.data[address]
            return self.get_register(reg_id)
        return super()._handle_modified_read(address, modification)

    def _handle_modified_write(self, value, address, modification):
        if modification == ArgumentUtils.REGISTER_MODE:
            # Register access
            self.set_register(value, address)
            return True
        return super()._handle_modified_write(value, address, modification)

    def get_register(self, reg_id):
        self.LOGGER.debug(f"Getting register: ${reg_id}")
        return self.registers[reg_id]

    def set_register(self, value, reg_id):
        self.LOGGER.debug(f"Setting register: ${reg_id} = {value}")
        self.registers[reg_id] = value
