#!/usr/bin/python3

import scrap_stock
import email_sender
from time import sleep
from dump_data import User
import json
import jsonpickle
from bs4 import BeautifulSoup
import requests

message=''

with open('data/user_data.json', 'w') as output:
    user1 = User('forsimi@gmail.com', 86400)
    user1_json = jsonpickle.encode(user1)
    json.dump(user1_json, output)

with open('data/user_data.json', 'r') as input:
    user_py=jsonpickle.decode(json.load(input))

try:
    while True:

        for x in user_py.stock:
            # url='https://www.marketwatch.com/investing/stock/'+x
            # response = requests.get(url)
            # soup = BeautifulSoup(response.text, 'lxml')
            # f = soup.find('div',attrs={'class': 'intraday__data'}).find('sup').get_text()

            f=scrap_stock.scratch_page('https://www.marketwatch.com/investing/stock/'+x,'intraday__close')
            dig = scrap_stock.filter_dig(f.find('td').get_text())
            str = scrap_stock.filter_str(f.find('td').get_text())

            if str:
                message+='Stock: '+x.upper()+' Price: '+dig[0]+' Currency: '+str[0]+'\n'
            else:
                message += 'Stock: '+x.upper()+' Price: '+dig[0]+' Currency: '+'\n'

        email_sender.send_email('cherrywidget@gmail.com','simi821219',user_py.email,'proba email kuldes',message+'Your next email in: 86400 sec')
        # f.clear()
        # str.clear()
        print('Email is sent...')
        sleep(user_py.interval)
except (KeyboardInterrupt):
        print('Stopping...')