import logging
import sys
from unittest import TestCase

from pypc.memory import MemoryTypes
from pypc.operations import Operations
from pypc.pc import Pc


class TestPc(TestCase):

    def setUp(self) -> None:
        logging.basicConfig(
            format="[%(levelname)s] %(name)s - %(message)s",
            stream=sys.stdout,
            level=logging.WARN)
        self.raw_data = [
            Operations.ADD.value, 0, 0, 7,
            Operations.OUT.value, 7,
            Operations.END.value,
            0]
        memory = MemoryTypes.MODIFIED_ACCESS.instantiate()
        memory.data = self.raw_data.copy()
        memory.address = 0
        self.pc = Pc()
        self.pc.set_memory(memory)

    def reset_pc(self):
        self.pc.memory.data = self.raw_data.copy()
        self.pc.memory.set_address(0)

    def test_run(self):
        self.reset_pc()
        self.pc.run()
        self.assertEqual(self.pc.memory.get_address(), 6, "Address")
        self.assertEqual([1, 0, 0, 7, 4, 7, 99, 2], self.pc.memory.data,
                         "Memory")

    def test_run_until_op(self):
        self.reset_pc()
        self.pc.run_until_op(Operations.OUT.value)
        self.assertEqual(self.pc.memory.get_address(), 4, "Address 1")
        self.assertEqual([1, 0, 0, 7, 4, 7, 99, 2], self.pc.memory.data,
                         "Memory 1")

        self.reset_pc()
        self.pc.run_until_op(Operations.ADD.value)
        self.assertEqual(self.pc.memory.get_address(), 0, "Address 2")
        self.assertEqual([1, 0, 0, 7, 4, 7, 99, 0], self.pc.memory.data,
                         "Memory 2")

        # No mul operation, should run to END
        self.reset_pc()
        self.pc.run_until_op(Operations.MUL.value)
        self.assertEqual(self.pc.memory.get_address(), 6, "Address 3")
        self.assertEqual([1, 0, 0, 7, 4, 7, 99, 2], self.pc.memory.data,
                         "Memory 3")
