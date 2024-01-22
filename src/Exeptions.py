class SyntaxExpressionException(Exception):
    def __init__(self, index):
        self.index = index
        self.message = f'bad syntax at index:{index}'
        super().__init__(self.message)
