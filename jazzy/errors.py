class JazError(Exception):
    """Base class for exceptions in this module."""
    pass

class FunctionExistError(JazError):
    def __init__(self, name):
        self.name = name
        self.message = "Function " + name + " already exists!";

class CommandNotFoundError(JazError):
    def __init__(self, action):
        self.message = "Command '" + action + "' not found!";

class StackUnderFlowError(JazError):
    def __init__(self, action):
        self.message = action;

class UndenfinedVariableError(JazError):
    def __init__(self, name):
        self.message = "Variable: " + str(name) + " is being accessed before it is defined!";
