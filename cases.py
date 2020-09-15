import requests
import pymysql
import schedule
import time
from bs4 import BeautifulSoup

def mycode():
    dbcon=pymysql.connect(host='localhost',user='root',passwd='',db='scrap')
    cursor=dbcon.cursor()
    print("database connected")

    URL = "https://www.mygov.in/covid-19"
    page = requests.get(URL)


    soup = BeautifulSoup(page.content, "html.parser")
    results = soup.find("table",id="state-covid-data")
    content = results.find_all('td')
    total = []
    states = []
    active_cases = []
    discharged_cases = []
    total_deaths = []
    total_confirmed_cases=[]
    i = 1
    for entries in content:
        total.append(entries.text.strip())
    print(total)
    for i in range(len(total)):
        if(i%5==0):
            states.append(total[i])
        elif(i%5==2):
            active_cases.append(total[i])
        elif(i%5==3):
            discharged_cases.append(total[i])
        elif(i%5==4):
            total_deaths.append(total[i])
        elif(i%5==1):
            total_confirmed_cases.append(total[i])
    for i in range(len(states)):
        total_confirmed_cases[i]=total_confirmed_cases[i].replace(',','')
        active_cases[i]=active_cases[i].replace(',','')
        discharged_cases[i]=discharged_cases[i].replace(',','')
        total_deaths[i]=total_deaths[i].replace(',','')
    for i in range(len(states)):
        print(states[i],active_cases[i],discharged_cases[i],total_deaths[i],total_confirmed_cases[i])
        #query="insert into statesdata values('"+states[i]+"','"+active_cases[i]+"','"+discharged_cases[i]+"','"+total_deaths[i]+"','"+total_confirmed_cases[i]+"');"
        #query="update statesdata set active_cases='"+active_cases[i]+"',discharged_cases='"+discharged_cases[i]+"',total_deaths='"+total_deaths[i]+"',total_confirmed_cases='"+total_confirmed_cases[i]+"' where states='"+states[i]+"';";
        query="update statesdata set active_cases="+active_cases[i]+",discharged_cases="+discharged_cases[i]+",total_deaths="+total_deaths[i]+",total_confirmed_cases="+total_confirmed_cases[i]+" where states='"+states[i]+"';";
        cursor.execute(query)
        dbcon.commit()
    print("updated")

schedule.every(5).seconds.do(mycode)

while(1):
    schedule.run_pending()
    print("wait")
    time.sleep(1)