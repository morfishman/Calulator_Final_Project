from src.TransitionKind import TransitionKind
from Operators_Claster import *
def is_minus(char:str):
    """

    :param char:
    :return: if it is a -
    """
    return char == '-'

def is_plus(char:str):
    """

    :param char:
    :return: if it is a +
    """
    return char == '+'

def is_digit(char:str):
    """

    :param char:
    :return: if it is a digit
    """
    return '0' <= char <='9'

def is_mul(char:str):
    """

    :param char:
    :return: if it is a *
    """
    return char == '*'

def is_div(char:str):
    """

    :param char:
    :return: if it is a /
    """
    return char == '/'

def is_l_braket(char:str):
    """

    :param char:
    :return: if it is a (
    """
    return char == '('

def is_r_braket(char:str):
    """

    :param char:
    :return: if it is a )
    """
    return char == ')'

def is_point(char:str):
    """

    :param char:
    :return: if it is a .
    """
    return char == '.'

def is_tilda(char:str):
    """

    :param char:
    :return: if it is a ~
    """
    return char == '~'

def is_atzeret(char:str):
    """

    :param char:
    :return: if it is a !
    """
    return char == '!'

def is_min(char:str):
    """

    :param char:
    :return: if it is a &
    """
    return char == '&'

def is_power(char:str):
    """

    :param char:
    :return: if it is a ^
    """
    return char == '^'

def is_avg(char:str):
    """

    :param char:
    :return: if it is a @
    """
    return char == '@'

def is_max(char:str):
    """

    :param char:
    :return: if it is a $
    """
    return char == '$'

def is_mod(char:str):
    """

    :param char:
    :return: if it is a %
    """
    return char == '%'

def defult(char:str):
    """

    :param char:
    :return: always returns True
    """
    return True

def add_to_buffer(buffer:str,new:str):
    """
    :param buffer: the temp buffer for the numbers int the Finite State Machine
    :param new: the char that is a digit
    :return: the new buffer + the param
    """
    buffer+=new
    return buffer

def from_str_to_num(buffer:str,farsh = 2):
    """
    :param buffer: the temp buffer for the numbers int the Finite State Machine
    :param fresh: none useble element for polymorephizem
    :return: the new number from the buffer
    """
    return float(buffer)

