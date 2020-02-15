import sys
import logging
from typing import List
from unittest import TestCase

from pypc.memory import MemoryTypes
from pypc.operation_parser import UnalignedParser
from pypc.pc import Pc


class OperationTestBase(TestCase):

    def setUp(self) -> None:
        log_format = "[%(levelname)s] %(name)s - %(message)s"
        log_level = logging.INFO
        logging.basicConfig(format=log_format,
                            stream=sys.stdout,
                            level=log_level)

    @staticmethod
    def run_pc(memory_type: MemoryTypes, initial_data: List):
        memory = memory_type.instantiate()
        memory.data = initial_data.copy()
        memory.address = 0
        pc = Pc()
        pc.set_memory(memory)
        pc.run()
        return memory

    @staticmethod
    def parse_input(data: str) -> List:
        return [int(x) for x in UnalignedParser().parse_string(data).split(",")]
