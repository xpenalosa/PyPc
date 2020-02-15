from pypc.memory import MemoryTypes
from test.operations.operation_test import OperationTestBase


class BranchNotZeroTest(OperationTestBase):

    def test_bnz_basic(self):
        memory_type = MemoryTypes.BASIC
        initial_data = "\n".join([
            "BNZ 1, 4",
            "END"])

        result_mem = self.run_pc(memory_type, self.parse_input(initial_data))
        self.assertEqual(self.parse_input(initial_data), result_mem.data)
        self.assertEqual(4, result_mem.address)

    def test_bnz_basic_false(self):
        memory_type = MemoryTypes.BASIC
        initial_data = "\n".join([
            "BNZ 0, 4",
            "END"])

        result_mem = self.run_pc(memory_type, self.parse_input(initial_data))
        self.assertEqual(self.parse_input(initial_data), result_mem.data)
        self.assertEqual(3, result_mem.address)

    def test_bnz_mod_access_l(self):
        memory_type = MemoryTypes.MODIFIED_ACCESS
        initial_data = "\n".join([
            "BNZ 0L, 4L",
            "END"])

        result_mem = self.run_pc(memory_type, self.parse_input(initial_data))
        self.assertEqual(self.parse_input(initial_data), result_mem.data)
        self.assertEqual(3, result_mem.address)

    def test_bnz_mod_access_r(self):
        memory_type = MemoryTypes.MODIFIED_ACCESS
        initial_data = "\n".join([
            "BNZ 0, 4L",
            "END"])

        result_mem = self.run_pc(memory_type, self.parse_input(initial_data))
        self.assertEqual(self.parse_input(initial_data), result_mem.data)
        self.assertEqual(4, result_mem.address)
