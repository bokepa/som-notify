import json
from urllib2 import urlopen
import datetime
import time



# Init
socis = '0'
contractes = '0'
url_socis = "https://api.somenergia.coop/stats/socis"


def getSocis():
	url = "https://api.somenergia.coop/stats/socis"
	response = urlopen(url)
	data = response.read()
	j = json.loads(data)
	ret = str(j['data']['socis']);
	return ret

def getContractes():
	url = "https://api.somenergia.coop/stats/contractes"
	response = urlopen(url)
	data = response.read()
	j = json.loads(data)
	ret = str(j['data']['contractes']);
	return ret

while True:
	# socis
	
	socis_new = getSocis()
	contractes_new = getContractes()
	
	if (socis < socis_new or contractes < contractes_new):
		now = datetime.datetime.now()
		fecha =  str(now.year) +"-"+ str(now.month) +"-"+ str(now.day) +" "+str(now.hour)+":"+str(now.minute);
		socis = socis_new
		contractes = contractes_new
		print (fecha+";"+socis +";"+contractes_new)

	# come back in a minute!
	time.sleep(60)


# contractes
#url = "https://api.somenergia.coop/stats/contractes"
#response = urlopen(url)
#data = response.read()
#encoding = response.info().get_content_charset('utf-8')
#j = json.loads(data.decode(encoding))
#contractes = str(j['data']['contractes']);

# datetime






