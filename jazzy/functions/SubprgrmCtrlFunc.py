__all__ = ['jazBegin', 'jazEnd', 'jazReturn', 'jazCall', 'jazStackInfo']


class jazBegin:
    def __init__(self):
        self.command = "begin";

    def call(self, interpreter, arg):
        interpreter.BeginSubroutine()
        return None

class jazEnd:
    def __init__(self):
        self.command = "end";

    def call(self, interpreter, arg):
        interpreter.EndSubroutine()
        return None

class jazReturn:
    def __init__(self):
        self.command = "return";

    def call(self, interpreter, arg):
        interpreter.ReturnSubroutine()
        return None

class jazCall:
    def __init__(self):
        self.command = "call";

    def call(self, interpreter, arg):
        interpreter.CallSubroutine(arg)
        return None


class jazStackInfo:
    def __init__(self):
        self.command = "stackinfo"

    def call(self, interpreter, arg):
        if arg is not None and len(arg) > 0:
            try:
                scope = interpreter.scopes[int(arg)]
                info = "Scope: "+str(scope.name)+"\n"
                info += "* PC : " + str(scope.pc) + "\n"
                info += "* Labels : " + str(interpreter.labels) + "\n"
                info += "* Vars : " + str(scope.variables) + "\n"
                info += "* Stack: " + str(scope.stack) + "\n"
                if scope.name == scope.lvalue.name:
                    info += "* LScope : self\n"
                else:
                    info += "* LScope : " + str(scope.lvalue.name) + "\n"
                if scope.name == scope.rvalue.name:
                    info += "* RScope : self\n"
                else:
                    info += "* RScope : " + str(scope.rvalue.name) + "\n"

            except Exception as e:
                print(e)
                return "Index is not valid"
        else:
            info = "Scopes: ("+str(len(interpreter.scopes))+")\n"
            i = 0
            for s in interpreter.scopes:
                info = info + "["+str(i)+"] : "+ str(s.name)+"\n"
                i = i+1;
        return info

# A dictionary of the classes in this file
# used to autoload the functions
Functions = {'jazBegin': jazBegin,'jazEnd': jazEnd, 'jazReturn': jazReturn, 'jazCall':jazCall,'jazStackInfo': jazStackInfo}
