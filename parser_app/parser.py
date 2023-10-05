import requests
from bs4 import BeautifulSoup as BS
from django.views.decorators.csrf import csrf_exempt

URL = "https://rezka.ag"

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
    items = soup.find_all("div", class_='b-content__inline_items')
    films_list = []

    for item in items:
        films_list.append(
            {
                "title_name": item.find("div", class_='b-content__inline_item-link').get_text(),
                "title_url": URL + item.find('a').get('href'),
                "image": URL + item.find("div", class_='b-content__inline_item-cover').find("img").get("src"),
            }
        )

    return films_list


@csrf_exempt
def parser():
    html = get_html(URL)
    if html.status_code == 200:
        films_list2 = []
        for page in range(0, 1):
            html = get_html(f'https://rezka.ag/films/arthouse/', params=page)
            films_list2.extend(get_data(html.text))
            return films_list2
            # print(films_list2)
    else:
        raise Exception('Ошибка парсинга')


# parser()
