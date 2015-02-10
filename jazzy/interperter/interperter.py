# class interface GenericInterperter {
#         CreateScope: Function;
#         DestroyScope: Function;
#         GoTo: Function;
#     }
from interperter.scope import Scope

class Interperter:
    def __init__(self):
        self.program = []
        self.scopes = []
        self.lables = {}
        self.functions = {}
        self.curScope = Scope()
        self.scopes.append(self.curScope);

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
        action, arg = instruction.split(' ', 1)
        print("Running: "+action+" with "+arg)
