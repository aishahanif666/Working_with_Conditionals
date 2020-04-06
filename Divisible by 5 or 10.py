a = int(input("Enter any number: "))
if (a%5 == 0) and (a%10 != 0):
    print("This number is divisible by 5")
elif(a%5 == 0) and (a%10 == 0):
    print("This number is divisible by 10 and 5 both ")
else:
    print("This number is neither divisible by 5 nor by 10")
    