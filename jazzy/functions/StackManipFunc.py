all__ = ['jazPush', 'jazRvalue', 'jazLvalue', 'jazPop', 'jazAssign', 'jazCopy']

class jazPush:
    def __init__(self):
        self.command = "push";

    def call(self, interpreter, arg):
        pass
        #return interpreter.GetScope().GetStackTop()

class jazRvalue:
    def __init__(self):
        self.command = "rvalue";

    def call(self, interpreter, arg):
        pass
        #return interpreter.GetScope().GetStackTop()

class jazLvalue:
    def __init__(self):
        self.command = "lvalue";

    def call(self, interpreter, arg):
        pass
        #return arg;

class jazPop:
    def __init__(self):
        self.command = "pop";

    def call(self, interpreter, arg):
        pass
        #return arg;

class jazAssign:
    def __init__(self):
        self.command = ":=";

    def call(self, interpreter, arg):
        pass
        #return arg;

class jazCopy:
    def __init__(self):
        self.command = "copy";

    def call(self, interpreter, arg):
        pass
        #return arg;

# A dictionary of the classes in this file
# used to autoload the functions
Functions = {'jazPush': jazPush, 'jazRvalue': jazRvalue, 'jazLvalue': jazRvalue, 'jazPop':jazPop, 'jazAssign':jazAssign, 'jazCopy':jazCopy}
