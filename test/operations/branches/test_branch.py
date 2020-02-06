from memory import MemoryTypes
from operations import Operations
from test.operations.operation_test import OperationTestBase


class BranchTest(OperationTestBase):

    def test_br_basic(self):
        memory_type = MemoryTypes.BASIC
        initial_data = "\n".join([
            "BR 4",
            "BR 0"])

        result_mem = self.run_pc(memory_type, self.parse_input(initial_data))
        self.assertEqual(self.parse_input(initial_data), result_mem.data)
        self.assertEqual(4, result_mem.address)

    def test_br_mod_access_l(self):
        memory_type = MemoryTypes.MODIFIED_ACCESS
        initial_data = "\n".join([
            "BR 4L",
            "BR 0L"])

        result_mem = self.run_pc(memory_type, self.parse_input(initial_data))
        self.assertEqual(self.parse_input(initial_data), result_mem.data)
        self.assertEqual(4, result_mem.address)

    def test_br_mod_access_r(self):
        memory_type = MemoryTypes.MODIFIED_ACCESS
        initial_data = "\n".join([
            "BR 2, 5",  # Skip to position 5 (stored in position 2)
            "BR 0L"])

        result_mem = self.run_pc(memory_type, self.parse_input(initial_data))
        self.assertEqual(self.parse_input(initial_data), result_mem.data)
        self.assertEqual(5, result_mem.address)
