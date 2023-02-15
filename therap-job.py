import requests
from bs4 import BeautifulSoup

URL = "https://therap.hire.trakstar.com/"
response = requests.get(URL)

soup = BeautifulSoup(response.content, "html.parser")
tags = soup.findAll('h3', {'class': 'js-job-list-opening-name'})
print("Available Jobs: " +str(len(tags))+"\n")
for tag in tags:
    title_content = tag.get('title')
    print(title_content)