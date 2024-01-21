from Finite_State_Machin import *
from Exeptions import *

class Lexer(FsmTable):
    def __init__(self,input:str):
        """
        :param input: the expression of the user
        :returns: an object that can lex this expression to Identifier
        """
        super().__init__()
        self.input = input
        self.buffer = ""
        self.index = 0
        self.current_state = TransitionKind.START
        self.final_expression = []
        self.braket_stack = []



