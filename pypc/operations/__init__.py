from enum import Enum, unique

from pypc.operations.base_op import BaseOp
from pypc.operations.branches import *
from pypc.operations.compares import *
from pypc.operations.io import *
from pypc.operations.math import *
from pypc.operations.move import MovOp


@unique
class Operations(Enum):
    NOP = 0
    ADD = 1
    MUL = 2
    INP = 3
    OUT = 4
    DIV = 5
    MOD = 6
    MOV = 7

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
        op_clazz = Operations(op).operation_class
        args = []
        for i in range(0, op_clazz.ARGC):
            mode = (op_id // pow(10, i+2)) % 10
            args.append(mode)
        return op_clazz(*args)

    @property
    def operation_class(self):
        """Get operation class via reflection."""
        clazzname = self.name.title() + "Op"
        if clazzname == "NopOp":
            clazz = BaseOp
        else:
            clazz = globals()[clazzname]
        return clazz
