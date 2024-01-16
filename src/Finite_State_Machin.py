
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


