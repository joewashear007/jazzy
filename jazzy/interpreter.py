from scope import Scope
from errors import *


debug = True

class Interpreter:
    def __init__(self, labels = {}):
        self.running = True
        self.program = []
        self.scopes = []
        self.lables = labels
        self.functions = {}
        self.curScope = Scope()
        self.scopes.append(self.curScope);

    def GetLabel(self, name):
        return self.labels[name]

    def CreateScope(self):
        # Use -1 as the index since pop() operates on the end of the list
        self.scopes.append(Scope());
        self.scopes[-1].PC(self.curScope.PC())
        return self.scopes[-1]

    def DestroyTopScope(self):
        if len(self.scopes) > 1:
            old = self.scopes.pop();
            self.curScope = self.scopes[-1];
            return old;
        else:
            raise StackUnderFlowError("On the Root Stack!, Use 'halt' to quit")

    def GoTo(self, line) :
        if line < self.program.count():
            self.curScope.PC(line);

    def Exec(self, instruction) :
        if len(instruction) < 1:
            return "No instruction"

        #Find the argument of the program
        split_inst = instruction.split(' ', 1)
        action = split_inst[0]
        if len(split_inst) is 2:
            arg = split_inst[1]
        else:
            arg = ""
        # if debug:
        #     print("#Debug: Running: "+action+" with "+arg)
        if action in self.functions:
            return self.functions[action].call(self, arg)
        else:
            raise CommandNotFoundError(action)

    def ExecNext(self):
        out = self.Exec(self.program[self.curScope.PC()])
        self.curScope.Step()
        if self.curScope.PC() == len(self.program) :
            self.Halt()
        return out

    def isFinished(self):
        return not self.running

    def Halt(self):
        # print("#Debug: Halting Program")
        self.running = False

    def GetScope(self, num = -1):
        return self.scopes[num];

    def RegisterFunction(self, name, func):
        if name not in self.functions:
            self.functions[name] = func
        else:
            raise FunctionExistError(name)
