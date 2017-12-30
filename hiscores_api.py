from urllib2 import Request, urlopen, URLError
import re
from tabulate import tabulate

url = 'http://services.runescape.com/m=hiscore_oldschool/index_lite.ws?player=Irish Dawg'

r = Request(url)

try:
	response = urlopen(r)
	hiscores = response.read()
	#print(hiscores)
except URLError as e:
	print("Something something error:", e)

hs_split = re.split(',|\n', hiscores)
#print(hs_split)

skills= dict()
skill_list = [line.rstrip('\n') for line in open('skill_order.txt')]

#print(skill_list)


count = 1
skill_count = 0
temp_list = list()

for val in hs_split:
	if val != '-1' and val != '':
		temp_list.append(val)
		if count == 3:
			count = 0 # reset counter
			skill = skill_list[skill_count]
			skills[skill] = temp_list
			temp_list = []
			skill_count += 1 		
		count += 1
				
#print(skills)

print tabulate(skills, headers=["Skill", "Rank", "Level", "Experience"])

'''
print("Skill \t\t"+"Rank \t\t"+"Level \t\t"+"Experience")
print("-----------------------------------------------------------")
for skill in skills:
	print(skill)
'''	
