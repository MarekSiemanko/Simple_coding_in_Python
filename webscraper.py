#Jak działa ten kod:
# # Import bibliotek: Importujemy requests do wysyłania zapytań HTTP i BeautifulSoup do parsowania HTML.
# Wysyłanie zapytania: Używamy requests.get() do pobrania zawartości strony.
# # Sprawdzanie statusu: Upewniamy się, że żądanie zakończyło się sukcesem (status 200).
# Parsowanie HTML: Tworzymy obiekt BeautifulSoup i wyszukujemy elementy HTML, które nas interesują. W tym przykładzie zakładamy, że tytuły artykułów znajdują się w tagach <h2> z klasą article-title.
# # # Wyświetlanie wyników: Iterujemy przez znalezione tytuły i wyświetlamy ich tekst.
# # Dostosowanie
# Pamiętaj, aby dostosować selektory w soup.find_all() do struktury HTML strony, którą chcesz zeskrobać. Możesz używać różnych selektorów, takich jak tagi, klasy, identyfikatory itp.

import requests
from bs4 import BeautifulSoup
#żądanie HTTP do strony
def scrape_titles(url):
    response = requests.get(url)

    if response.status_code == 200:
        soup = BeautifulSoup(response.text, 'html.parser') #parsujemy HTML

        titles = soup.find_all('h2', class_='article-title')

        for title in titles:
            print(title.get.text())
    else:
        print(f"Nie udało sie polaczyc z {url}. Status kod: {response.status_code}")
url = 'https://www.wp.pl'
scrape_titles(url)