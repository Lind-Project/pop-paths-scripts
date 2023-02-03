import os, sys, wget
import json, requests
from selenium import webdriver
from bs4 import BeautifulSoup

from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.desired_capabilities import DesiredCapabilities

#kern = sys.argv[1]
#url = "https://www.linuxkernelcves.com/steams/{}".format(kern)

url = "https://www.linuxkernelcves.com/streams/5.15"
options = webdriver.ChromeOptions()
options.add_argument('--headless')
driver = webdriver.Remote("http://127.0.0.1:4444/wd/hub", DesiredCapabilities.CHROME)
#driver = webdriver.Chrome(executable_path='/home/lind/lind_project/lind/pop-paths-scripts/pop_paths_scripts/chromedriver_linux64/chromedriver')
driver.get(url)

#wait = WebDriverWait(driver, 10)
#wait.until(EC.presence_of_element_located((By.CLASS_NAME, "cve-card v-card v-sheet theme--light")))
html = driver.page_source
soup = BeautifulSoup(html, "html.parser")
cards = soup.find_all("div", class_="cve-card v-card v-sheet theme--light")

#place items into dictionary in tuples of the form:; {cve_date, kern_hash}, cve_date = key
dict = {}
for card in cards:
    cve_date = card.find("span",class_="headline").text.strip()
    kern_hash = card.find("span",class_="mono").text.strip()
    blurb = card.find("p").text.strip()
    dict[cve_date] = kern_hash
with open("cve_dict.json", "w") as f:
    json.dump(dict, f)

#loop through dict and use kern_hash's to scrape through diff pages and download
#kern = "5.15"
for date, hash_num in dict.items():
    ids = hash_num
    if ids == "":
        continue
    cve_date = date
    url_diff = 'https://git.kernel.org/pub/scm/linux/kernel/git/torvalds/linux.git/diff/?id={}'.format(ids)
    dirs = r'\Users\jkoer\Desktop\Cooper\lind_cont\diff-{kern}'.format(kern)
    if not os.path.exists(dirs):
        os.makedirs(dirs)
    filepath = r'{dir}\{cve_date}.txt'.format(cve_date)
    wget.download(url_diff, filepath) 
