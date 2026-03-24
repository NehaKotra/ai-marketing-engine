import requests
from bs4 import BeautifulSoup


def get_website_content(url):

    response = requests.get(url)

    soup = BeautifulSoup(response.text, "html.parser")

    paragraphs = soup.find_all("p")

    text = ""

    for p in paragraphs:
        text += p.get_text()

    return text[:4000]