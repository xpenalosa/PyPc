from unittest import TestCase
from typing import List

from pc import Pc
from memory import MemoryTypes
from operation_parser import UnalignedParser


class OperationTestBase(TestCase):

    @staticmethod
    def run_pc(memory_type: MemoryTypes, initial_data: List):
        memory = memory_type.instantiate()
        memory.data = initial_data.copy()
        memory.address = 0
        pc = Pc(debug_mode=False)
        pc.set_memory(memory)
        pc.run()
        return memory

    @staticmethod
    def parse_input(data: str) -> List:
        return [int(x) for x in UnalignedParser().parse_string(data).split(",")]
