FirstNum = input("enter first number")
#convert to int
FirstNum = int(FirstNum)
SecondNum = input("enter second number")
SecondNum = int(SecondNum)

Total = FirstNum + SecondNum

if Total > 100:
    print("total value is more than 100")
else:
    print("total value is less than or equal to 100")