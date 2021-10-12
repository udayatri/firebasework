import requests
import os
import smtplib
import imghdr
import json
from email.message import EmailMessage
import yaml


  

#ncomplete message needes to be completed
def schedulingLinkForwarding(name,number):

    with open("configuration.yml", "r") as ymlfile:
        cfgMain = yaml.load(ymlfile)  

    #mainsheet name
    link=cfgMain["link"] 

    #reading instance id   
    instanceid=cfgMain["instanceName"]  


    url = "https://api.chat-api.com/"+ str(instanceid) +"/sendLink?token=bfllgpii7xqb42zq"

    payload="{\r\n  \"body\": \"Hi " + str(name.title()) + "\\nCan you Please  use the below link to schedule your session \xF0\x9F\x98\x83 . \\n\\n  https://" + str(link) +".herokuapp.com/template \",\r\n  \"phone\": \"" +str(number) + "\"\r\n}"
    headers = {
            'Content-Type': 'application/json'
            }

    response = requests.request("POST", url, headers=headers, data=payload)

    #print(response.text)
    return





