from .branches import *
from .compares import *
from operations.op import Op
from operations.errors import OpEndError
from operations.add import AddOp
from operations.multiply import MulOp
from operations.input import InpOp
from operations.output import OutOp


def from_id(op_id):
    op = op_id % 100
    mod_a1 = (op_id // 100) % 10
    mod_a2 = (op_id // 1000) % 10

    if op == 0: return Op()
    elif op == 1: return AddOp(mod_a1, mod_a2)
    elif op == 2: return MulOp(mod_a1, mod_a2)
    elif op == 3: return InpOp()
    elif op == 4: return OutOp(mod_a2)
    elif op == 11: return BeOp(mod_a1, mod_a2)
    elif op == 12: return BneOp(mod_a1, mod_a2)
    elif op == 13: return BnzOp(mod_a1, mod_a2)
    elif op == 14: return BzOp(mod_a1, mod_a2)
    elif op == 21: return LtOp(mod_a1, mod_a2)
    elif op == 22: return LteOp(mod_a1, mod_a2)
    elif op == 23: return EqOp(mod_a1, mod_a2)
    elif op == 99: raise OpEndError()
    else: raise IndexError("Invalid op code " + str(op_id))
