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
        interpreter.labels[arg] = interpreter.curScope.pc
        return None

class jazGoto:
    def __init__(self):
        self.command = "goto";

    def call(self, interpreter, arg):
        if arg in interpreter.labels:
            interpreter.GoTo(interpreter.labels[arg])
        return None

class jazGofalse:
    def __init__(self):
        self.command = "gofalse";

    def call(self, interpreter, arg):
        value = interpreter.GetScope().stack.pop()
        if value == 0:
            interpreter.GoTo(interpreter.labels[arg])
        return None

class jazGotrue:
    def __init__(self):
        self.command = "gotrue";

    def call(self, interpreter, arg):
        value = interpreter.GetScope().stack.pop()
        if value != 0:
            interpreter.GoTo(interpreter.labels[arg])
        return None

# A dictionary of the classes in this file
# used to autoload the functions
Functions = {'jazHalt': jazHalt, 'jazLabel': jazLabel, 'jazGoto': jazGoto, 'jazGofalse': jazGofalse, 'jazGotrue': jazGotrue}
