from scope import Scope
from errors import *


debug = True

class Interpreter:
    def __init__(self, labels = {}):
        self.running = True
        self.program = []
        self.scopes = []
        self.labels = {}
        self.functions = {}
        self.scopes.append(Scope());
        self.pcscope = -1

    def GetLabel(self, name):
        return self.labels[name]

    def CreateScope(self):
        # Use -1 as the index since pop() operates on the end of the list
        self.scopes.append(Scope());
        self.scopes[-1].PC(self.scopes[-2].PC())
        return self.scopes[-1]

    def DestroyTopScope(self):
        if len(self.scopes) > 1:
            old = self.scopes.pop();
            # self.curScope = self.scopes[-1];
            return old;
        else:
            raise StackUnderFlowError("On the Root Stack!, Use 'halt' to quit")

    def GoTo(self, line) :
        if line < len(self.program):
            self.scopes[-1].PC(line)
        else:
            raise errors.BadLineNumberError(line)

    def Exec(self, instruction) :
        instruction=instruction.strip()
        if len(instruction) < 1:
            return None

        #Find the argument of the program
        split_inst = instruction.strip().split(' ', 1)
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
        pc = self.PC()
        out = self.Exec(self.program[pc])
        self.scopes[self.pcscope].Step()
        if self.scopes[self.pcscope].PC() > len(self.program) :
            self.Halt()
        # return "PC: " + str(pc) + " = " + str(out)
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

    def PC(self, value = None):
        if value is not None:
            return self.scopes[self.pcscope].PC(value)
        return self.scopes[self.pcscope].PC()

    def BeginSubroutine(self):
        #Creates a new Scope
        #set the pcscope to -2 to continue using the pc until the call
        #Reassigns the right scrope to allow varible to declared on the new scope
        self.CreateScope()
        self.pcscope = -2;
        self.scopes[-1].RValue(self.scopes[-2])

    def EndSubroutine(self):
        self.pcscope = -1
        self.DestroyTopScope()

    def CallSubroutine(self, label):
        # Set the proper PC
        self.pcscope = -1
        self.scopes[-1].RValue(self.scopes[-1])
        self.scopes[-1].LValue(self.scopes[-1])
        if label in self.labels:
            self.GoTo(self.labels[label])
        else:
            raise errors.UndenfinedLabelError(label)

    def ReturnSubroutine(self):
        #Switches the Left and Right Scopes so the varible are assign to the
        #   parent scope when return from function
        self.scopes[-1].RValue(self.scopes[-1])
        self.scopes[-1].LValue(self.scopes[-2])
        self.pcscope = -2
