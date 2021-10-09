import requests # type: ignore
from bs4 import BeautifulSoup # type: ignore

def get_html(pg):
    url='https://codeforces.com/contests/page/'+str(pg)
    page=requests.get(url)
    #BeautifulSoup expects a string input
    soup=BeautifulSoup(page.text,'html.parser')
    return soup

def get_structure(soup) :
    outpt=soup.find('tr',{'data-contestid' : True })
    print(outpt.prettify())

def get_dates(soup) : 
    items =soup.find_all('tr',{'data-contestid':True})
    dates=[]
    for i in items:
        date=i.find('span').text
        if(len(date)>1) :
            dates.append(date)
    return dates