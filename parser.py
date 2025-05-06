import requests
from bs4 import BeautifulSoup

url = "https://kit.alexgyver.ru/"

response = requests.get(url)
response.raise_for_status()

soup = BeautifulSoup(response.text, "html.parser")

# Ищем все теги <a> с классом 'comp_btn'
items = soup.find_all("a", class_="comp_btn")

# Извлекаем текст из каждого
names = [item.get_text(strip=True) for item in items]

# Выводим список названий
for name in names:
    print(name)
