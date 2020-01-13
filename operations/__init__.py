from enum import Enum, unique

from operations.base_op import BaseOp
from operations.errors import OpEndError
from .branches import *
from .compares import *
from .io import *
from .math import *


@unique
class Operations(Enum):
    NOP = 0
    ADD = 1
    MUL = 2
    INP = 3
    OUT = 4
    DIV = 5
    MOD = 6

    BR = 10
    BE = 11
    BNE = 12
    BZ = 13
    BNZ = 14

    EQ = 20
    LT = 21
    LTE = 22

    END = 99

    @staticmethod
    def from_id(op_id):
        op = op_id % 100
        mod_a1 = (op_id // 100) % 10
        mod_a2 = (op_id // 1000) % 10

        def __get_op(_op_id):
            op = Operations(_op_id)
            if op is Operations.NOP:
                return BaseOp
            elif op == Operations.ADD:
                return AddOp
            elif op == Operations.MUL:
                return MulOp
            elif op == Operations.INP:
                return InpBaseOp
            elif op == Operations.OUT:
                return OutBaseOp
            elif op == Operations.DIV:
                return DivOp
            elif op == Operations.MOD:
                return ModOp
            elif op == Operations.BR:
                return BrOp
            elif op == Operations.BE:
                return BeOp
            elif op == Operations.BNE:
                return BneOp
            elif op == Operations.BZ:
                return BzOp
            elif op == Operations.BNZ:
                return BnzOp
            elif op == Operations.EQ:
                return EqOp
            elif op == Operations.LT:
                return LtOp
            elif op == Operations.LTE:
                return LteOp
            elif op == Operations.END:
                raise OpEndError()

        return __get_op(op)(mod_a1, mod_a2)
