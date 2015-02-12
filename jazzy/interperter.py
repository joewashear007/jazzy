# class interface GenericInterperter {
#         CreateScope: Function;
#         DestroyScope: Function;
#         GoTo: Function;
#     }
from scope import Scope
from functions import OutputFunc
from errors import *


debug = True

class Interperter:
    def __init__(self):
        self.program = []
        self.scopes = []
        self.lables = {}
        self.functions = {}
        self.curScope = Scope()
        self.scopes.append(self.curScope);
        for func in OutputFunc.Functions:
            jazFunc = OutputFunc.Functions[func]()
            self.RegisterFunction(jazFunc.command, jazFunc)


    def CreateScope(self):
        # Use -1 as the index since pop() operates on the end of the list
        self.scopes.append(Scope());
        self.scopes[-1].PC(self.curScope.PC())
        return self.scopes[-1]


    def DestroyTopScope(self):
        old = self.scopes.pop();
        self.curScope = self.scopes[-1];
        return old;

    def GoTo(self, line) :
        if line < self.program.count():
            self.curScope.PC(line);

    def Exec(self, instruction) :
        if len(instruction) < 1:
            return "No instruction"
        split_inst = instruction.split(' ', 1)
        action = split_inst[0]
        if len(split_inst) is 2:
            arg = split_inst[1]
        else:
            arg = ""
        if debug:
            print("#Debug: Running: "+action+" with "+arg)
        if action in self.functions:
            return self.functions[action].call(self, arg)
        else:
            raise CommandNotFoundError(action)

    def GetScope(self):
        return self.scopes[-1];

    def RegisterFunction(self, name, func):
        if name not in self.functions:
            self.functions[name] = func
        else:
            raise FunctionExistError(name)
