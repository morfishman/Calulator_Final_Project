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

    def next(self):
        """

        :return: void, but put the char at [index] in the final expression array as a Identifier
        :raise: SyntaxExpretionExeption
        :raise: IndexError
        """
        if self.current_state == TransitionKind.BAD_INPUT:
            raise SyntaxExpretionExeption(self.index)
        elif self.index >= len(self.input):
            raise IndexError(f"[IndexError] Index Is Out Of The Array Bounds (self.index = {self.index})")
        temp_char = self.input[self.index]
        state = self.current_state
        for tester in self._transitions[state].keys():
            if tester(temp_char):
                for action_at_transition in range(len(self._transitions[state][tester])):
                    if action_at_transition == 0:
                        self.current_state = self._transitions[state][tester][action_at_transition]
                    elif action_at_transition == 2 and self._transitions[state][tester][action_at_transition] is not None:
                        self.final_expression.append(self._transitions[state][tester][action_at_transition]())
                    elif action_at_transition == 1 and self._transitions[state][tester][action_at_transition] is not None:
                        self.buffer = self._transitions[state][tester][action_at_transition](self.buffer,temp_char)
                        if type(self.buffer) != str:
                            self.final_expression.append(self.buffer)
                            self.buffer = ""
                        elif self.index == len(self.input)-1 and self.accept_state[self.current_state]:
                            self.final_expression.append(float(self.buffer))
                            self.buffer = ""
                break
        if self.current_state == TransitionKind.BAD_INPUT:
            raise SyntaxExpretionExeption(self.index)
        self.index += 1