class FsmTable:

    def __init__(self):
        """
        :returns new Fsm (Finite State Machine Element) Object
        """
        self._transitions = {}
        #start only unary_right or number or (              *****
        self._transitions[TransitionKind.START] =\
        {

            is_minus:[TransitionKind.UNARY_MINUS,None,UnaryMinus],
            is_digit:[TransitionKind.DECIMAL,add_to_buffer],
            is_l_braket:[TransitionKind.L_BRAKET,None,LBraket],
            is_tilda:[TransitionKind.UNARY_R_OPERATOR,None,Tilda], #---------
            defult: [TransitionKind.BAD_INPUT],
        }
        # only number or operator unary_left                *****
        self._transitions[TransitionKind.DECIMAL] = \
        {
            is_atzeret:[TransitionKind.UNARY_L_OPERATOR,from_str_to_num,Atzeret], #---------
            is_digit: [TransitionKind.DECIMAL,add_to_buffer,None],
            is_point: [TransitionKind.AFTER_POINT,add_to_buffer,None],
            is_r_braket: [TransitionKind.R_BRAKET,from_str_to_num,RBraket],
            is_plus: [TransitionKind.BINARY_OPERATOR,from_str_to_num,Plus],
            is_mod:[TransitionKind.BINARY_OPERATOR,from_str_to_num,Mod],
            is_max:[TransitionKind.BINARY_OPERATOR,from_str_to_num,Max],
            is_avg:[TransitionKind.BINARY_OPERATOR,from_str_to_num,Avg],
            is_power:[TransitionKind.BINARY_OPERATOR,from_str_to_num,Power],
            is_minus: [TransitionKind.BINARY_OPERATOR,from_str_to_num,Minus],
            is_min: [TransitionKind.BINARY_OPERATOR, from_str_to_num, Min],
            is_mul: [TransitionKind.BINARY_OPERATOR,from_str_to_num,Mul],
            is_div: [TransitionKind.BINARY_OPERATOR,from_str_to_num,Div],
            defult: [TransitionKind.BAD_INPUT],
        }
        # only number                                       *****
        self._transitions[TransitionKind.AFTER_POINT] = \
        {
            is_digit:[TransitionKind.FLOAT,add_to_buffer,None],
            defult:[TransitionKind.BAD_INPUT]
        }
        # only number or operator, unary_left               *****
        self._transitions[TransitionKind.FLOAT] = \
        {
            is_atzeret: [TransitionKind.UNARY_L_OPERATOR, from_str_to_num, Atzeret],  # ---------
            is_digit: [TransitionKind.FLOAT,add_to_buffer,None],
            is_r_braket: [TransitionKind.R_BRAKET,from_str_to_num,RBraket],
            is_plus: [TransitionKind.BINARY_OPERATOR,from_str_to_num,Plus],
            is_minus: [TransitionKind.BINARY_OPERATOR,from_str_to_num,Minus],
            is_min: [TransitionKind.BINARY_OPERATOR, from_str_to_num, Min],
            is_mul: [TransitionKind.BINARY_OPERATOR,from_str_to_num,Mul],
            is_div: [TransitionKind.BINARY_OPERATOR,from_str_to_num,Div],
            is_mod: [TransitionKind.BINARY_OPERATOR, from_str_to_num, Mod],
            is_max: [TransitionKind.BINARY_OPERATOR, from_str_to_num, Max],
            is_avg: [TransitionKind.BINARY_OPERATOR, from_str_to_num, Avg],
            is_power: [TransitionKind.BINARY_OPERATOR, from_str_to_num, Power],
            defult: [TransitionKind.BAD_INPUT],
        }
        #only number or ( or unary_right
        self._transitions[TransitionKind.BINARY_OPERATOR] =\
        {
            is_digit: [TransitionKind.DECIMAL,add_to_buffer,None],
            is_l_braket: [TransitionKind.L_BRAKET,None,LBraket],
            is_minus: [TransitionKind.UNARY_MINUS,None,MaxUnaryMinus],
            is_tilda: [TransitionKind.UNARY_R_OPERATOR, None, Tilda],  # ---------
            defult: [TransitionKind.BAD_INPUT]
        }
        #only numbers and unary_right and (
        self._transitions[TransitionKind.L_BRAKET] = \
        {
            is_digit:[TransitionKind.DECIMAL,add_to_buffer,None],
            is_minus:[TransitionKind.UNARY_MINUS,None,MaxUnaryMinus],
            is_l_braket: [TransitionKind.L_BRAKET,None,LBraket],
            is_tilda: [TransitionKind.UNARY_R_OPERATOR, None, Tilda],  # ---------
            defult: [TransitionKind.BAD_INPUT]
        }
        #only unary_minus,number,(
        self._transitions[TransitionKind.UNARY_MINUS] = \
        {
            is_minus: [TransitionKind.UNARY_MINUS,None,MaxUnaryMinus],
            is_digit: [TransitionKind.DECIMAL,add_to_buffer,None],
            is_l_braket: [TransitionKind.L_BRAKET,None,LBraket],
            defult: [TransitionKind.BAD_INPUT],
        }
        #only unary_left, operator, )                       *****
        self._transitions[TransitionKind.R_BRAKET] = \
        {
            is_atzeret: [TransitionKind.UNARY_L_OPERATOR, None, Atzeret],  # ---------
            is_r_braket: [TransitionKind.R_BRAKET,None,RBraket],
            is_plus: [TransitionKind.BINARY_OPERATOR,None,Plus],
            is_minus: [TransitionKind.BINARY_OPERATOR,None,Minus],
            is_mul: [TransitionKind.BINARY_OPERATOR,None,Mul],
            is_min: [TransitionKind.BINARY_OPERATOR, None, Min],
            is_div: [TransitionKind.BINARY_OPERATOR,None,Div],
            is_mod: [TransitionKind.BINARY_OPERATOR, None, Mod],
            is_max: [TransitionKind.BINARY_OPERATOR, None, Max],
            is_avg: [TransitionKind.BINARY_OPERATOR, None, Avg],
            is_power: [TransitionKind.BINARY_OPERATOR, None, Power],
            defult: [TransitionKind.BAD_INPUT]
        }
        #only unary_minus, (, number
        self._transitions[TransitionKind.UNARY_R_OPERATOR] = \
        {
            is_minus: [TransitionKind.UNARY_MINUS, None, MaxUnaryMinus],
            is_digit: [TransitionKind.DECIMAL, add_to_buffer, None],
            is_l_braket: [TransitionKind.L_BRAKET, None, LBraket],
            defult: [TransitionKind.BAD_INPUT]
        }
        #binary operator,),unary_left                        *****
        self._transitions[TransitionKind.UNARY_L_OPERATOR] = \
        {
            is_atzeret: [TransitionKind.UNARY_L_OPERATOR, None, Atzeret],  # ---------
            is_r_braket: [TransitionKind.R_BRAKET, None, RBraket],
            is_plus: [TransitionKind.BINARY_OPERATOR, None, Plus],
            is_minus: [TransitionKind.BINARY_OPERATOR, None, Minus],
            is_mul: [TransitionKind.BINARY_OPERATOR, None, Mul],
            is_min: [TransitionKind.BINARY_OPERATOR, None, Min],
            is_div: [TransitionKind.BINARY_OPERATOR, None, Div],
            is_mod: [TransitionKind.BINARY_OPERATOR, None, Mod],
            is_max: [TransitionKind.BINARY_OPERATOR, None, Max],
            is_avg: [TransitionKind.BINARY_OPERATOR, None, Avg],
            is_power: [TransitionKind.BINARY_OPERATOR, None, Power],
            defult: [TransitionKind.BAD_INPUT]
        }

        self.accept_state = {
            TransitionKind.UNARY_L_OPERATOR:True,
            TransitionKind.UNARY_R_OPERATOR: False,
            TransitionKind.R_BRAKET:True,
            TransitionKind.UNARY_MINUS:False,
            TransitionKind.L_BRAKET:False,
            TransitionKind.BINARY_OPERATOR:False,
            TransitionKind.FLOAT: True,
            TransitionKind.AFTER_POINT:True,
            TransitionKind.DECIMAL: True,
            TransitionKind.START: True
        }


