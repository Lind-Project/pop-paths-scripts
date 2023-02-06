import sys, getopt, os
import wget
import json, requests
from selenium import webdriver
from bs4 import BeautifulSoup
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

#uncomment these two lines to insert any kernel version from command line or just change url manually
#kern = sys.argv[1]
#url = f"https://www.linuxkernelcves.com/steams/{kern}"
url = "https://www.linuxkernelcves.com/streams/5.15"

options = webdriver.ChromeOptions()
options.add_argument('--headless')
driver = webdriver.Chrome()
driver.get(url)

html = driver.page_source
soup = BeautifulSoup(html, "html.parser")

cards = soup.find_all("div", class_="cve-card v-card v-sheet theme--light")

dict = {}
for card in cards:
    cve_date = card.find("span",class_="headline").text.strip()
    kern_hash = card.find("span",class_="mono").text.strip()
    blurb = card.find("p").text.strip()
    dict[cve_date] = (kern_hash, blurb)
with open("cve_dict.json", "w") as f:
    json.dump(dict, f)

for date, hash_num in dict.items():
    ids = hash_num[0]
    if ids == "":
        continue
    cve_date = date
    url2 = f"https://git.kernel.org/pub/scm/linux/kernel/git/torvalds/linux.git/patch/?id={ids}"
    #before running, set dir to the directory path you want to scrape all the diffs into
    #dir = 
    if not os.path.exists(dir):
        os.makedirs(dir)
    filepath = fr'{dir}\{cve_date}.txt'
    wget.download(url2, filepath) 

