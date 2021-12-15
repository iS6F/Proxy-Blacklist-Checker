import requests, os
from bs4 import BeautifulSoup
path = os.path.normpath(os.getcwd())
ipf = open(f'{path}\\config\\ips.txt', 'r')
ips = ipf.read().splitlines()
cw = '\33[37m'
cp = '\33[35m'
cg = '\33[32m'
cr = '\33[31m'
os.system('cls')
for ipport in ips:
    ipportlist = ipport.split(':')
    ip = ipportlist[0]
    os.system(f'title [ {ip} ]')
    pl = {'ip': ip, 'action': 'blacklist-check'}
    t = requests.post('https://www.xmyip.com/include/blacklisted.php', data=pl)
    soup = BeautifulSoup(t.content, 'lxml')
    ul = soup.find('ul', class_="vert")
    ulList = ul.text.split()
    nl = 0
    for word in ulList:
        if word == 'Not':
            nl += 1
    if nl < 50:
        print(f'{cw}[{cp}{ip}{cw}] {cw}[{cr}Blacklisted{cw}]')
        with open(f'{path}\\config\\blacklisted.txt', 'a') as bl:
            bl.write(f'{ipport}\n')
    elif nl >= 50:
        print(f'{cw}[{cp}{ip}{cw}] {cw}[{cg}Whitelisted{cw}]')
        with open(f'{path}\\config\\whitelisted.txt', 'a') as wl:
            wl.write(f'{ipport}\n')        
input(f'{cw}[{cp}Done{cw}]')