import time

import requests , random
from requests.structures import CaseInsensitiveDict

url = "https://mybsms.gr/ws/send.json"

headers = CaseInsensitiveDict()
headers["Content-Type"] = "application/json"
headers["Accept"] = "application/vnd.api+json"

data = """
{
 "username":"thessalybank",
 "password":"YWhAUx0iqe",
 "senderId":"ethessbank",
 "recipients":["00306988577088"], 
 "message":"message-text",
 "dlr-url":"http://ros.seczero.eu/incomes"
}
"""


resp = requests.post(url, headers=headers, data=data)
print(resp.json())
resp.json()
