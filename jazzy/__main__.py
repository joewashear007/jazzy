
def main():
    print("Running Jazzy!")
    import interperter.interperter
    intrp = interperter.interperter.Interperter()

    action = input(">>")
    intrp.Exec(action)






if __name__ == "__main__":
    # execute only if run as a script
    main()
