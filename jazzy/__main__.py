import functions
import interpreter


def main():
    print("Running Jazzy!")
    intrp = interpreter.Interpreter()

    #Register the Funcitons
    for mod in functions.__all__:
        __import__("functions."+mod)
        mofFunc = getattr(functions, "OutputFunc")
        for func in mofFunc.Functions:
            funcClass = getattr(mofFunc, func)
            jazFunc = funcClass()
            intrp.RegisterFunction(jazFunc.command, jazFunc)

    action = input(">>")
    print(intrp.Exec(action))






if __name__ == "__main__":
    # execute only if run as a script
    main()
