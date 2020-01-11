from memory.modified_access_memory import ModifiedAccessMemory


class RelativeAccessMemory(ModifiedAccessMemory):

    def __init__(self):
        super().__init__()

    def _handle_modified_read(self, address, modification):
        if modification == 2:
            # Relative access
            new_address = address + self.data[address]
            return self.data[new_address]
        return super()._handle_modified_read(address, modification)

    def _handle_modified_write(self, value, address, modification):
        if modification == 2:
            # Relative access
            new_address = address + self.data[address]
            self.data[new_address] = value
            return True
        return super()._handle_modified_write(value, address, modification)
