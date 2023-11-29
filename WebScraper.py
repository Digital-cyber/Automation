import requests
from bs4 import BeautifulSoup

def get_news_headlines(url):
    response = requests.get(url)
    soup = BeautifulSoup(response.text, 'html.parser')
    
    headlines = soup.find_all('h2', class_='headline')
    
    for index, headline in enumerate(headlines, start=1):
        print(f"{index}. {headline.text.strip()}")

get_news_headlines("https://www.example-news-site.com")
