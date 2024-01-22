import math


class GenericIdentifier:

    def __init__(self, value: str, priority: float):
        """
        :param value: gets string value,of the Identifier
        :param priority: the priority of the operator
        :returns new object of generic operator
        """
        self.priority = priority
        self.value = value
        self.unary = False


class Bracket(GenericIdentifier):
    def __init__(self, value: str, priority: float, side: int):
        """
        :param value: gets string value,of the Identifier
        :param priority: the priority of the operator
        :param side: the side of the bracket 0 == ( , 1 == )
        :returns new object of generic operator
        """
        super().__init__(value, priority)
        self.side = side
        self.unary = True


class LBracket(Bracket):
    def __init__(self):
        """
        :returns new L bracket element
        """
        super().__init__('(', 0, 0)


class RBracket(Bracket):
    def __init__(self):
        """
        :returns new R bracket element
        """
        super().__init__(')', 10, 1)


class UnaryMinus(GenericIdentifier):
    def __init__(self):
        """
            returns new Minus Unary Operator (when the minus is not after operator)
        """
        super().__init__('-', 3.5)
        self.unary = True

    @staticmethod
    def calc(param: float) -> float:
        """
        :param param:
        :return: flip the sign of a float param
        :raise OverflowError
        """

        if float != type(param):
            raise OverflowError(f"Max Num Exceeded from {param}")
        if param >= float('inf') or param <= float('-inf'):
            raise OverflowError(f"Max Num Exceeded from {param}")
        returnable = 0.0 - param
        if float != type(returnable):
            raise OverflowError(f"Max Num Exceeded from {-param}")
        return returnable


class MaxUnaryMinus(GenericIdentifier):
    def __init__(self):
        """
        returns new Minus Max Unary Operator (when the minus is after operator)
        """
        super().__init__('-', 7)
        self.unary = True

    @staticmethod
    def calc(param: float) -> float:
        """
        :param param:
        :return: flip the sign of a float param
        :raise OverflowError
        """
        if float != type(param):
            raise OverflowError(f"Max Num Exceeded from {param}")
        if param >= float('inf') or param <= float('-inf'):
            raise OverflowError(f"Max Num Exceeded from {param}")
        returnable = 0.0 - param
        if float != type(returnable):
            raise OverflowError(f"Max Num Exceeded from {-param}")
        return returnable


class Int(GenericIdentifier):
    def __init__(self):
        """
        returns new Int Operator
        """
        super().__init__('int', 6)
        self.unary = True

    @staticmethod
    def calc(param: float) -> float:
        """
        :param param:
        :return: remove the digits after the point
        :raise OverflowError
        """
        if float != type(param):
            raise OverflowError(f"Max Num Exceeded from {param}")
        if param >= float('inf') or param <= float('-inf'):
            raise OverflowError(f"Max Num Exceeded from {param}")
        returnable = float(int(param))
        if float != type(returnable):
            raise OverflowError(f"Max Num Exceeded from {-param}")
        return returnable


class Tilda(GenericIdentifier):
    def __init__(self):
        """
        returns new Tilda Operator
        """
        super().__init__('~', 6)
        self.unary = True

    @staticmethod
    def calc(param: float) -> float:
        """
        :param param:
        :return: flip the sign of a float param
        :raise OverflowError
        """
        if float != type(param):
            raise OverflowError(f"Max Num Exceeded from {param}")
        if param >= float('inf') or param <= float('-inf'):
            raise OverflowError(f"Max Num Exceeded from {param}")
        returnable = 0.0 - param
        if float != type(returnable):
            raise OverflowError(f"Max Num Exceeded from {-param}")
        return returnable


class Factorial(GenericIdentifier):
    def __init__(self):
        """
        returns new Factorial Operator
        """
        super().__init__('!', 6)
        self.unary = True

    @staticmethod
    def calc(param: float) -> float:
        """
        :param param: float number
        :return: the value of the factorial of the param
        :raise ArithmeticError
        :raise OverflowError
        """
        if float != type(param):
            raise OverflowError(f"Max Num Exceeded from {param}")
        if param >= float('inf') or param <= float('-inf'):
            raise OverflowError(f"Max Num Exceeded from {param}")
        if int(param) < 0:
            raise ArithmeticError(f"factorial of a negative param: {param}!")
        if param * 10 % 10 != 0:
            raise ArithmeticError(f"factorial of a uncompleted param: {param}!")
        if int(param) == 0:
            return float(1)
        sum = 1
        for i in range(1, int(param) + 1):
            sum *= float(i)
            round(sum, 10)
            if float != type(sum) or (sum >= float('inf') or sum <= float('-inf')):
                raise OverflowError(f"Max Num Exceeded from {param}!")
        return sum


