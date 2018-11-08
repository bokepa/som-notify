import json
#from urllib2 import urlopen
from urllib.request import urlopen
import datetime
import time
from plyer import notification


# Init
socis = '0'
socis_new = '0'
contractes = '0'
contractes_new='0'
url_socis = "https://api.somenergia.coop/stats/socis"
sleep_time = 300

def doNotify(text):

    notification.notify(
        title='Nou soci!',
        message=text,
        app_name='Som Notify',
        app_icon='icon.ico'
)

def getSocis():
	url = "https://api.somenergia.coop/stats/socis"
	
	response = urlopen(url)
	data = response.read()
	j = json.loads(data.decode('utf-8'))
	#j = json.loads(data)
	ret = str(j['data']['socis']);
	return ret

def getContractes():
	url = "https://api.somenergia.coop/stats/contractes"
	response = urlopen(url)
	data = response.read()
	j = json.loads(data.decode('utf-8'))
	#j = json.loads(data)
	ret = str(j['data']['contractes']);
	return ret

while True:
	# socis
	try:
		socis_new = getSocis()
		contractes_new = getContractes()
	except Exception:
		print ("Oops. Some error retrieving data... (connection down?) I'll try again in the next minutes.")
	
	if (socis < socis_new or contractes < contractes_new):
		now = datetime.datetime.now()
		fecha =  str(now.year) +"-"+ str(now.month) +"-"+ str(now.day) +" "+str(now.hour)+":"+str(now.minute);
		socis_add = int(socis_new) - int(socis)
		contractes_add = int(contractes_new) - int(contractes)
		socis = socis_new
		contractes = contractes_new
		text = fecha+";"+socis +";"+contractes+";"+str(socis_add)+";"+str(contractes_add)
		print (text)
		doNotify("Socis: +"+str(socis_add)+ " Contractes: +"+str(contractes_add))
	# come back in a minute!
	time.sleep(sleep_time)


# contractes
#url = "https://api.somenergia.coop/stats/contractes"
#response = urlopen(url)
#data = response.read()
#encoding = response.info().get_content_charset('utf-8')
#j = json.loads(data.decode(encoding))
#contractes = str(j['data']['contractes']);

# datetime






