import sys
import os
import argparse
import functions
import interpreter
import preprocessor
from errors import *;


def main(args):
    parser = argparse.ArgumentParser(description='Jaz Interpreter')
    parser = argparse.ArgumentParser()
    parser.add_argument('infile', nargs='?', type=argparse.FileType('r'), default=sys.stdin)
    parser.add_argument('outfile', nargs='?', type=argparse.FileType('w'),default=sys.stdout)
    parser.parse_args();
    args = parser.parse_args()

    intrp = interpreter.Interpreter()
    RegisterFunctions(intrp)

    if(args.infile is not sys.stdin):
        #run the file
        RunFile(intrp, args.infile, args.outfile)
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
        except JazError as error:
            print("Error! -- " + error.message)
        except Exception as err:
            print("Error! -- " + str(err))

def RunFile(intrp, infile, outfile):
    # output = []
    try:
        processor = preprocessor.Preprocessor()
        code = processor.parseFile(infile)
        labels = processor.GetLabels()
        intrp.labels = labels
        intrp.program = code
        while not intrp.isFinished():
            output = intrp.ExecNext()
            if output is not None:
                outfile.write(str(output))
                outfile.write("\n")
    except JazError as error:
        print("Error! -- " + error.message)

if __name__ == "__main__":
    # execute only if run as a script
    main(sys.argv[1:])