class Hash(GenericIdentifier):
    def __init__(self):
        """
        returns new Hash Operator
        """
        super().__init__('#', 6)
        self.unary = True

    @staticmethod
    def calc(param: float) -> float:

        """
        :param param: float number
        :return: the value of the hash of the param
        :raise ArithmeticError
        :raise OverflowError
        """

        if float != type(param):
            raise OverflowError(f"Max Num Exceeded from {param}")
        if param >= float('inf') or param <= float('-inf'):
            raise OverflowError(f"Max Num Exceeded from {param}")
        if param < 0:
            raise ArithmeticError(f"hash of a negative param: {param}#")
        if param == 0:
            return 0
        if param >= float('inf') or param <= float('-inf'):
            raise OverflowError(f"hash too large param: inf#")
        list_operand = list(str(param))
        if 'e' in list_operand:
            return sum(
                float(list_operand[char]) for char in range(list_operand.index('e')) if list_operand[char].isnumeric())
        return sum(float(char) for char in list_operand if char.isnumeric())


class Minus(GenericIdentifier):
    """
    returns new Minus Binary Operator
    """

    def __init__(self):
        super().__init__('-', 1)
        self.unary = False

    @staticmethod
    def calc(p1: float, p2: float) -> float:
        """

        :param p1: float,
        :param p2:  float
        :return: operand -operand
        :raise OverflowError
        """
        if float != type(p1):
            raise OverflowError(f"Max Num Exceeded from {p1}")
        if float != type(p2):
            raise OverflowError(f"Max Num Exceeded from {p2}")
        if not float('-inf') < p1 < float('inf') or not float('-inf') < p2 < float('inf'):
            raise OverflowError(f"Max Num Exceeded")

        return p1 - p2


class Plus(GenericIdentifier):
    def __init__(self):
        """
        returns new Plus Binary Operator
        """
        super().__init__('+', 1)
        self.unary = False

    @staticmethod
    def calc(p1: float, p2: float) -> float:
        """

        :param p1: operand float,
        :param p2:  operand float
        :return: operand + operand
        :raise OverflowError
        """
        if float != type(p1):
            raise OverflowError(f"Max Num Exceeded from {p1}")
        if float != type(p2):
            raise OverflowError(f"Max Num Exceeded from {p2}")
        if not float('-inf') < p1 < float('inf') or not float('-inf') < p2 < float('inf'):
            raise OverflowError(f"Max Num Exceeded")

        return p1 + p2


class Mul(GenericIdentifier):
    def __init__(self):
        """
        returns new Mul Binary Operator
        """
        super().__init__('*', 2)
        self.unary = False

    @staticmethod
    def calc(p1: float, p2: float) -> float:
        """
        :param p1: operand float,
        :param p2:  operand float
        :return: operand * operand
        :raise OverflowError
        """
        if float != type(p1):
            raise OverflowError(f"Max Num Exceeded from {p1}")
        if float != type(p2):
            raise OverflowError(f"Max Num Exceeded from {p2}")
        if not float('-inf') < p1 < float('inf') or not float('-inf') < p2 < float('inf'):
            raise OverflowError(f"Max Num Exceeded")
        returnable = p1 * p2
        if float != type(returnable) or not float('-inf') < returnable < float('inf'):
            raise OverflowError(f"Max Num Exceeded from {p1}*{p2}")
        return returnable


class Div(GenericIdentifier):
    def __init__(self):
        """
        returns new Div Binary Operator
        """
        super().__init__('/', 2)
        self.unary = False

    @staticmethod
    def calc(p1: float, p2: float) -> float:
        """

        :param p1: operand float,
        :param p2:  operand float
        :return: operand / operand
        :raise ZeroDivisionError
        :raise OverflowError
        """
        if float != type(p1):
            raise OverflowError(f"Max Num Exceeded from {p1}")
        if float != type(p2):
            raise OverflowError(f"Max Num Exceeded from {p2}")
        if not float('-inf') < p1 < float('inf') or not float('-inf') < p2 < float('inf'):
            raise OverflowError(f"Max Num Exceeded")
        if p1 == 0:
            raise ZeroDivisionError("Cant divide by zero")
        returnable = p1 / p2
        if float != type(returnable) or not float('-inf') < returnable < float('inf'):
            raise OverflowError(f"Max Num Exceeded from {p1}/{p2}")
        return returnable


