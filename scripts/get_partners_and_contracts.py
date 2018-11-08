import json
import sys
#if sys.version_info > (2, 7):
#    import simplejson as json
#else:
#    import json
from urllib2 import urlopen # works ok with 2.7.9 on rasp
#from urllib.request import urlopen ## works ok with 

import datetime
import time
from plyer import notification

import re

import urllib2


# Init
socis = '0'
socis_new = '0'
contractes = '0'
contractes_new='0'
url_api_stats = "https://api.somenergia.coop/stats/"

# notify constants
app_name = 'Som Notify'
icon_notify = 'icon.ico'

# main config
sleep_time = 300

# blog scrap config
URLBASE_BLOG = 'https://blog.somenergia.coop/'


def doNotify(msgtext, msgtitle):
    notification.notify(
        title = msgtitle,
        message = msgtext,
        app_name = app_name,
        app_icon = icon_notify
)

def callApi(op):
	url = url_api_stats + op
	response = urlopen(url)
	data = response.read()
	j = json.loads(data.decode('utf-8'))
	ret = str(j['data'][op]);
	return  ret
	
def getSocis():
	return callApi("socis")

def getContractes():
	return callApi("contractes")

def socisHandler():
	global socis
	global socis_new
	try:
		socis_new = getSocis()
	except Exception:
		print ("Oops. Some error retrieving data... (connection down?) I'll try again in the next minutes.")
	if (socis < socis_new):
		now = datetime.datetime.now()
		fecha =  str(now.year) +"-"+ str(now.month) +"-"+ str(now.day) +" "+str(now.hour)+":"+str(now.minute);
		socis_add = int(socis_new) - int(socis)
		socis = socis_new
		text = "SOCI;"+fecha+";"+socis +";"+str(socis_add)+";"
		print (text)
		doNotify("Socis nous: +"+str(socis_add)+ " Socis total: "+socis, 'Nou soci!')
		time.sleep(5)


def contractesHandler():
	global contractes
	global contractes_new
	try:
		contractes_new = getContractes()
	except Exception:
		print ("Oops. Some error retrieving data... (connection down?) I'll try again in the next minutes.")
	if (contractes < contractes_new):
		now = datetime.datetime.now()
		fecha =  str(now.year) +"-"+ str(now.month) +"-"+ str(now.day) +" "+str(now.hour)+":"+str(now.minute);
		contractes_add = int(contractes_new) - int(contractes)
		contractes = contractes_new
		text = "CONTRACTES;"+fecha+";"+contractes +";"+str(contractes_add)+";"
		print (text)
		doNotify("Contractes nous: +"+str(contractes_add)+ " Contractes total: "+contractes, 'Nou contracte!')		

def blogNewsHandler():
        print ("Checking posts...")
        now = datetime.datetime.now()
        url = URLBASE_BLOG + str(now.year) + "/"+str(now.month)+"/"+str(now.day)
        opener = urllib2.build_opener()
        opener.addheaders = [('User-agent', 'Mozilla/5.0')]
        response = opener.open(url)
        html_contents = response.read()
        print (html_contents)

        import BeautifulSoup
        print ("Now we put in a soup")
        soup = BeautifulSoup.BeautifulSoup(html_contents)

        print("Cercant bloque...")
        bar = soup.find('div', attrs={'class': 'entry'})
        print(bar.text)
 
        print ("Printing bnoque")
       

while True:

    socisHandler()
    contractesHandler()
    blogNewsHandler()   
    time.sleep(sleep_time)


# contractes
#url = "https://api.somenergia.coop/stats/contractes"
#response = urlopen(url)
#data = response.read()
#encoding = response.info().get_content_charset('utf-8')
#j = json.loads(data.decode(encoding))
#contractes = str(j['data']['contractes']);

# datetime






