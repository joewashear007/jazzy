import sys
import functions
import interpreter
import preprocessor
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
        mofFunc = getattr(functions, mod)
        for func in mofFunc.Functions:
            try:
                funcClass = getattr(mofFunc, func)
                jazFunc = funcClass()
                intrp.RegisterFunction(jazFunc.command, jazFunc)
            except Exception as err:
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
        processor = preprocessor.Preprocessor()
        code = processor.parseFile(filename)
        labels = processor.GetLabels()
        intrp.SetLabels(labels)
        for line in code:
            try:
                output = intrp.Exec(line)
                print(output)
            except CommandNotFoundError as error:
                print(error.message)
    except Exception as err:
        print(err)


if __name__ == "__main__":
    # execute only if run as a script
    main(sys.argv[1:])
