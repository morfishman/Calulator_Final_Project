from Parser import *


def calc_postfix_expression(expiration: str):
    stack_of_operands = []
    for element in expiration:
        if not isinstance(element, GenericIdentifier):
            stack_of_operands.append(element)
        else:
            if element.unary:
                stack_of_operands.append(round(element.calc(stack_of_operands.pop()), 10))
            else:
                p2 = stack_of_operands.pop()
                p1 = stack_of_operands.pop()
                stack_of_operands.append(round(element.calc(p1, p2), 10))
    return stack_of_operands


expression = ""

try:
    expression = input()
    if expression == "":
        print("nothing mate :)")
    else:
        element_lex = Parser(expression)
        element_lex.calc_postfix()
        print(calc_postfix_expression(element_lex.final_expo)[0])

except SyntaxExpressionException as e:
    print("SyntaxError at this element:", expression[e.index])
except ZeroDivisionError as e:
    print(e)
except OverflowError as e:
    print(e)
except ArithmeticError as e:
    print(e)
except IndexError as e:
    print(e)
except KeyboardInterrupt as e:
    print("stopping")
except EOFError as e:
    print("stopping")
