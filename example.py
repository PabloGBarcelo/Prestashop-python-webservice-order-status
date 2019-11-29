#!/usr/bin/python3
# Python 3.7
# Prestashop 1.6.x (not tested >1.6)

# Libraries
import requests, mysql.connector
import xml.etree.ElementTree as ET
from requests.auth import HTTPBasicAuth

# Activate webservice (Advance Parameters/Webservice) and create apikey
protocol = 'https:// OR http://'
apiKey = 'InsertYourApiKeyHere'
apiHost = 'YOURDOMAIN.COM/api/orders/'
stateSent = '4' # New status to set automatically
config = {
    'host':'Yourdomain.com',
    'user':'Userdatabase',
    'password':'passwordDatabase',
    'database':'nameDatabase',
    'raise_on_warnings': True
}

while 1: # Optional while order.upper()!= 'Q': to exit
    order = input('Insert order to update:')
    try:
        # With id_order try to call Webservice Prestashop
        order = requests.get(protocol+apiKey+'@'+apiHost+order, auth=HTTPBasicAuth(apiKey,''))
        orderXML = ET.fromstring(order.content)
        # Modify status order
        elm = orderXML.find(".//current_state")
        elm.text=stateSent
        orderXMLModified = ET.tostring(orderXML)
        # Insert new data in Prestashop
        resultModification = requests.put(protocol+apiKey+'@'+apiHost+result, data=orderXMLModified, auth=HTTPBasicAuth(apiKey,''))

    except mysql.connector.Error as err:
        if err.errno == errorcode.ER_ACCESS_DENIED_ERROR:
            print("Something is wrong with your user name or password")
        elif err.errno == errorcode.ER_BAD_DB_ERROR:
            print("Database does not exist")
        else:
            print(err)