import sys, getopt, os
import wget, time, urllib.request
import json, requests
from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from bs4 import BeautifulSoup

kern = sys.argv[1]
url = fr"https://www.linuxkernelcves.com/streams/[kern]"

options = Options()
options.add_argument('--headless')
driver = webdriver.Chrome(options=options)
driver.get(url)

time.sleep(5)

html = driver.page_source
soup = BeautifulSoup(html, "html.parser")


cards = soup.find_all("div", class_="cve-card v-card v-sheet theme--light")

d = {}
for card in cards:
    cve_date = card.find("span",class_="headline").text.strip()
    kern_hash = card.find("span",class_="mono").text.strip()
    blurb = card.find("p").text.strip()
    d[cve_date] = []
    d[cve_date].append(kern_hash)
    d[cve_date].append(blurb)
with open("cve_dict.json", "w") as f:
    json.dump(d, f)

for date, hash_num in d.items():
    ids = hash_num[0]
    if ids == "":
        continue
    cve_date = date
    url2 = f"https://git.kernel.org/pub/scm/linux/kernel/git/torvalds/linux.git/patch/?id={ids}"
    dir = sys.argv[2]
    if not os.path.exists(dir):
        os.makedirs(dir)
    filename = f'{cve_date}.txt'
    filepath = os.path.join(dir, filename)
    wget.download(url2, filepath)
    with urllib.request.urlopen(url2) as response, open(filepath, 'wb') as out_file:
        data = response.read()
        out_file.write(data)
