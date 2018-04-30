from lxml import html
import requests
from bs4 import BeautifulSoup
import re

def filter_dig(text):
    if "." in text:
        return re.findall(r'(\d+\.\d+)', text)
    else:
        return re.findall(r'(\d+\,\d+)', text)
def filter_str(text):
    return re.findall(r'\D+', text)

def scratch_page(url,class_name):
    response = requests.get(url)
    soup = BeautifulSoup(response.text, 'lxml')
    return soup.find('div', attrs={'class': class_name})

# dig = filter_dig(f.find("td").text)
# str = filter_str(f.find("td").text)
# try:
#     print('Price: '+dig[0]+' Currency: '+str[0])
# except:
#     print('Hello')

# tree = html.fromstring(page.content)
# price = tree.xpath('//div[@title="intraday__close"]/text()')
# print (price)


