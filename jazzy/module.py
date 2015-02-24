import sys
import argparse
import jazzy.functions
import jazzy.interpreter
import jazzy.preprocessor
from jazzy.errors import *;


def main():
    parser = argparse.ArgumentParser(description='Jaz Interpreter')
    parser = argparse.ArgumentParser()
    parser.add_argument('infile', nargs='?', type=argparse.FileType('r'), default=sys.stdin)
    parser.add_argument('outfile', nargs='?', type=argparse.FileType('w'),default=sys.stdout)
    parser.parse_args();
    args = parser.parse_args()

    intrp = jazzy.interpreter.Interpreter()
    RegisterFunctions(intrp)

    if(args.infile is not sys.stdin):
        #run the file
        RunFile(intrp, args.infile, args.outfile)
    else:
        #read from std in
        RunSdtIn(intrp)

def RegisterFunctions(intrp):
    #Register the Funcitons
    for mod in jazzy.functions.__all__:
        __import__("jazzy.functions."+mod)
        mofFunc = getattr(jazzy.functions, mod)
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

def RunFile(intrp, infile, outfile):
    # output = []
    try:
        processor = jazzy.preprocessor.Preprocessor()
        code = processor.parseFile(infile)
        labels = processor.GetLabels()
        intrp.labels = labels
        intrp.program = code
        while not intrp.isFinished():
            output= intrp.ExecNext()
            # print(output[-1])
            if output is not None:
                outfile.write(output)
    except CommandNotFoundError as error:
        print("Error! -- " + error.message)
    except StackUnderFlowError as error:
        print("Error! -- " + error.message)
    except Exception as err:
        print("Error! -- " + err)


if __name__ == "__main__":
    # execute only if run as a script
    main()
