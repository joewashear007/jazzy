__all__ = ['jazHalt']


class jazHalt:
    def __init__(self):
        self.command = "halt";

    def call(self, interpreter, arg):
        return interpreter.Halt()


# A dictionary of the classes in this file
# used to autoload the functions
Functions = {'jazHalt': jazHalt}
