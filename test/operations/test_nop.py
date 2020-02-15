from pypc.memory import MemoryTypes
from pypc.operations import Operations
from test.operations.operation_test import OperationTestBase


class NopTest(OperationTestBase):

    def test_nop(self):
        memory_type = MemoryTypes.BASIC
        initial_data = list(
            [Operations.NOP.value,
             Operations.END.value])
        result_mem = self.run_pc(memory_type, initial_data)
        self.assertEqual(result_mem.data, initial_data)
        self.assertEqual(result_mem.address, 1)

    def test_multi_nop(self):
        memory_type = MemoryTypes.BASIC
        initial_data = list(
            [Operations.NOP.value,
             Operations.NOP.value,
             Operations.NOP.value,
             Operations.NOP.value,
             Operations.END.value])
        result_mem = self.run_pc(memory_type, initial_data)
        self.assertEqual(initial_data, result_mem.data)
        self.assertEqual(4, result_mem.address)
