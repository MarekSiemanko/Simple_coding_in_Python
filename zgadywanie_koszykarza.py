def zgadywanie_koszykarza():
    koszykarze = {
        "Micheal Jordan": ["Sześciokrotny mistrz NBA", "sześciokrotny MVP finałów", "najlepszy z najlepszych"],
        "Bill Rusell": ["zdobył 11 mistrzowskich pierścieni.", "Jego nawiększym rywalem był Wilt Chamberlain"],
        "Lebron James": ["Najlepszy strzelec w historii NBA", "Wybrany w drafcie z numerem 1"]
        }
    
    import random
    koszykarz, wskazowki = random.choice(list(koszykarze.items()))

    print("Zgadnij, koszykarza na podstawie wskazowek")

    for i, wskazowka in enumerate(wskazowki, start=1):
        print(f"Wskazowka {i}: {wskazowka}")

    while True:
        #pobieranie odpowiedzi
        odpowiedz = input("Wpisz pełna nazwe koszykarza: ").strip()

        #sprawdzenie odpowiedzi
        if odpowiedz.lower() == koszykarz.lower():
            print("Gratulacje! Poprawna odpowiedz")
            break
        else:
            print("sprobuj innego")

zgadywanie_koszykarza()