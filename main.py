from bs4 import BeautifulSoup
import requests

url = 'https://www.eventbrite.com/d/ny--new-york/tech/?subcategories=2004&page=1'
response = requests.get(url)
soup = BeautifulSoup(response.text, 'html.parser')
div = soup.find_all('div', class_='Stack_root__1ksk7')

for index, event in enumerate(div):
    date_and_location = event.find_all('p', class_='Typography_root__487rx #585163 Typography_body-md__487rx event-card__clamp-line--one Typography_align-match-parent__487rx')
    if len(date_and_location) < 2:
        continue
    event_location = date_and_location[1].text.strip()
    event_date = date_and_location[0].text.strip() 
    event_url = event.a['href']
    event_name = event.a.h3.text
    print(f"Name: {event_name}")
    print(f"URL: {event_url}")
    print(f"Date: {event_date}")
    print(f"Location: {event_location}")

