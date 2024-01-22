from Lexer import *


class Parser:
    def __init__(self, expression: str):
        """
        :param expression: User Expression
        :returns new Object that by using Lexer can lex , And Pars this expression to a Postfix Expression
        :raise SyntaxExpressionException
        """
        self.lexer_obj = Lexer(expression)
        for i in range(len(expression)):
            self.lexer_obj.next()
        if not (self.lexer_obj.accept_state[self.lexer_obj.current_state]):
            raise SyntaxExpressionException(self.lexer_obj.index - 1)
        self.final_expo = []

    def calc_postfix(self):
        """
        :return: void, in self.final_expo puts the postfix expression.
        :raise: ArithmeticError
        """
        operators_stack = []
        for element in self.lexer_obj.final_expression:
            if float == type(element):
                self.final_expo.append(element)
            else:
                if isinstance(element, Bracket) and element.side == 0:
                    operators_stack.append(element)
                elif isinstance(element, Bracket) and element.side == 1:
                    while operators_stack != [] and not (operators_stack[len(operators_stack) - 1]).value == '(':
                        self.final_expo.append(operators_stack.pop())
                    if operators_stack == [] or not (operators_stack[len(operators_stack) - 1]).value == '(':
                        raise ArithmeticError(
                            "Not Valid Use Of Brackets: missing '(' ")  # make it more costume exception :)
                    operators_stack.pop()
                elif not operators_stack:
                    operators_stack.append(element)
                else:
                    if element.unary and (isinstance(element, UnaryMinus) or isinstance(element, MaxUnaryMinus)):
                        if (operators_stack[len(operators_stack) - 1]).priority <= element.priority:
                            operators_stack.append(element)
                        else:
                            while operators_stack != [] and not (
                                    (operators_stack[len(operators_stack) - 1]).priority <= element.priority):
                                self.final_expo.append(operators_stack.pop())
                            operators_stack.append(element)
                    else:
                        if (operators_stack[len(operators_stack) - 1]).priority < element.priority:
                            operators_stack.append(element)
                        else:
                            while operators_stack != [] and not (
                                    (operators_stack[len(operators_stack) - 1]).priority < element.priority):
                                self.final_expo.append(operators_stack.pop())
                            operators_stack.append(element)
        while operators_stack:
            operator = operators_stack.pop()
            if isinstance(operator, Bracket):
                raise ArithmeticError("Not Valid Use Of Brackets: missing ')' ")  # make it more costume exception :)
            self.final_expo.append(operator)
