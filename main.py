import scrap_stock
import email_sender

stock='vlkay'
f=scrap_stock.scratch_page('https://www.marketwatch.com/investing/stock/'+stock,'intraday__close')
dig = scrap_stock.filter_dig(f.find("td").text)
str = scrap_stock.filter_str(f.find("td").text)
t=str[0].encode('utf-8')
print(t.decode('utf-8'))
email_sender.send_email('cherrywidget@gmail.com','simi821219','forsimi@gmail.com','proba email kuldes','Stock: '+stock.upper()+' Price: '+dig[0]+' Currency: '+t.decode('utf-8'))