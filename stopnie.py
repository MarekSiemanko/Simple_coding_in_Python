print('Zmien stopnie C na F i odwrotnie ')
opcja = input('C na F wybierz 1,  F na C wybierz 2. Wybór: ')

if opcja == '1':
    print('Zmiana C na F')
    wartosc = int(input('Podaj wartosc w Cejciuszach: '))
    result = (wartosc * 9/5) + 32
    print(f'{wartosc} C = {result:.2f} F')
elif opcja == '2':
    print('Zmiana F na C')
    wartosc = int(input('Podaj wartosc w Farenheitach: '))
    result = (wartosc - 32) * 5/9
    print(f'{wartosc} F = {result:.2f} C')
else:
    print('Nie ma takiej opcji')
    quit()
    
print('Tyle fajrant')