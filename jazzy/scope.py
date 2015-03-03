import uuid
from errors import *
class Scope:
    def __init__(self):
        self.pc = 0;
        self.variables = {}
        self.lvalue = self
        self.rvalue = self
        self.stack = []
        self.name = uuid.uuid1()

    def CreateVar(self, name):
        # creates a variable with default value
        # each value in the dictionary is (address, value)
        # the var_addr maps the address of a var to its na,e
        self.variables[name] = (len(self.variables), 0)
        return self.variables[name]

    def GetVar(self, name):
        if name in self.rvalue.variables:
            return self.rvalue.variables[name][1]
        else:
            # raise UndenfinedVariableError(name)
            return 0

    def GetAddress(self, name):
        if name in self.lvalue.variables:
            return self.lvalue.variables[name][0]
        else:
            return self.lvalue.CreateVar(name)[0]

    def SetVar(self, name, value):
        try:
            # assume that name is an address of variable
            address = int(name)
            for var in self.lvalue.variables:
                if address == self.lvalue.variables[var][0]:
                    self.lvalue.variables[var] = (self.lvalue.variables[var][0], value)
                    return
            raise UndenfinedVariableError(name)
        except ValueError:
            # name is not a number
            if name in self.lvalue.variables:
                self.lvalue.variables[name] =(self.lvalue.variables[name][0], value)
            else:
                raise UndenfinedVariableError(name)


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
