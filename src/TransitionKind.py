from enum import Enum

class TransitionKind(Enum):
    """
    :type: an enum that represrnt the state of the machine
    """
    START = 0
    DECIMAL = 1
    UNARY_MINUS = 2
    UNARY_R_OPERATOR = 3
    UNARY_L_OPERATOR = 4
    BINARY_OPERATOR = 5
    L_BRAKET = 6
    R_BRAKET = 7
    BAD_INPUT =8
    FLOAT = 9
    AFTER_POINT = 10




