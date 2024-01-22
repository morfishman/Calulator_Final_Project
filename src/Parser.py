from Lexer import *


class Parser:
    def __init__(self, expression: str):
        """
        :param expression: User Expression
        :returns new Object that by using Lexer can lex , And Pars this expression to a Postfix Expretion
        :raise SyntaxExpretionExeption
        """
        self.lexerment = Lexer(expression)
        for i in range(len(expression)):
            self.lexerment.next()
        if not (self.lexerment.accept_state[self.lexerment.current_state]):
            raise SyntaxExpretionExeption(self.lexerment.index - 1)
        self.final_expo = []

    def calc_postfix(self):
        """
        :return: void, in self.final_expo puts the postfix expression.
        :raise: ArithmeticError
        """
        operators_stack = []
        for element in self.lexerment.final_expression:
            if type(element) == float:
                self.final_expo.append(element)
            else:
                if isinstance(element, Braket) and element.side == 0:
                    operators_stack.append(element)
                elif isinstance(element, Braket) and element.side == 1:
                    while operators_stack != [] and not (operators_stack[len(operators_stack) - 1]).value == '(':
                        self.final_expo.append(operators_stack.pop())
                    if operators_stack == [] or not (operators_stack[len(operators_stack) - 1]).value == '(':
                        raise ArithmeticError(
                            "Not Valid Use Of Brakets: missing '(' ")  # make it more castume exeption :)
                    operators_stack.pop()
                elif operators_stack == []:
                    operators_stack.append(element)
                else:
                    if (element).unary and (isinstance(element, UnaryMinus) or isinstance(element, MaxUnaryMinus)):
                        if (operators_stack[len(operators_stack) - 1]).priority <= (element).priority:
                            operators_stack.append(element)
                        else:
                            while operators_stack != [] and not (
                                    (operators_stack[len(operators_stack) - 1]).priority <= (element).priority):
                                self.final_expo.append(operators_stack.pop())
                            operators_stack.append(element)
                    else:
                        if (operators_stack[len(operators_stack) - 1]).priority < (element).priority:
                            operators_stack.append(element)
                        else:
                            while operators_stack != [] and not (
                                    (operators_stack[len(operators_stack) - 1]).priority < (element).priority):
                                self.final_expo.append(operators_stack.pop())
                            operators_stack.append(element)
        while operators_stack != []:
            operator = operators_stack.pop()
            if isinstance(operator, Braket):
                raise ArithmeticError("Not Valid Use Of Brakets: missing ')' ")  # make it more castume exeption :)
            self.final_expo.append(operator)
