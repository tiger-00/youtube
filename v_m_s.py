import mechanicalsoup
import time
import requests
from mechanize import Browser
browser = mechanicalsoup.Browser()
import random
print('snapchat:ar5824')
print('''
     d8888b.  .d88b.   .d88b.  d888888b        .88b  d88.  .d88b.  db    db d8b   db d888888b d8888b. 
     88  `8D .8P  Y8. .8P  Y8. `~~88~~'        88'YbdP`88 .8P  Y8. 88    88 888o  88   `88'   88  `8D 
     88oobY' 88    88 88    88    88           88  88  88 88    88 88    88 88V8o 88    88    88oobY' 
     88`8b   88    88 88    88    88    C8888D 88  88  88 88    88 88    88 88 V8o88    88    88`8b   
     88 `88. `8b  d8' `8b  d8'    88           88  88  88 `8b  d8' 88b  d88 88  V888   .88.   88 `88. 
     88   YD  `Y88P'   `Y88P'     YP           YP  YP  YP  `Y88P'  ~Y8888P' VP   V8P Y888888P 88   YD 
    ''')
print('for subscription enter(1) for more views (2)')
num = input("enter your choice:")
if num == '1':
    url = input("enter url your channel:")
    num1 = '?sub_confirmation=1'
    print(url + num1)
elif num == '2':
    ir = input("put utl the video")
    thradd = int(input("how many views you want ? :"))
    br = Browser()
    br.set_handle_robots(False)

    br.addheaders = [('User-agent', 'Firefox')]
    for i in range(thradd):
        re = time.sleep(1)
        r = requests.get(ir)
        time.sleep(1)
        eo = requests.post(ir)
        if eo == requests.ConnectionError:
            print('error in your Connection')
            break
        else:
            print('some thing wrong..')
        br.set_handle_refresh(mechanize._http.HTTPRefreshProcessor(), max_time=1)
        e = br.open(ir)
        e4 = browser.get(ir)
        print("one view complete")