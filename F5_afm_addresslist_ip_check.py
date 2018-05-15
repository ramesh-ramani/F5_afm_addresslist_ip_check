import f5
from f5.bigip import ManagementRoot
import certifi
import urllib3
import requests
import urllib
import json
import ssl
import re

context = ssl._create_unverified_context()
serviceurl = 'https://10.50.0.240/mgmt/tm/security/firewall/address-list'

#from requests.packages.urllib3.exceptions import iInsecureRequestWarning

#requests.packages.urllib3.disable_warnings(InsecureRequestWarning)


lst=list()

url = serviceurl

uh=urllib.urlopen(url,context=context)
data=uh.read()
js = json.loads(str(data))

##This will check for a particular name of Address list and print out all the addresses in thatAddress List##
for i in js["items"]:
     if "Allow-Access-to-STG-Pools" not in i["name"]: continue
     else:
         for i in i["addresses"]:
             print i["name"]
