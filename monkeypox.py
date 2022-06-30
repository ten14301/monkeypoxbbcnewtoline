import requests
import re
from bs4 import BeautifulSoup

request = requests.get('https://www.bbc.co.uk/search?q=monkeypox&page=1')
html = request.content
sup = BeautifulSoup(html, 'html.parser')
Linetoken = "Line-token"


def LineNotifyMessage(message):
    payload = {'message':message}
    return LineNotify(payload)
def LineNotify(payload,file=None):
    url = 'https://notify-api.line.me/api/notify'
    token = Linetoken
    headers = {'Authorization':'Bearer ' + token}
    return requests.post(url, headers=headers , data = payload, files=file)

def monkeypoxcheck():
    head = sup.findAll('div',{'class' : 'ssrcss-1f3bvyz-Stack'})
    
    for div in head:
      links = div.findAll('a')
      for a in links:
         LineNotifyMessage("ข่าวล่าสุดเรื่องฝีดาษลิง จาก BBC NEWS UK\n\n" + a.get_text() + "\nอ่านรายละเอียดเพิ่มเติมได้ที่ " + a['href'] + "\n")
            

 
        
monkeypoxcheck()
