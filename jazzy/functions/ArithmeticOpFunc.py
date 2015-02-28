__all__ = ['jazAdd', 'jazSubtract', 'jazMultiply', 'jazDivide', 'jazDiv']


class jazAdd:
    def __init__(self):
        self.command = "+";

    def call(self, interpreter, arg):
        topValue1 = interpreter.GetScope().stack[-1]
        topValue2 = interpreter.GetScope().stack[-2]
        result = int(topValue1) + int(topValue2)
        interpreter.GetScope().stack.append(result)
        return None

class jazSubtract:
    def __init__(self):
        self.command = "-";

    def call(self, interpreter, arg):
        topValue1 = interpreter.GetScope().stack[-2]
        topValue2 = interpreter.GetScope().stack[-1]
        result = int(topValue1) - int(topValue2)
        interpreter.GetScope().stack.append(result)
        return None

class jazMultiply:
    def __init__(self):
        self.command = "*";

    def call(self, interpreter, arg):
        topValue1 = interpreter.GetScope().stack[-1]
        topValue2 = interpreter.GetScope().stack[-2]
        result = int(topValue1) * int(topValue2)
        interpreter.GetScope().stack.append(result)
        return None

class jazDivide:
    def __init__(self):
        self.command = "/";

    def call(self, interpreter, arg):
        topValue1 = int(interpreter.GetScope().stack[-2])
        topValue2 = int(interpreter.GetScope().stack[-1])
        result = int(topValue1) / int(topValue2)
        interpreter.GetScope().stack.append(int(result))
        return None

class jazDiv:
    def __init__(self):
        self.command = "div";

    def call(self, interpreter, arg):
        topValue1 = interpreter.GetScope().stack[-2]
        topValue2 = interpreter.GetScope().stack[-1]
        result = int(topValue1) % int(topValue2)
        interpreter.GetScope().stack.append(result)
        return None

# A dictionary of the classes in this file
# used to autoload the functions
Functions = {'jazAdd': jazAdd, 'jazSubtract': jazSubtract, 'jazMultiply': jazMultiply, 'jazDivide': jazDivide, 'jazDiv': jazDiv}
