__all__ = ['jazAND', 'jazNOT', 'jazOR']

class jazAND:
    def __init__(self):
        self.command = "&";
        
    def call(self, interpreter, arg):
        topValue1 = interpreter.GetScope().stack[-2]
        topValue2 = interpreter.GetScope().stack[-1]
        if (topValue1 and topValue2):
            interpreter.GetScope().stack.append(True)
        else:
            interpreter.GetScope().stack.append(False)
        return None
    
    
class jazNOT:
    def __init__(self):
        self.command = "!";
        
    def call(self, interpreter, arg):
        topValue = interpreter.GetScope().stack[-1]
        not topValue
        interpreter.GetScope().stack.append(topValue)
        return None

class jazOR:
    def __init__(self):
        self.command = "|";
        
    def call(self, interpreter, arg):
        topValue1 = interpreter.GetScope().stack[-2]
        topValue2 = interpreter.GetScope().stack[-1]
        if (topValue1 or topValue2):
            interpreter.GetScope().stack.append(True)
        else:
            interpreter.GetScope().stack.append(False)
        return None
    
Functions = {'jazAND': jazAND, 'jazNOT': jazNOT, 'jazOR': jazOR}