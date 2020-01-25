from memory.errors import MemoryReadError, MemoryWriteError
from operation_parser import UnalignedParser


class BasicMemory:
    MEM_SIZE = 512

    def __init__(self):
        self.data = [0] * BasicMemory.MEM_SIZE
        self.address = 0

    def read_file(self, file, is_parsed=False):
        self.data = [0] * BasicMemory.MEM_SIZE
        read_data = BasicMemory._parse_data(file, is_parsed)
        if len(read_data) > len(self.data):
            raise MemoryWriteError(
                f"Data too big for memory ({BasicMemory.MEM_SIZE})")
        self.data[:len(read_data)] = read_data[:]
        self.address = 0

    def get_value(self, address=None, *args, **kwargs):
        if address is None:
            address = self.address
        try:
            return self.data[address]
        except IndexError as e:
            raise MemoryReadError(f"Accessing memory out of bounds [{address}]")

    def set_value(self, value=0, address=None, *args, **kwargs):
        if address is None:
            address = self.address
        try:
            self.data[address] = value
        except IndexError as e:
            raise MemoryReadError(f"Accessing memory out of bounds [{address}]")

    def get_address(self):
        return self.address

    def set_address(self, address):
        self.address = address

    def __str__(self):
        return f"[M {self.address}] {self.data}"

    @staticmethod
    def _parse_data(file, is_parsed):
        with open(file, 'r') as f:
            target = f.readline()
            if not is_parsed:
                target = UnalignedParser.parse_file(file)
            read_data = [int(x) for x in target.split(",")]
        return read_data
