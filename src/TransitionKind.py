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
    AFTER_POINT_NUMBER = 11
    INT_I = 12
    INT_N = 13
    INT_T = 14
    SPACE = 15
    UNARY_MINUS_FIRST_SIC = 16
    E_NUMBER = 17
    E_NUMBER_OPERATOR = 18
    E_NUMBER_OPERATOR_NUMBER = 19



