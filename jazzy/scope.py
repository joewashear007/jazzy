class Scope:
    def __init__(self):
        self.pc = 0;
        self.variables = {}
        self.lvalue = self
        self.ralue = self
        self.stack = [1,2,3]

    def GetVar(self, name):
        if name in self.variables:
            return self.variables[name]
        else:
            return None

    def SetVar(self, name, value):
        self.variables[name] = value

    def Step(self):
        self.pc = self.pc+1

    def SetPC(self,number=None):
        if number is not None:
            self.pc = number
        return self.pc

    def GetStackTop(self):
        return self.stack[-1]

    def LValue(self, newScope = None ):
        if newScope is not None:
            self.lvalue = newScope
        return self.lvalue

    def RValue(self, newScope = None ):
        if newScope is not None:
            self.rvalue = newScope
        return self.rvalue
