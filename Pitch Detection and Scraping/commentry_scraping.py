""" selenium for scraping commentry from espn crick info
make sure you have chromedriver installed(referance:https://tecadmin.net/setup-selenium-chromedriver-on-ubuntu/)"""

from selenium import webdriver
import pandas as pd
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.ui import WebDriverWait
import time
"""PATH of the chrome driver in your device"""
PATH= '/usr/bin/chromedriver'
driver = webdriver.Chrome(PATH)
"""url of the match commentry site"""
url = "https://www.espncricinfo.com/series/8044/commentary/1195573/brisbane-heat-vs-sydney-thunder-big-bash-league-2019-20"

for i in ['1','2']:
    driver.get(url+'?innings='+i)
    comments = pd.DataFrame(columns=['Ball','Score','Bowler','Batsmen','Commentry'])
    for j in range(10)  :
        html = driver.find_element_by_tag_name('html')
        html.send_keys(Keys.END)
        time.sleep(2)
    ids = driver.find_elements_by_class_name('item-wrapper') 
    for x in ids:
        data = x.text
        split_list=data.split()
        se =' '.join(split_list[2:])
        sen = se.split(',')
        tt = (sen[0]).split()
        bat=tt[2]
        bow=tt[0]
        comments.loc[len(comments)] = [split_list[0],split_list[1],bow,bat,' '.join(sen[2:])]
    #saving it in CSV file     
    comments.to_csv('innings '+i+'.cvs',index=False)      
driver.close()
