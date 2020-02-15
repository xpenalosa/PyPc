import logging

from pypc.memory.errors import MemoryReadError, MemoryWriteError
from pypc.operation_parser import UnalignedParser


class BasicMemory:

    LOGGER = logging.getLogger(__name__)
    MEM_SIZE = 512

    def __init__(self):
        self.data = [0] * BasicMemory.MEM_SIZE
        self.LOGGER.debug(f"Starting memory of size {len(self.data)}")
        self.address = 0

    def read_file(self, file, is_parsed=False):
        self.data = [0] * BasicMemory.MEM_SIZE
        self.LOGGER.debug(f"Reading from {file}")
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
                BasicMemory.LOGGER.debug("Parsing file into memory")
                target = UnalignedParser.parse_file(file)
            read_data = [int(x) for x in target.split(",")]
        return read_data