class Min(GenericIdentifier):
    def __init__(self):
        """
        returns new Min Binary Operator
        """
        super().__init__('&', 5)
        self.unary = False

    @staticmethod
    def calc(p1: float, p2: float) -> float:
        """

        :param p1: operand,
        :param p2: operand
        :return: the lowest value between them
        :raise OverflowError
        """
        if float != type(p1):
            raise OverflowError(f"Max Num Exceeded from {p1}")
        if float != type(p2):
            raise OverflowError(f"Max Num Exceeded from {p2}")
        if not float('-inf') < p1 < float('inf') or not float('-inf') < p2 < float('inf'):
            raise OverflowError(f"Max Num Exceeded")
        return min(p1, p2)


class Power(GenericIdentifier):
    def __init__(self):
        """
        returns new Power Binary Operator
        """
        super().__init__('^', 3)
        self.unary = False

    @staticmethod
    def calc(p1: float, p2: float) -> float:
        """
        :param p1: operand,
        :param p2: operand
        :return: p1 ^ p2
        :raise ZeroDivisionError
        :raise ArithmeticError
        :raise OverflowError
        """
        if float != type(p1):
            raise OverflowError(f"Max Num Exceeded from {p1}")
        if float != type(p2):
            raise OverflowError(f"Max Num Exceeded from {p2}")
        if not float('-inf') < p1 < float('inf') or not float('-inf') < p2 < float('inf'):
            raise OverflowError(f"Max Num Exceeded")
        if p1 == 0 and p2 < 0:
            raise ZeroDivisionError(f"cant divide by zero {p1}^{p2} = {p1}/{p2}")
        if p1 < 0 and p2 * 10 % 10 != 0:
            raise ArithmeticError(f"sqrt of negative number {p1}^{p2}")
        try:
            returnable = math.pow(p1, p2)
        except OverflowError:
            raise OverflowError(f"Max Num Exceeded from {p1}^{p2}")
        if float != type(returnable) or not float('-inf') < returnable < float('inf'):
            raise OverflowError(f"Max Num Exceeded from {p1}^{p2}")
        return returnable


class Avg(GenericIdentifier):
    def __init__(self):
        """
        returns new Avg Binary Operator
        """
        super().__init__('@', 5)
        self.unary = False

    @staticmethod
    def calc(p1: float, p2: float) -> float:
        """

        :param p1: Operand,
        :param p2: Operand
        :return: the average between the 2 operands
        :raise OverflowError
        """
        if float != type(p1):
            raise OverflowError(f"Max Num Exceeded from {p1}")
        if float != type(p2):
            raise OverflowError(f"Max Num Exceeded from {p2}")
        if not float('-inf') < p1 < float('inf') or not float('-inf') < p2 < float('inf'):
            raise OverflowError(f"Max Num Exceeded")
        returnable = (p1 + p2) / 2.0
        if not float('-inf') < returnable < float('inf'):
            raise OverflowError(f"Max Num Exceeded")
        return returnable


class Max(GenericIdentifier):
    def __init__(self):
        """
        returns new Max Binary Operator
        """
        super().__init__('$', 5)
        self.unary = False

    @staticmethod
    def calc(p1: float, p2: float) -> float:
        """
        :param p1: Operand,
        :param p2: Operand
        :return: Maximum Value Between the Operand
        :raise OverflowError
        """
        if float != type(p1):
            raise OverflowError(f"Max Num Exceeded from {p1}")
        if float != type(p2):
            raise OverflowError(f"Max Num Exceeded from {p2}")
        if not float('-inf') < p1 < float('inf') or not float('-inf') < p2 < float('inf'):
            raise OverflowError(f"Max Num Exceeded")
        return max(p1, p2)


class Mod(GenericIdentifier):
    def __init__(self):
        """
        returns new Mod Binary Operator
        """
        super().__init__('%', 4)
        self.unary = False

    @staticmethod
    def calc(p1: float, p2: float) -> float:
        """
        :param p1:Operand,
        :param p2: Operand
        :return Operand % Operand
        :raise ZeroDivisionError
        :raise OverflowError
        """
        if float != type(p1):
            raise OverflowError(f"Max Num Exceeded from {p1}")
        if float != type(p2):
            raise OverflowError(f"Max Num Exceeded from {p2}")
        if not float('-inf') < p1 < float('inf') or not float('-inf') < p2 < float('inf'):
            raise OverflowError(f"Max Num Exceeded")
        if p2 == 0:
            raise ZeroDivisionError("cant divide by zero")
        returnable = p1 % p2
        if float != type(returnable) or not float('-inf') < returnable < float('inf'):
            raise OverflowError(f"Max Num Exceeded from {p1}%{p2}")
        return returnable
