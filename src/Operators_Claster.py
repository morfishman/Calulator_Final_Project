class GenericIdentifier:

    def __init__(self, value: str,priority: int):
        """
        :param value: gets string value,of the Identifier
        :param priority: the priority of the operator
        :returns new object of generic operator
        """
        self.priority = priority
        self.value = value
        self.unary = False


class Braket(GenericIdentifier):
    def __init__(self, value: str,priority: int,side: int):
        """
        :param value: gets string value,of the Identifier
        :param priority: the priority of the operator
        :param side: the side of the braket 0 == ( , 1 == )
        :returns new object of generic operator
        """
        super().__init__(value,priority)
        self.side = side
        self.unary = True


class LBraket(Braket):
    def __init__(self):
        """
        :returns new L bracket element
        """
        super().__init__('(', 0,0)


class RBraket(Braket):
    def __init__(self):
        """
        :returns new R bracket element
        """
        super().__init__(')', 10,1)


class UnaryMinus(GenericIdentifier):
    def __init__(self):
        """
        :returns new Minus Unary Operator (when the minus is not after operator)
        """
        super().__init__('-',3.5)
        self.unary = True
    def calc(self,param:float) -> float:
        """
        :param param:
        :return: flip the sign of a float param
        """
        return 0.0-param



class MaxUnaryMinus(GenericIdentifier):
    def __init__(self):
        """
        :returns new Minus Max Unary Operator (when the minus is after operator)
        """
        super().__init__('-',7)
        self.unary = True
    def calc(self,param:float) -> float:
        """
        :param param:
        :return: flip the sign of a float param
        """
        return 0.0-param



class Tilda(GenericIdentifier):
    def __init__(self):
        """
        :returns new Tilda Operator
        """
        super().__init__('~',6)
        self.unary = True
    def calc(self,param:float) -> float:
        """
        :param param:
        :return: flip the sign of a float param
        """
        return 0.0-param

class Atzeret(GenericIdentifier):
    def __init__(self):
        """
        :returns new Atzeret Operator
        """
        super().__init__('!',6)
        self.unary = True

    def calc(self,param:float) -> float:
        """
        :param param: float number
        :return: the value of the factorial of the param
        :raise ArithmeticError
        """
        if int(param) < 0:
            raise ArithmeticError(f"factorial of a negative param: {param}!")
        if int(param)  == 0:
            return 1;
        return float(self.calc(param-1) * param)


class Minus(GenericIdentifier):
    """
    :returns new Minus Binery Operator
    """
    def __init__(self):
        super().__init__('-',1)
        self.unary = False
    def calc(self,p1:float,p2:float) -> float:
        """

        :param p1: operand float
        :param p2:  operand float
        :return: operand -operand
        """
        return p1 - p2


class Plus(GenericIdentifier):
    def __init__(self):
        """
        :returns new Plus Binery Operator
        """
        super().__init__('+',1)
        self.unary = False

    def calc(self,p1:float,p2:float) -> float:
        """

        :param p1: operand float
        :param p2:  operand float
        :return: operand + operand
        """
        return p1 + p2

class Mul(GenericIdentifier):
    def __init__(self):
        """
        :returns new Mul Binery Operator
        """
        super().__init__('*',2)
        self.unary = False

    def calc(self,p1:float,p2:float) -> float:
        """
        :param p1: operand float
        :param p2:  operand float
        :return: operand * operand
        """
        return p1 * p2


class Div(GenericIdentifier):
    def __init__(self):
        """
        :returns new Div Binery Operator
        """
        super().__init__('/',2)
        self.unary = False

    def calc(self,p1:float,p2:float) -> float:
        """

        :param p1: operand float
        :param p2:  operand float
        :return: operand / operand
        :raise ZeroDivisionError
        """
        if p1 == 0:
            raise ZeroDivisionError
        return p1 / p2

class Min(GenericIdentifier):
    def __init__(self):
        """
        :returns new Min Binery Operator
        """
        super().__init__('&',5)
        self.unary = False
    def calc(self,p1:float,p2:float) -> float:
        """

        :param p1: operand
        :param p2: operand
        :return: the lowest value between them
        """
        return min(p1 ,p2)

class Power(GenericIdentifier):
    def __init__(self):
        """
        :returns new Power Binary Operator
        """
        super().__init__('^',3)
        self.unary = False

    def calc(self,p1:float,p2:float) -> float:
        """
        :param p1: operand
        :param p2: operand
        :return: p1 ^ p2
        :raise ZeroDivisionError
        """
        if p1 == 0 and p2 < 0:
            raise ZeroDivisionError
        return p1**p2


class Avg(GenericIdentifier):
    def __init__(self):
        """
        :returns new Avg Binary Operator
        """
        super().__init__('@',5)
        self.unary = False

    def calc(self,p1:float,p2:float) -> float:
        """

        :param p1: Operand
        :param p2: Operand
        :return: the avarage between the 2 operands
        """
        return (p1 + p2) / 2.0

class Max(GenericIdentifier):
    def __init__(self):
        """
        :returns new Max Binary Operator
        """
        super().__init__('$',5)
        self.unary = False

    def calc(self,p1:float,p2:float) -> float:
        """
        :param p1: Operand
        :param p2: Operand
        :return: Maximum Value Between the Operand
        """
        return max(p1,p2)

class Mod(GenericIdentifier):
    def __init__(self):
        """
        :returns new Mod Binary Operator
        """
        super().__init__('%',4)
        self.unary = False

    def calc(self,p1:float,p2:float) -> float:
        """
        :param p1:Operand
        :param p2: Operand
        :return Operand % Operand
        :raise ZeroDivisionError
        """
        if p2 ==0:
            raise ZeroDivisionError
        return p1%p2