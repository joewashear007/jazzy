__all__ = ['jazAND', 'jazNOT', 'jazOR']

class jazAND:
    def __init__(self):
        self.command = "&";

    def call(self, interpreter, arg):
        topValue1 = interpreter.GetScope().stack.pop()
        topValue2 = interpreter.GetScope().stack.pop()
        interpreter.GetScope().stack.append( int(topValue1) & int(topValue2))
        return None


class jazNOT:
    def __init__(self):
        self.command = "!";

    def call(self, interpreter, arg):
        topValue = interpreter.GetScope().stack.pop()
        interpreter.GetScope().stack.append(int( not topValue))
        return None

class jazOR:
    def __init__(self):
        self.command = "|";

    def call(self, interpreter, arg):
        topValue1 = interpreter.GetScope().stack.pop()
        topValue2 = interpreter.GetScope().stack.pop()
        interpreter.GetScope().stack.append( int(topValue1) | int(topValue2))
        return None
Functions = {'jazAND': jazAND, 'jazNOT': jazNOT, 'jazOR': jazOR}
