import datetime

from bs4 import BeautifulSoup
from urllib.request import Request, urlopen
import os
from lxml import etree
import re

days = ["Mon", "Tue", "Wed", "Thu", "Fri", "Sat", "Sun"]

site = "http://www.lib.berkeley.edu/hours/calendar?day=" + datetime.date.today().__str__() + "&library_id=179"
hdr = {'User-Agent': 'Mozilla/5.0'}
req = Request(site,headers=hdr)
page = urlopen(req)
soup = BeautifulSoup(page, features="lxml")

now = datetime.datetime.today().weekday()

num = (now + 1) % 7
num = str(num)
val = "body-row-4-cell-" + num
now = days[now]
curr_div = soup.find("table", {"class": "cal"})
s = curr_div.__str__()

target = datetime.date.today().__str__()[8:]
if target[0] == "0":
	target = target[1]

offset = len("<h1 class=\"calendar_numeral\">")

while s:
	times_start = s.index("<tr class=\"descriptions\">")
	x1 = s.index("<h1 class=\"calendar_numeral\">")
	found = False
	curr_count = 0
	while x1 < times_start:
		x2 = s.index("</h1>", x1)
		day = s[x1 + offset : x2]
		if target == day:
			found = True
			break
		x1 = s.index("<h1 class=\"calendar_numeral\">", x2 + 5)
		curr_count += 1
	
	if not found:
		s = s[x1:]
	else:
		x3 = s.index("<h6>")
		while curr_count > 0:
			x3 = s.index("<h6>", x3 + 4)
			curr_count -= 1
		m = s[x3:]
		start_slice = len("<h6>\n\n") 
		end_slice = m.index("\n", 6)
		result = m[start_slice : end_slice]
		os.system("say \"" + result.replace("-", " to ").replace("am", "a.m.") + "\"")
		break
		