__all__ = ['jazPrint', 'jazShow']


class jazPrint:
    def __init__(self):
        self.command = "print";

    def call(self, interpreter, arg):
        return interpreter.GetScope().GetStackTop()


class jazShow:
    def __init__(self):
        self.command = "show";

    def call(self, interpreter, arg):
        return arg;

# A dictionary of the classes in this file
# used to autoload the functions
Functions = {'jazShow': jazShow, 'jazPrint': jazPrint}
