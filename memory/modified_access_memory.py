from memory.basic_memory import BasicMemory


class ModifiedAccessMemory(BasicMemory):

    def __init__(self):
        super().__init__()

    def get_value(self, address=None, modification=0, *args, **kwargs):
        if address is None:
            address = self.address
        value = self._handle_modified_read(address, modification)
        if value is None:
            # Unsupported modification. Reference access
            new_address = self.data[address]
            value = super().get_value(address=new_address)
        return value

    def _handle_modified_read(self, address, modification):
        if modification == 1:
            # Literal access
            return self.data[address]

    def set_value(self, value=0, address=None, modification=0, *args, **kwargs):
        if address is None:
            address = self.address
        ret_value = self._handle_modified_write(value, address, modification)
        if ret_value is None:
            # Unsupported modification. Default operation
            self.data[address] = value

    def _handle_modified_write(self, value, address, modification):
        # Writes are literal access by default
        pass
