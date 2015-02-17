import sys
import functions
import interpreter
from errors import *;


def main(args):
    print("Running Jazzy!")

    intrp = interpreter.Interpreter()
    RegisterFunctions(intrp)

    if(len(args) > 0):
        #run the file
        RunFile(intrp, args[0])
    else:
        #read from std in
        RunSdtIn(intrp)






def RegisterFunctions(intrp):
    #Register the Funcitons
    for mod in functions.__all__:
        __import__("functions."+mod)
        mofFunc = getattr(functions, "OutputFunc")
        for func in mofFunc.Functions:
            try:
                funcClass = getattr(mofFunc, func)
                jazFunc = funcClass()
                intrp.RegisterFunction(jazFunc.command, jazFunc)
            except err:
                print(err.message)

def RunSdtIn(intrp):
    action = input(">>")
    try:
        output  =intrp.Exec(action)
        print(output)
    except CommandNotFoundError as err:
        print(err.message)

def RunFile(intrp, filename):
    try:
        file = open(filename, 'r')
        for line in file:
            output = intrp.Exec(line)
            print(output)
    except err:
        print(err)


if __name__ == "__main__":
    # execute only if run as a script
    main(sys.argv[1:])
