#program to check a prime number


num = 29

#to take input from user
# num = int(input("Enter a random number:"))

#define a flag variable 
flag = False

if num == 0 or num ==1:
    print("It is no t a prime number")
else:
    if num > 1:
        for i in range(2,num):
            if (num % i) == 0:
                flag = True
            #breaking out of loop
                break

    # check if flag = True

    if flag:
        print(num, "It is not a prime number")
    else:
        print(num, "It is a prime number")