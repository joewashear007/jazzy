__all__ = ['jazGT', 'jazET', 'jazGTET', 'jazLT', 'jazLTET', 'jazGL']

class jazGT:
    def __init__(self):
        self.command = ">";

    def call(self, interpreter, arg):
        topValue1 = interpreter.GetScope().stack.pop()
        topValue2 = interpreter.GetScope().stack.pop()
        if (topValue2 > topValue1):
            interpreter.GetScope().stack.append(1)
        else:
            interpreter.GetScope().stack.append(0)
        return None

class jazET:
    def __init__(self):
        self.command = "=";

    def call(self, interpreter, arg):
        topValue1 = interpreter.GetScope().stack.pop()
        topValue2 = interpreter.GetScope().stack.pop()
        if (topValue2 == topValue1):
            interpreter.GetScope().stack.append(1)
        else:
            interpreter.GetScope().stack.append(0)
        return None

class jazGTET:
    def __init__(self):
        self.command = ">=";

    def call(self, interpreter, arg):
        topValue1 = interpreter.GetScope().stack.pop()
        topValue2 = interpreter.GetScope().stack.pop()
        if (topValue2 >= topValue1):
            interpreter.GetScope().stack.append(1)
        else:
            interpreter.GetScope().stack.append(0)
        return None

class jazLT:
    def __init__(self):
        self.command = "<";

    def call(self, interpreter, arg):
        topValue1 = interpreter.GetScope().stack.pop()
        topValue2 = interpreter.GetScope().stack.pop()
        if (topValue2 < topValue1):
            interpreter.GetScope().stack.append(1)
        else:
            interpreter.GetScope().stack.append(0)
        return None

class jazLTET:
    def __init__(self):
        self.command = "<=";

    def call(self, interpreter, arg):
        topValue1 = interpreter.GetScope().stack.pop()
        topValue2 = interpreter.GetScope().stack.pop()
        if (topValue2 <= topValue1):
            interpreter.GetScope().stack.append(0)
        else:
            interpreter.GetScope().stack.append(1)
        return None

class jazGL:
    def __init__(self):
        self.command = "<>";

    def call(self, interpreter, arg):
        topValue1 = interpreter.GetScope().stack.pop()
        topValue2 = interpreter.GetScope().stack.pop()
        if (topValue2 != topValue1):
            interpreter.GetScope().stack.append(1)
        else:
            interpreter.GetScope().stack.append(0)
        return None

Functions = {'jazGT': jazGT, 'jazET': jazET, 'jazGTET': jazGTET, 'jazLT':jazLT, 'jazLTET':jazLTET, 'jazGL':jazGL}
