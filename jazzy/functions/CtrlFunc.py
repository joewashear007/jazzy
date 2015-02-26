__all__ = ['jazHalt', 'jazLabel', 'jazGoto', 'jazGofalse', 'jazGotrue']


class jazHalt:
    def __init__(self):
        self.command = "halt";

    def call(self, interpreter, arg):
        return interpreter.Halt()

class jazLabel:
    def __init__(self):
        self.command = "label";

    def call(self, interpreter, arg):
        return none

class jazGoto:
    def __init__(self):
        self.command = "goto";

    def call(self, interpreter, arg):
        return none

class jazGofalse:
    def __init__(self):
        self.command = "gofalse";

    def call(self, interpreter, arg):
        return none

class jazGotrue:
    def __init__(self):
        self.command = "gotrue";

    def call(self, interpreter, arg):
        return none
        
# A dictionary of the classes in this file
# used to autoload the functions
Functions = {'jazHalt': jazHalt, 'jazLabel': jazLabel, 'jazGoto': jazGoto, 'jazGofalse': jazGofalse, 'jazGotrue': jazGotrue}
