import json
import sys
import datetime
import time
from plyer import notification
import requests
import re
import logging

# Init
socis = '0'
socis_new = '0'
contractes = '0'
contractes_new='0'

# notify constants
app_name = 'Som Notify'
icon_notify = 'somenergia_icon_K2f_icon.ico'

# main config
SLEEP_TIME = 300

# blog scrap config
URLBASE_BLOG = 'https://blog.somenergia.coop/'

# API OPERATIONS
OP_CONTRACTS = "contractes"
OP_PARTNERS  = "socis"
JSON_DATA_FIELD   = "data"
URL_API_STATS = "https://api.somenergia.coop/stats/"


def doNotify(msgtext, msgtitle):
    notification.notify(
        title = msgtitle,
        message = msgtext,
        app_name = app_name,
        app_icon = icon_notify
)

# makes the url and retorn data value, depending operation
def callApi(op):
	url = URL_API_STATS + op
	response = requests.get(url)
	j = response.json()
	ret = str(j[JSON_DATA_FIELD][op]);
	return  ret
	
def getSocis():
	return callApi(OP_PARTNERS)

def getContractes():
	return callApi(OP_CONTRACTS)

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
        opener = urllib.build_opener()
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
	# main. keep pulling 
	
    socisHandler()
    contractesHandler()
   #blogNewsHandler()   
    time.sleep(SLEEP_TIME)







