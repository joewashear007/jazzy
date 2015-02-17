__all__ = ['jazBegin', 'jazEnd', 'jazReturn', 'jazCall']


class jazBegin:
    def __init__(self):
        self.command = "begin";

    def call(self, interpreter, arg):
        return interpreter.GetScope().GetStackTop()


class jazEnd:
    def __init__(self):
        self.command = "end";

    def call(self, interpreter, arg):
        return arg;

class jazReturn:
    def __init__(self):
        self.command = "return";

    def call(self, interpreter, arg):
        return arg;

class jazCall:
    def __init__(self):
        self.command = "call";

    def call(self, interpreter, arg):
        return arg;

# A dictionary of the classes in this file
# used to autoload the functions
Functions = {'jazBegin': jazBegin, 'jazEnd': jazEnd, 'jazReturn': jazReturn, 'jazCall':jazCall}
