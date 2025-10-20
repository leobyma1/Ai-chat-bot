while True:
    a = input("Enter value for a (or type 'exit' to stop): ")
    if a.lower() == "exit":
        print("Goodbye!")
        break

    b = input("Enter value for b: ")

    if a == "testing":
        print(a)

    elif a == "testing" and b != "no testing":
        print(a)

    else:
        print(a, b)

    print()
