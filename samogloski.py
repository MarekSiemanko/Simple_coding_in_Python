from collections import Counter
word = input('Enter any words and check how many vowels have: ')
vowels = 'aeiouAEIOU'
# vowels - samogłoski
cnt = Counter(i for i in word if i in vowels)
print(cnt)
print(f'Total vowels: {sum(cnt.values())}')
