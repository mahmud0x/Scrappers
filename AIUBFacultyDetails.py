#This script will get all research papers of AIUB CS faculties with specific keyword
import requests
from bs4 import BeautifulSoup
import re
import pandas as pd

facultyName = []
profileLink = []
paperTitle = []
paperLink = []
val = input("Enter your keyword: ")
df = pd.DataFrame()
i=0
URL = "https://cs.aiub.edu/people/facultiesCS"
page = requests.get(URL)
soup = BeautifulSoup(page.content, "html.parser")
results = soup.findAll(class_="stretched-link")
for result in results:
    profile_link = 'https://cs.aiub.edu'+result.get('href')
    name = result.get_text()
    page = requests.get(profile_link)
    soup = BeautifulSoup(page.content, "html.parser")
    results = soup.find(id="nav-publications")
    items = results.findAll('a',string=re.compile(val))
    if items:
        for item in items:
            paper_title = str(item.get_text())[2:]
            paper_link = item.get('href')
            facultyName.append(name)
            profileLink.append(profile_link)
            paperTitle.append(paper_title.lstrip())
            paperLink.append(paper_link)
            i = i+1
            print("Found Paper -> "+str(i))
df['facultyName'] = facultyName
df['profileLink'] = profileLink
df['paperTitle'] = paperTitle
df['paperLink'] = paperLink
filename = 'FacultyDetails'+val+'.csv'
df.to_csv(filename)
print('Faculty Details saved as '+filename+'.csv')
