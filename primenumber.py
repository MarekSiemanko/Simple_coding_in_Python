try:
    num = int(input('Enter any number and check if they are prime or not prime: '))

    flag = False

    if num == 0 or num == 1:
        print(f'{num} is not a prime number')
    elif num > 1:
        for i in range(2, num):
            if (num % i) == 0:

                flag = True

                break

        if flag:
            print(f'{num} is not a prime number')
        else:
            print(f'{num} is a prime number')
except ValueError:
    print('Its not number put integer')