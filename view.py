import os

os.system("pip install requests")

import requests

ngurl=requests.get("http://localhost:4040/api/tunnels").text

data=str(""""""+ngurl+"""""")

ul=data.find('"public_url":"http')
ur=data.find('.ngrok.io","proto"')
print(data[ul+14:ur]+".ngrok.io")
