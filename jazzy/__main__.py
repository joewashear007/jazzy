
def main():
    print("Running Jazzy!")
    import interperter
    intrp = interperter.Interperter()

    action = input(">>")
    print(intrp.Exec(action))






if __name__ == "__main__":
    # execute only if run as a script
    main()
