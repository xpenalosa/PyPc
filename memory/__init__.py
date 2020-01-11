from memory.basic_memory import BasicMemory
from memory.modified_access_memory import ModifiedAccessMemory
from memory.relative_access_memory import RelativeAccessMemory
from memory.register_memory import RegisterMemory


def from_id(mem_id):
    if mem_id == 0: return BasicMemory()
    elif mem_id == 1: return ModifiedAccessMemory()
    elif mem_id == 2: return RelativeAccessMemory()
    elif mem_id == 3: return RegisterMemory()
