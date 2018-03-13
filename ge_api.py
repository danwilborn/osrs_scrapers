from urllib2 import Request, urlopen, URLError
import re
from tabulate import tabulate
import sys
import json

item_id = sys.argv[1]

url = 'http://services.runescape.com/m=itemdb_oldschool/api/catalogue/detail.json?item='+item_id

r = Request(url)

try:
	response = urlopen(r)
	data = response.read()
	#print(hiscores)
except URLError as e:
	print("Something something error:", e)

data = json.loads(data)
#print(data)

output = dict()
output['name'] = data['item']['name']
output['price'] = data['item']['current']['price']
output['today'] = data['item']['today']['price']
output['30 days'] = data['item']['day30']['change']
output['90 days'] = data['item']['day90']['change']
output['180 days'] = data['item']['day180']['change']

print("name: "+str(output['name']))
print("price: "+str(output['price']))
print("today: "+str(output['today']))
print("30 days: "+str(output['30 days']))
print("90 days: "+str(output['90 days']))
print("180 days: "+str(output['180 days']))


