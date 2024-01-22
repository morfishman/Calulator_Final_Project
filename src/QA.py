from Parser import *
import pytest


def calc_postfix_expression(expression: str):
    stack_of_operands = []
    for element in expression:
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


def for_pytest(input_ex: str):
    element = ""
    expression = ""
    try:
        expression = input_ex
        if expression == "":
            print("nothing mate :)")
        else:
            element = Parser(expression)
            element.calc_postfix()
            print(calc_postfix_expression(element.final_expo)[0])
        return calc_postfix_expression(element.final_expo)[0]

    except SyntaxExpressionException as e:
        print("SyntaxError at this element:", expression[e.index])
    except ZeroDivisionError as e:
        print(e)
    except OverflowError as e:
        print(e)
    except ArithmeticError as e:
        print(e)
    except KeyboardInterrupt:
        print("stopping")
    except EOFError:
        print("stopping")
    except IndexError as e:
        print(e)


expressions = [
    ("1+2*7^3-5/2", 684.5),
    ("12&4&6-8%3", 2.0),
    ("(3+5)*2-4+7*(2-1)", 19.0),
    ("10$5%3*2+(7-4)", 5.0),
    ("8^(-2)+4/2-1", 1.015625),
    ("2@3+4*(6-2)", 18.5),
    ("~-7-3*(2+1)", -2.0),
    ("int(8.9)-2*3+5", 7.0),
    ("3%2+6/2-1", 3.0),
    ("4*3-7+(2^3)", 13.0),
    ("5-2+6*3", 21.0),
    ("7+9-2*5", 6.0),
    ("2@4-1", 2.0),
    ("3#-2+7", 8.0),
    ("6$8+3-1", 10.0),
    ("9@2/3-1", 0.8333333333),
    ("(-5)^2+3*4", 37.0),
    ("(2+3)*(4-1)+(8/2)", 19.0),
    ("4*(7-3)-2%3+6$2", 20.0),
    ("1+2^3*4-(8%3@2)", 32.5),
    ("((((((((~-3!!^~-3!)#/5) ^ 100)#!#) + ~-(5&2$4)!#)%7 / 10 ) ^ 2 * 1000) % 3)! + ~-------((((((((~-3!!^~-3!)#/5) ^"
     " 100)#!#) + ~-(5&2$4)!#)%7 / 10 ) ^ 2 * 1000) %  3)!", 2.0)
]


@pytest.mark.parametrize("_input, result", expressions)
def test_mytest(_input, result):
    assert for_pytest(_input) == result
