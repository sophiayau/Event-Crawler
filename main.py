import time
from bs4 import BeautifulSoup
import requests
import json

# making a global set to avoid duplicate events when scraping
seen_url = set()

def find_events(page_number):
    global seen_url
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

        event_url = event.a['href']

        # handling duplicate events
        if event_url in seen_url:
            continue

        seen_url.add(event_url)
        event_location = date_and_location[1].text.strip()
        event_date = date_and_location[0].text.strip() 
        event_name = event.a.h3.text
        print(f"Event Name: {event_name}")
        print(f"Read More: {event_url}")
        print(f"Date: {event_date}")
        print(f"Location: {event_location}")
        print("---"*10)

        events.append({
            "event_name": event_name,
            "event_url": event_url,
            "event_date": event_date,
            "event_location": event_location
        })

    return events

def save_to_json(data, filename="event_info.json"):
    # read in file and append new data to existing data
    try:
        with open(filename, 'r') as json_file:
            existing_data = json.load(json_file)
    except (FileNotFoundError, json.JSONDecodeError):
        existing_data = []

    existing_data.extend(data)
    
    with open(filename, 'w') as json_file:
        json.dump(existing_data, json_file, indent=4)


def main():

    OUTPUT_FILE = "event_info.json"
    page_number = 1
    
    with open(OUTPUT_FILE, 'w') as file:
        while True:
            print(f"Searching page {page_number}...\n")
            events = find_events(page_number)
            if not events:
                print(f"No more items to display...")
                print("Halting program execution and retrying later...")
                page_number = 1
                time.sleep(6)
                print("Starting new search")

                continue

            # implement file writing 
            save_to_json(events, OUTPUT_FILE)
            
            page_number += 1


if __name__ == "__main__":
    main()

