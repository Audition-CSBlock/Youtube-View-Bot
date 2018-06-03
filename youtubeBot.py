import random, time, requests
from selenium import webdriver
from bs4 import BeautifulSoup

USER_AGENTS_FILE = './user_agents.txt'
RUNNING = True

def LoadUserAgents(uafile=USER_AGENTS_FILE):
    uas = []
    with open(uafile, 'rb') as uaf:
        for ua in uaf.readlines():
            if ua:
                uas.append(ua.strip()[1:-1-1])
    random.shuffle(uas)
    return uas

uas = LoadUserAgents()

while RUNNING == True:
    ip = []
    port = []
    
    response = requests.get('https://www.sslproxies.org')
    soup = BeautifulSoup(response.content, "html.parser")
    
    rows = soup.findAll("tr")

    for row in rows:
        if(len(row.findAll("td")) == 8):
            ip.append(row.contents[0].contents[0])
    for row in rows:
        if(len(row.findAll("td")) == 8):
            port.append(row.contents[1].contents[0])

    random.shuffle(ip)

    profile = webdriver.FirefoxProfile()
    profile.set_preference('general.useragent.override', random.choice(uas))
    profile.set_preference("network.proxy.type", 1)
    profile.set_preference("network.proxy.http", "ip")
    profile.set_preference("network.proxy.http_port", "port")
    driver = webdriver.Firefox(firefox_profile=profile)
    driver.get('https://www.ipchicken.com/')
    raw_input('Press enter to continue')
    driver.quit()