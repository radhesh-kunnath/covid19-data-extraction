import requests
import pymysql
import schedule
import time
from bs4 import BeautifulSoup

def mycode():
    #dbcon=pymysql.connect(host='localhost',user='root',passwd='',db='scrap')
    #cursor=dbcon.cursor()
    #print("database connected")

    URL = "http://covid19.karnataka.gov.in/covid-dashboard/dashboard.html"
    page = requests.get(URL)


    soup = BeautifulSoup(page.content, "html.parser")
    print(soup.prettify())
    #results = soup.find_all('table',class_="table table-sm table-striped table-hover table-bordered sortable")
    #print(results)
    #content = results.find_all('td')
    #print(content)


mycode()


"""
schedule.every(5).seconds.do(mycode)

while(1):
    schedule.run_pending()
    print("wait")
    time.sleep(1)
"""