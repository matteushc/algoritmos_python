import requests
from bs4 import BeautifulSoup

result = requests.get("https://www.whitehouse.gov/briefings-statements/")
src = result.content

soup = BeautifulSoup(src, 'lxml')

docs = []

for x in soup.find_all('div',{'class':'briefing-statement__content'}):
    d = {}
    d['header'] = x.find('p').text
    d['title'] = x.find('a').text
    d['url'] = x.find('a').attrs['href']
    d['footer'] = x.find('p', {'class' : 'issue-flag issue-flag--left'}).find('a').text

    result = requests.get(d['url'])
    next_src = result.content
    next_soup = BeautifulSoup(next_src, 'lxml')
    
    all_text = ""
    for y in next_soup.find_all('div',{'class':'page-content__content editor'}):
        for p in y.find_all('p'):
            all_text += p.text
    d['text'] = all_text

    docs.append(d)

print(docs)

# Getting photo content

#card_url = "https://www.shellvoide.com/media/images/common/3905478824.jpeg"
# with open("/home/user/test/" + "3905478824.jpeg", 'wb') as fobj:
#     fobj.write(requests.get(card_url).content)
