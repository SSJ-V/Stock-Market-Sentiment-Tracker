# scraper.py
import requests
from bs4 import BeautifulSoup

def get_stock_headlines(stock="AAPL"):
    url = f"https://finviz.com/quote.ashx?t={stock}"
    headers = {'User-Agent': 'Mozilla/5.0'}
    r = requests.get(url, headers=headers)
    soup = BeautifulSoup(r.text, 'html.parser')

    news_table = soup.find('table', class_='fullview-news-outer')
    headlines = []

    for row in news_table.findAll('tr'):
        headline = row.a.text
        headlines.append(headline)

    return headlines
