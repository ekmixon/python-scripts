import requests
import re

# get url
url = input('Enter a URL (include `http://`): ')

# connect to the url
website = requests.get(url)

# read html
html = website.text

# use re.findall to grab all the links
links = re.findall('"((http|ftp)s?://.*?)"', html)
emails = re.findall('([\w\.,]+@[\w\.,]+\.\w+)', html)


# print the number of links in the list
print(f"\nFound {len(links)} links")
for email in emails:
    print(email)
