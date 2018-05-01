#!/usr/bin/python3

import scrap_stock
import email_sender
from time import sleep

stock='vlkay'
s=7200

try:
    while True:
        f=scrap_stock.scratch_page('https://www.marketwatch.com/investing/stock/'+stock,'intraday__close')
        dig = scrap_stock.filter_dig(f.find("td").text)
        str = scrap_stock.filter_str(f.find("td").text)

        email_sender.send_email('cherrywidget@gmail.com','simi821219','forsimi@gmail.com','proba email kuldes','Stock: '+stock.upper()+' Price: '+dig[0]+' Currency: '+str[0]+' Your next mail in: 360 sec')
        dig.clear()
        str.clear()
        sleep(s)
except (KeyboardInterrupt):
        print('Stopping...')