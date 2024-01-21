from Lexer import *

class Parser:
    def __init__(self, expression:str):
        """
        :param expression: User Expression
        :returns new Object that by using Lexer can lex , And Pars this expression to a Postfix Expretion
        :raise SyntaxExpretionExeption
        """
        self.lexerment = Lexer(expression)
        for i in range(len(expression)):
            self.lexerment.next()
        if not (self.lexerment.accept_state[self.lexerment.current_state]):
            raise SyntaxExpretionExeption(self.lexerment.index-1)
        self.final_expo = []


