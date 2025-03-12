try:
    number = int(input("Enter any number to test whether it is even or odd: "))


    if (number % 2 ) == 0:
        print("Number is even")
    else:
        print("the provided number is odd")
except ValueError:
    print("Invalid input! Please enter number")