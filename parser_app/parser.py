import requests
from bs4 import BeautifulSoup as BS
from django.views.decorators.csrf import csrf_exempt

URL = "https://kassir.kg/"

HEADERS = {
    "Accept": "text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3;q=0.7",
    "User-Agent": "Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/117.0.0.0 Safari/537.36",
}


@csrf_exempt
def get_html(url, params=''):
    req = requests.get(URL, headers=HEADERS, params=params)
    return req


@csrf_exempt
def get_data(html):
    soup = BS(html, 'html.parser')
    items = soup.find_all("div", class_='event-card d-flex flex-row d-lg-block')
    kassir_kg = []

    for item in items:
        kassir_kg.append(
            {
                "title_name": item.find("div", class_='EventsList_event_title__pExiP').get_text(),
                "title_url": URL + item.find('a').get('href'),
                "image": URL + item.find("div", class_='justify-self:center;object-fit:contain').find("img").get("crs"),
            }
        )

    return kassir_kg


@csrf_exempt
def parser():
    html = get_html(URL)
    if html.status_code == 200:
        kassir_kg2 = []
        for page in range(0, 1):
            html = get_html(f'https://kassir.kg/events/13', params=page)
            kassir_kg2.extend(get_data(html.text))
            print(kassir_kg2)
    else:
        raise Exception('Ошибка парсинга')


parser()
