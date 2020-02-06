from memory import MemoryTypes
from operations import Operations
from test.operations.operation_test import OperationTestBase


class LessThanTest(OperationTestBase):

    def test_lt_basic_true(self):
        memory_type = MemoryTypes.BASIC
        initial_data = "\n".join([
            "LT 1, 2, 0"])
        expected_data = list(
            [1, 1, 2, 0,
             Operations.END.value])

        result_mem = self.run_pc(memory_type, self.parse_input(initial_data))
        self.assertEqual(expected_data, result_mem.data)
        self.assertEqual(result_mem.address, 4)

    def test_lt_basic_false(self):
        memory_type = MemoryTypes.BASIC
        initial_data = "\n".join([
            "LT 2, 2, 0"])
        expected_data = list(
            [0, 2, 2, 0,
             Operations.END.value])

        result_mem = self.run_pc(memory_type, self.parse_input(initial_data))
        self.assertEqual(expected_data, result_mem.data)
        self.assertEqual(result_mem.address, 4)

    def test_lt_mod_access_ll(self):
        memory_type = MemoryTypes.MODIFIED_ACCESS
        initial_data = "\n".join([
            "LT 2L, 3L, 0"])
        expected_data = list(
            [1, 2, 3, 0,
             Operations.END.value])

        result_mem = self.run_pc(memory_type, self.parse_input(initial_data))
        self.assertEqual(expected_data, result_mem.data)
        self.assertEqual(result_mem.address, 4)

    def test_lt_mod_access_lr(self):
        memory_type = MemoryTypes.MODIFIED_ACCESS
        initial_data = "\n".join([
            "LT 2L, 1, 0"])
        expected_data = list(
            [0, 2, 1, 0,
             Operations.END.value])

        result_mem = self.run_pc(memory_type, self.parse_input(initial_data))
        self.assertEqual(expected_data, result_mem.data)
        self.assertEqual(result_mem.address, 4)

    def test_lt_mod_access_rr(self):
        memory_type = MemoryTypes.MODIFIED_ACCESS
        initial_data = "\n".join([
            "LT 1, 2, 0"])
        expected_data = list(
            [1, 1, 2, 0,
             Operations.END.value])

        result_mem = self.run_pc(memory_type, self.parse_input(initial_data))
        self.assertEqual(expected_data, result_mem.data)
        self.assertEqual(result_mem.address, 4)
