all__ = ['jazPush', 'jazRvalue', 'jazLvalue', 'jazPop', 'jazAssign', 'jazCopy']

class jazPush:
    def __init__(self):
        self.command = "push"

    def call(self, interpreter, arg):
        interpreter.GetScope().stack.append(arg)
        return None

class jazRvalue:
    def __init__(self):
        self.command = "rvalue"

    def call(self, interpreter, arg):
        value = interpreter.GetScope().GetVar(arg)
        interpreter.GetScope().stack.append(value)
        return None

class jazLvalue:
    def __init__(self):
        self.command = "lvalue"

    def call(self, interpreter, arg):
        address = interpreter.GetScope().GetAddress(arg)
        interpreter.GetScope().stack.append(address)
        return None

class jazPop:
    def __init__(self):
        self.command = "pop"

    def call(self, interpreter, arg):
        interpreter.GetScope().stack.pop()
        return None

class jazAssign:
    def __init__(self):
        self.command = ":="

    def call(self, interpreter, arg):
        value = interpreter.GetScope().stack.pop()
        addr = interpreter.GetScope().stack.pop()
        print(addr, value)
        interpreter.GetScope().SetVar(addr, value)
        return None

class jazCopy:
    def __init__(self):
        self.command = "copy"

    def call(self, interpreter, arg):
        topStack = interpreter.GetScope().stack[-1]
        interpreter.GetScope().stack.append(topStack)
        return None

# A dictionary of the classes in this file
# used to autoload the functions
Functions = {'jazPush': jazPush, 'jazRvalue': jazRvalue, 'jazLvalue': jazRvalue, 'jazPop':jazPop, 'jazAssign':jazAssign, 'jazCopy':jazCopy}
