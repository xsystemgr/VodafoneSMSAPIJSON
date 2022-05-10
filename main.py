import requests
from requests.structures import CaseInsensitiveDict

url = "https://mybsms.gr/ws/send.json"

headers = CaseInsensitiveDict()
headers["Content-Type"] = "application/json"
headers["Accept"] = "application/vnd.api+json"

data = """
{
 "username":"xxxxxxxxxxx",
 "password":"xxxxxxxxxxx",
 "senderId":"hellouser",
 "recipients":["00306988577000"], 
 "message":"message-text",
 "dlr-url":"http://ros.seczero.eu/incomes"
}
"""


resp = requests.post(url, headers=headers, data=data)
print(resp.json())

