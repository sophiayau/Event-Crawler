import time
from bs4 import BeautifulSoup
import requests
import json


def find_events(page_number):
    url = f'https://www.eventbrite.com/d/ny--new-york/tech/?subcategories=2004&page={page_number}'
    response = requests.get(url)

    if response.status_code != 200:
        print(f"Failed to fetch page {page_number}. Status code: {response.status_code}")
        return []

    events = []

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
        print(f"Event Name: {event_name}")
        print(f"Read More: {event_url}")
        print(f"Date: {event_date}")
        print(f"Location: {event_location}")
        print("---"*10)

        events.append({
            "event_name": {event_name},
            "event_url": {event_url},
            "event_date": {event_date},
            "event_location": {event_location}
        })

    return events


def main():

    OUTPUT_FILE = "event_info.jsonl"
    page_number = 1
    
    with open("event_info.jsonl", 'w') as file:
        while True:
            print(f"Searching page {page_number}...\n")
            events = find_events(page_number)
            if not events:
                print(f"No more items to display...")
                print("Halting program execution")
                # if all events have been scraped, reset page number to 1 for the each scrape we do
                # sleeps for 6 seconds (scrapes every 6 seconds)
                # need to implement a hashset so it doesnt keep printing events that we already saw
                page_number = 1
                time.sleep(6)
                print("Starting new search")

                continue
            # implement file writing 
            # for event in events:
            #     file.write(json.dumps(event))
            page_number += 1


        



if __name__ == "__main__":
    main()

