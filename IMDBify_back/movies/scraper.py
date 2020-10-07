from bs4 import BeautifulSoup
from requests import get
import re

def scrape(url):
    main_response = get(url)
    soup = BeautifulSoup(main_response.text, 'lxml')

    movies = soup.select('td.titleColumn')
    links = [a.attrs.get('href') for a in soup.select('td.titleColumn a')]
    imdb_data = []

    for index in range(0, 3):
        movie_str = movies[index].get_text()
        movie = (' '.join(movie_str.split()).replace('.', ''))
        name = movie[len(str(index)) + 1:-7]
        year = re.search('\((.*?)\)', movie_str).group(1)

        movie_detail_page = get('https://www.imdb.com' + links[index])
        movie_detail_soup = BeautifulSoup(movie_detail_page.content, 'lxml')
        img_link = movie_detail_soup.find('div', class_='poster').select('a img')[0]['src']
        director_name = movie_detail_soup.find('div', class_='credit_summary_item').text.split(':')[1].replace("\n", "")

        imdb_data.append({
            "name": name,
            "image": img_link,
            "year_of_release": year,
            "director": director_name
        })

    return imdb_data


