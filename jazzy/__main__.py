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
    while not intrp.isFinished():
        print("")
        action = input(">>")
        try:
            output = intrp.Exec(action)
            if output is not None:
                print(output)
        except Exception as err:
            print(err.message)

def RunFile(intrp, filename):
    try:
        processor = preprocessor.Preprocessor()
        code = processor.parseFile(filename)
        labels = processor.GetLabels()
        intrp.labels = labels
        intrp.program = code
        while not intrp.isFinished():
            output = intrp.ExecNext()
            print(output)
    except CommandNotFoundError as error:
        print("Error! -- " + error.message)
    except StackUnderFlowError as error:
        print("Error! -- " + error.message)
    except Exception as err:
        print("Error! -- " + err)


if __name__ == "__main__":
    # execute only if run as a script
    main(sys.argv[1:])
