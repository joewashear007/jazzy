import uuid
from errors import *
class Scope:
    def __init__(self):
        self.pc = 0;
        self.variables = {}
        self.lvalue = self
        self.rvalue = self
        self.stack = [1, 2, 3]
        self.name = uuid.uuid1()

    def CreateVar(self, name):
        # creates a variable with default value
        # each value in the dictionary is (address, value)
        # the var_addr maps the address of a var to its na,e
        self.variables[name] = (len(self.variables), 0)
        return self.variables[name]

    def GetVar(self, name):
        if name in self.variables:
            return self.variables[name][1]
        else:
            raise UndenfinedVariableError(name)

    def GetAddress(self, name):
        if name in self.variables:
            return self.variables[name][0]
        else:
            return self.CreateVar(name)[0]

    def GetVarFromAddress(self, addr):
        if(int(addr) < len(self.variables)):
            for address, value in self.variables.iteritems():
                if address is addr:
                    return value;
        return None


    def Step(self):
        self.pc = self.pc+1

    def PC(self,number=None):
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
