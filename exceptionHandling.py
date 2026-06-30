for i in range(0,4):
    a = int(input("Enter number 1:"))
    b = int(input("Enter number 2:"))
    try:
        c = a/b
        print(c)

    except Exception as e:
        print("Error is ", e)