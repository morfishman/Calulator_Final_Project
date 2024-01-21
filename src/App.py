from Parser import *



def calc_postfix_expretion(expretion: str):
    stack_of_operands = []
    for element in expretion:
        if not isinstance(element,GenericIdentifier):
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
while expression != "exit":
    try:
        expression = input()
        if expression == "":
            print("nothing mate :)")
        else:
            elementa = Parser(expression)
            elementa.calc_postfix()
            print(calc_postfix_expretion(elementa.final_expo)[0])

    except SyntaxExpretionExeption as e:
        print("SyntaxError at this element:", expression[e.index])
    except ArithmeticError as e:
        print(e)
    except KeyboardInterrupt as e:
        print("stoping")
    except EOFError as e:
        print("stoping")
    except ZeroDivisionError as e:
        print(e)
    except IndexError as e:
        print(e)
    except OverflowError as e:
        print(e)



