import requests # type: ignore
from bs4 import BeautifulSoup # type: ignore
import os 
import sys
import webbrowser

def get_html(pg=1):
    url='https://codeforces.com/contests/page/'+str(pg)
    page=requests.get(url)
    #BeautifulSoup expects a string input
    soup=BeautifulSoup(page.text,'html.parser')
    return soup

def get_structure(soup) :
    outpt=soup.find('tr',{'data-contestid' : True })
    print(outpt.prettify())

def get_dates(soup) : 
    dates=[]
    wrapper=soup.find('div',class_='datatable')
    items =wrapper.find_all('tr',{'data-contestid':True})
    for i in items : 
        date=i.td.text
        dates.append(str(date))
    return dates

def get_date(soup) :
    coming=soup.find('tbody')
    fst=coming.find('tr',{'data-contestid':True})
    date=fst.find('span').text
    return date

def get_name(soup) : 
    wrapper= soup.find('tr',{'data-contestid':True})
    name=wrapper.td.text
    return name

def reg_link(soup,) : 
    first = soup.find('tr',{'data-contestid':True})
    link=first.find('a',class_='red-link').get('href')
    url='https://codeforces.com'+str(link)
    return url

def get_authors(soup) :
    wrapper=soup.find('tr',{'data-contestid': True}).td
    outr=wrapper.find_next_sibling()
    items=outr.find_all('a')
    names=[]
    for i in items :
        name=(i.text)
        names.append(name)
    return names

def get_contest_code(contest_tree) : 
    num=contest_tree.get('data-contestid')
    return int(num)

soup=get_html()
