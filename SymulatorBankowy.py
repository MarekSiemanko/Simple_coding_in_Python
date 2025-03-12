class Account:
    def __init__(self, owner, balance=0):
        self.owner = owner
        self.balance = balance
        self.transactions = []

    def deposit (self, amount):
        self.balance += amount
        self.transactions.append(f"Deposit: {amount}")

    def withdraw(self, amount):
        if amount > self.balance:
            print("Niewystarczający fundusz")
        else:
            self.balance -= amount
            self.transactions.append(f"Withdraw: {amount}")

    def get_balance(self):
        return self.balance

    def get_transactions(self):
        return self.transactions

    def main_menu():
        print("1. Stwórz konto")
        print("2. Depozyt")
        print("3. Wycofać")
        print("4. Sprawdź saldo")
        print("5. Pokaż transakcje")
        print("6. Wyjdź")

        choice = input("Wybierz opcję: ")
        return choice
    