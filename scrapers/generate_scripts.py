import os
import sys

path = sys.argv[1]
if path[-1] != "/":
	path = path + "/"

locs = ['moffitt', 'main_stacks', 'anthro', 'art_history', 'VLSB', 'doe', 'business', 'chemistry', 
'asian', 'engineering', 'optometry', 'music', 'morrison', 'math', 'physics', "rsf", "stadium_gym"]

for loc in locs:
	f = open(loc + ".scpt", "w")
	f.write("tell application \"Terminal\"\n")
	f.write("if (exists window 1) and not busy of window 1 then\n")

	if loc == "rsf":
		f.write("do script (\"%s %s\") in window 1\n" % ("python3", path + "scrapers/rsf.py"))
	elif loc == "stadium_gym":
		f.write("do script (\"%s %s\") in window 1\n" % ("python3", path + "scrapers/stadium_gym.py"))
	else:
		f.write("do script (\"%s %s %s\") in window 1\n" % ("python3", path + "scrapers/lib.py", loc))

	f.write("else\n")

	if loc == "rsf":
		f.write("do script (\"%s %s\")\n" % ("python3", path + "scrapers/rsf.py"))
	elif loc == "stadium_gym":
		f.write("do script (\"%s %s\")\n" % ("python3", path + "scrapers/stadium_gym.py"))
	else:
		f.write("do script (\"%s %s %s\")\n" % ("python3", path + "scrapers/lib.py", loc))
	
	f.write("end if\n")
	f.write("activate\n")
	f.write("end tell")

try:
	os.system("cd .. && mkdir scripts")
except Exception:
	pass

files = os.listdir()
files = [e for e in files if ".scpt" in e]
for scpt in files:
	os.system("mv %s %s%s" % (scpt, "../scripts/", scpt))
