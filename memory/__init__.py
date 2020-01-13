from enum import Enum, unique

from .basic_memory import BasicMemory
from .modified_access_memory import ModifiedAccessMemory
from .register_memory import RegisterMemory
from .relative_access_memory import RelativeAccessMemory


@unique
class MemoryTypes(Enum):
    BASIC = 0
    MODIFIED_ACCESS = 1
    RELATIVE_ACCESS = 2
    REGISTER = 3

    def instantiate(self):
        if self.value == MemoryTypes.BASIC.value:
            return BasicMemory()
        elif self.value == MemoryTypes.MODIFIED_ACCESS.value:
            return ModifiedAccessMemory()
        elif self.value == MemoryTypes.RELATIVE_ACCESS.value:
            return RelativeAccessMemory()
        elif self.value == MemoryTypes.REGISTER.value:
            return RegisterMemory()
