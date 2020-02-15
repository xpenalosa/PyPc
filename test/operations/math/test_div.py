from pypc.memory import MemoryTypes
from pypc.operations import Operations
from test.operations.operation_test import OperationTestBase


class DivTest(OperationTestBase):

    def test_div_basic(self):
        memory_type = MemoryTypes.BASIC
        initial_data = "\n".join([
            "DIV 8, 2, 0"])
        expected_data = list(
            [4, 8, 2, 0,
             Operations.END.value])

        result_mem = self.run_pc(memory_type, self.parse_input(initial_data))
        self.assertEqual(expected_data, result_mem.data)
        self.assertEqual(result_mem.address, 4)

    def test_div_basic_decimal(self):
        memory_type = MemoryTypes.BASIC
        initial_data = "\n".join([
            "DIV 8, 3, 0"])
        expected_data = list(
            [2, 8, 3, 0,
             Operations.END.value])

        result_mem = self.run_pc(memory_type, self.parse_input(initial_data))
        self.assertEqual(expected_data, result_mem.data)
        self.assertEqual(result_mem.address, 4)

    def test_div_mod_access_ll(self):
        memory_type = MemoryTypes.MODIFIED_ACCESS
        initial_data = "\n".join([
            "DIV 8L, 2L, 0"])
        expected_data = list(
            [4, 8, 2, 0,
             Operations.END.value])

        result_mem = self.run_pc(memory_type, self.parse_input(initial_data))
        self.assertEqual(expected_data, result_mem.data)
        self.assertEqual(result_mem.address, 4)

    def test_div_mod_access_lr(self):
        memory_type = MemoryTypes.MODIFIED_ACCESS
        initial_data = "\n".join([
            "DIV 8L, 1, 0"])
        expected_data = list(
            [1, 8, 1, 0,
             Operations.END.value])

        result_mem = self.run_pc(memory_type, self.parse_input(initial_data))
        self.assertEqual(expected_data, result_mem.data)
        self.assertEqual(result_mem.address, 4)

    def test_div_mod_access_rr(self):
        memory_type = MemoryTypes.MODIFIED_ACCESS
        initial_data = "\n".join([
            "DIV 3, 2, 0"])
        expected_data = list(
            [0, 3, 2, 0,
             Operations.END.value])

        result_mem = self.run_pc(memory_type, self.parse_input(initial_data))
        self.assertEqual(expected_data, result_mem.data)
        self.assertEqual(result_mem.address, 4)
