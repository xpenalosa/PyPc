from pypc.memory import MemoryTypes
from test.operations.operation_test import OperationTestBase


class BranchNotEqualsTest(OperationTestBase):

    def test_bne_basic(self):
        memory_type = MemoryTypes.BASIC
        initial_data = "\n".join([
            "BNE 1, 99, 5",
            "END"])

        result_mem = self.run_pc(memory_type, self.parse_input(initial_data))
        self.assertEqual(self.parse_input(initial_data), result_mem.data)
        self.assertEqual(5, result_mem.address)

    def test_bne_basic_false(self):
        memory_type = MemoryTypes.BASIC
        initial_data = "\n".join([
            "BNE 99, 99, 5",
            "END"])

        result_mem = self.run_pc(memory_type, self.parse_input(initial_data))
        self.assertEqual(self.parse_input(initial_data), result_mem.data)
        self.assertEqual(4, result_mem.address)

    def test_bne_mod_access_ll(self):
        memory_type = MemoryTypes.MODIFIED_ACCESS
        initial_data = "\n".join([
            "BNE 1L, 99L, 5",
            "END"])

        result_mem = self.run_pc(memory_type, self.parse_input(initial_data))
        self.assertEqual(self.parse_input(initial_data), result_mem.data)
        self.assertEqual(5, result_mem.address)

    def test_bne_mod_access_lr(self):
        memory_type = MemoryTypes.MODIFIED_ACCESS
        initial_data = "\n".join([
            "BNE 2L, 3, 5",
            "END"])

        result_mem = self.run_pc(memory_type, self.parse_input(initial_data))
        self.assertEqual(self.parse_input(initial_data), result_mem.data)
        self.assertEqual(5, result_mem.address)

    def test_bne_mod_access_rr(self):
        memory_type = MemoryTypes.MODIFIED_ACCESS
        initial_data = "\n".join([
            "BNE 5, 3, 5",
            "END"])

        result_mem = self.run_pc(memory_type, self.parse_input(initial_data))
        self.assertEqual(self.parse_input(initial_data), result_mem.data)
        self.assertEqual(5, result_mem.address)
