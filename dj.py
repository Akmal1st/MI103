import urllib.request as ul
import urllib.parse as up
from bs4 import BeautifulSoup
import re
site = input('sayt manzili: ')
try:
    my_data = {"request":"true","auth_stud_id":"300034845","password":"O9IM-D21-62RE"}
    #site = "http://talaba.tdpu.uz/student/jadval"
    if site=='':
        site = "http://talaba.tdpu.uz/"
    data = up.urlencode(my_data)
    data = data.encode('ascii')
    page = ul.urlopen(site  ,data)
except:
    f = open('talaba.html','rb').read()
    page = f.decode('cp1251')

soup = BeautifulSoup(page, 'lxml')
print(soup.prettify().get_text())
#a = soup.find_all('a')
#h4 = soup.find_all('h4')
#hafta = ['dushanba','seshanba','chorshanba','payshanba','juma','shanba','yakshanba']
#print([x.get_text().split() for x in a if x.get_text()!=None])
#print([x.get_text().split()[0] for x in h4 if x.get_text().split()[0].lower() in hafta])

'''links = [x for x in soup.find_all('a') if x.get('class')!=None and len(x.get('class'))>1 and x.get('class')[1]=='btn-warning' and x.get('target')!=None and x.get('target')=='_blank']
n=0
k=0
bb = soup.find_all('b')
#print(bb)
lst = [str(y.get_text()) for y in bb]
lst2=[]
for y in lst:
    if n>3:
        n=0
        k+=1
    if n==0:
        lst2.append([])
    n+=1
    lst2[k].append(y)
for x in range(len(lst2)):
    print(f"{x+1}{lst2[x][0]}-{lst2[x][1]}\n  {lst2[x][2]}\n {lst2[x][3]}\n{links[x].get('href')}")
    print()
#print(links)
#print(soup.prettify())'''

