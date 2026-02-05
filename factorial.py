num =5
factorial =1 

if num < 0:
    print("facotrialk  doesnot exist")
elif num == 0:
    print("Factorial of number o is 1")
else:
    for i in range(1, num + 1):
        factorial = factorial * i

    print(f"The factorial of {num} is {factorial}")