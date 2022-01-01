import webbot
import requests
from bs4 import BeautifulSoup
import time

food= webbot.Browser()
print(1)
food.go_to('google.com')
YOUR_USERNAME = "" #ex. CoolDabber
YOUR_LEVEL_REQUIREMENT = 18 
while True:
    #print(food.get_current_url())
    
    if 'doordash' in food.get_current_url() or "ubereats" in food.get_current_url() or "grubhub" in food.get_current_url():
        pg = requests.get(f'https://sky.shiiyu.moe/stats/{YOUR_USERNAME}/Kiwi')
        supper = BeautifulSoup(pg.content,'lxml')
        oofs = supper.find_all('div',{'class':'skill-name'})
        farm = [oof for oof in oofs if 'Farming' in oof.get_text()]
        lvl = farm[0].find('span').get_text()
        if int(lvl)>=YOUR_LEVEL_REQUIRMENT:
            pass
        else:
            #food.close_current_tab()
            food.go_to('google.com')
            food.execute_script(f"document.getElementsByTagName('body')[0].innerHTML='FARMER JOE:You only have {lvl} out of {YOUR_LEVEL_REQUIREMENT} farming levels required to eat';")
            
         

