def dodaj(a, b):
    return a + b

def odejmij(a, b):
    return a - b

def mnoz(a, b):
    return a * b

def dziel(a, b):
    if b == 0:
        return "Nie można dzielić przez zero!"
    return a / b

def kalkulator():
    print("Prosty Kalkulator")
    print("1. Dodawanie")
    print("2. Odejmowanie")
    print("3. Mnożenie")
    print("4. Dzielenie")

    wybor = input("Wybierz operację (1/2/3/4): ")

    if wybor in ['1', '2', '3', '4']:
        num1 = float(input("Podaj pierwszą liczbę: "))
        num2 = float(input("Podaj drugą liczbę: "))

        if wybor == '1':
            print(f"Wynik: {dodaj(num1, num2)}")
        elif wybor == '2':
            print(f"Wynik: {odejmij(num1, num2)}")
        elif wybor == '3':
            print(f"Wynik: {mnoz(num1, num2)}")
        elif wybor == '4':
            print(f"Wynik: {dziel(num1, num2)}")
    else:
        print("Nieprawidłowy wybór")

if __name__ == "__main__":
    kalkulator()