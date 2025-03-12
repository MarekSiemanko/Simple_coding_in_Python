from collections import Counter
Numbers = input('Enter any integer number to count how many is it: ')
Numbers_all = '1234567890'

count = Counter (i for i in Numbers if i in Numbers_all)
print(f'Total numbers : {sum(count.values())}')
