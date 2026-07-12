for i in range(0,4):
    try:
        a = int(input("Enter Ist number: "))
        b = int(input("Enter IInd number: "))

        c = a/b
        print(c)
    except Exception as e:
        print("Some Error occured")
        print("Error is ", e)