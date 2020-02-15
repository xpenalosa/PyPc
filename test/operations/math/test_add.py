from pypc.memory import MemoryTypes
from pypc.operations import Operations
from test.operations.operation_test import OperationTestBase


class AddTest(OperationTestBase):

    def test_add_basic(self):
        memory_type = MemoryTypes.BASIC
        initial_data = "\n".join([
            "ADD 1, 2, 0"])
        expected_data = list(
            [3, 1, 2, 0,
             Operations.END.value])

        result_mem = self.run_pc(memory_type, self.parse_input(initial_data))
        self.assertEqual(expected_data, result_mem.data)
        self.assertEqual(result_mem.address, 4)

    def test_add_mod_access_ll(self):
        memory_type = MemoryTypes.MODIFIED_ACCESS
        initial_data = "\n".join([
            "ADD 1L, 2L, 0"])
        expected_data = list(
            [3, 1, 2, 0,
             Operations.END.value])

        result_mem = self.run_pc(memory_type, self.parse_input(initial_data))
        self.assertEqual(expected_data, result_mem.data)
        self.assertEqual(result_mem.address, 4)

    def test_add_mod_access_lr(self):
        memory_type = MemoryTypes.MODIFIED_ACCESS
        initial_data = "\n".join([
            "ADD 1L, 2, 0"])
        expected_data = list(
            [3, 1, 2, 0,
             Operations.END.value])

        result_mem = self.run_pc(memory_type, self.parse_input(initial_data))
        self.assertEqual(expected_data, result_mem.data)
        self.assertEqual(result_mem.address, 4)

    def test_add_mod_access_rr(self):
        memory_type = MemoryTypes.MODIFIED_ACCESS
        initial_data = "\n".join([
            "ADD 1, 2, 0"])
        expected_data = list(
            [3, 1, 2, 0,
             Operations.END.value])

        result_mem = self.run_pc(memory_type, self.parse_input(initial_data))
        self.assertEqual(expected_data, result_mem.data)
        self.assertEqual(result_mem.address, 4)
