from pypc.memory import MemoryTypes
from test.operations.operation_test import OperationTestBase


class BranchEqualsTest(OperationTestBase):

    def test_be_basic(self):
        memory_type = MemoryTypes.BASIC
        initial_data = "\n".join([
            "BE 99, 99, 5",
            "END"])

        result_mem = self.run_pc(memory_type, self.parse_input(initial_data))
        self.assertEqual(self.parse_input(initial_data), result_mem.data)
        self.assertEqual(5, result_mem.address)

    def test_be_basic_false(self):
        memory_type = MemoryTypes.BASIC
        initial_data = "\n".join([
            "BE 1, 99, 5",
            "END"])

        result_mem = self.run_pc(memory_type, self.parse_input(initial_data))
        self.assertEqual(self.parse_input(initial_data), result_mem.data)
        self.assertEqual(4, result_mem.address)

    def test_be_mod_access_ll(self):
        memory_type = MemoryTypes.MODIFIED_ACCESS
        initial_data = "\n".join([
            "BE 1L, 99L, 5",
            "END"])

        result_mem = self.run_pc(memory_type, self.parse_input(initial_data))
        self.assertEqual(self.parse_input(initial_data), result_mem.data)
        self.assertEqual(4, result_mem.address)

    def test_be_mod_access_lr(self):
        memory_type = MemoryTypes.MODIFIED_ACCESS
        initial_data = "\n".join([
            "BE 5L, 3, 5",
            "END"])

        result_mem = self.run_pc(memory_type, self.parse_input(initial_data))
        self.assertEqual(self.parse_input(initial_data), result_mem.data)
        self.assertEqual(5, result_mem.address)

    def test_be_mod_access_rr(self):
        memory_type = MemoryTypes.MODIFIED_ACCESS
        initial_data = "\n".join([
            "BE 2, 3, 5",
            "END"])

        result_mem = self.run_pc(memory_type, self.parse_input(initial_data))
        self.assertEqual(self.parse_input(initial_data), result_mem.data)
        self.assertEqual(4, result_mem.address)
