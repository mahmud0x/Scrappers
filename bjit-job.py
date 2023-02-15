#This script will get all available jobs from bjit website
import requests
URL = "https://wwwcms.bjitgroup.com/career?limit=99&page=1&country=Bangladesh"
response = (requests.get(URL)).json()
job_count = int(response["total"])
#print(response["list"][1]["position"])
print("Total Jobs: "+str(job_count))
print("\nJob Title: ")
for i in range(0,job_count):
    job_title = response["list"][i]["position"]
    print(str(i+1)+". "+job_title.strip())