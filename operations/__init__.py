from enum import Enum, unique

from operations.base_op import BaseOp
from .move import MoveOp
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
        mod_a1 = (op_id // 100) % 10
        mod_a2 = (op_id // 1000) % 10

        return Operations(op).operation_class(mod_a1, mod_a2)

    @property
    def operation_class(self):
        """Get operation class via reflection."""
        clazzname = self.name.title() + "Op"
        if clazzname == "NopOp":
            clazz = BaseOp
        else:
            clazz = globals()[clazzname]
        return clazz
