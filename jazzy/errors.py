class JazError(Exception):
    """Base class for exceptions in this module."""
    pass

class FunctionExistError(JazError):
    def __init__(self, name):
        self.name = name
        self.message = "Function " + name + " already exists!";

class CommandNotFoundError(JazError):
    def __init__(self, action):
        self.name = name
        self.message = "Command " + action + " not found!";
