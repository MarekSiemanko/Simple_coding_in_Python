import random
import string

def passwords():
     # Łączenie wszystkich zestawów znaków w jeden ciąg
    characters = string.ascii_letters + string.ascii_lowercase + string.ascii_uppercase + string.digits + string.punctuation
    lenght = 12 # Określenie długości hasła
    # Generowanie hasła
    passwords = ''.join (random.choice(characters) for i in range(lenght))
    print(passwords)
# Wywołanie funkcji
passwords()