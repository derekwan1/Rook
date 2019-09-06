import datetime

from bs4 import BeautifulSoup
from urllib.request import Request, urlopen
import os
months = {"01": "Jan", "02": "Feb", "03": "Mar", "04": "Apr", "05": "May", "06": "Jun", \
	"07": "Jul", "08": "Aug", "09": "Sep", "10": "Oct", "11": "Nov", "12": "Dec"}
days = ["Monday", "Tuesday", "Wednesday", "Thursday", "Friday", "Saturday", "Sunday"]

def translate_to_text(s):
	lst = s.split("-")
	month = lst[0]
	day = lst[1]
	if day[0] == "0":
		day = day[1]
	month = months[month]
	return month + " " + day

def tag_text(tag):
	return tag.contents[0]


site= "https://recsports.berkeley.edu/stadium-fitness-center-hours/"
hdr = {'User-Agent': 'Mozilla/5.0'}
req = Request(site,headers=hdr)
page = urlopen(req)
soup = BeautifulSoup(page, features="lxml")

lst = soup.select("tr td")
now = str(datetime.datetime.today())
now = translate_to_text(now[5:10])

k = 0
while k + 1 < len(lst):
	date = lst[k]
	date = tag_text(date)
	if now in date:
		times = lst[k + 1]
		os.system("say \"" + tag_text(times).replace("–", " to ") + "\"")
		break
	k += 2