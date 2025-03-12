try:

    i = int(input('Enter number and it shows  is this number is divisible with 3, 5 or both '))

    if i % 3 == 0 and i % 5 == 0:
        print('FizzBuzz')
    elif i % 5 == 0:
        print('Buzz')
    elif i % 3 == 0:
        print('Fizz')
    else:
        print(f'The number is not divisible with 3 or 5 put diffrent number Your choise = {i}')
except ValueError:
    print('WRONG! Enter any integer')
# integer- liczba całkowita
quit()

