import requests
import yaml
import logging
from logging.handlers import RotatingFileHandler
import basicFunctions.logfille as lg


#configurations to read main configurations
with open("configuration.yml", "r") as ymlfile:
    cfg = yaml.load(ymlfile)

#reading instance id   
instanceid=cfg["instanceName"]    


def mailNotFOundMsgToAdmin(name,email):
    lg.finalLog()
    url = "https://api.chat-api.com/"+ str(instanceid) +"/sendMessage?token=bfllgpii7xqb42zq"
    
    payload="{\r\n  \"body\": \"*Alert* \\n\\n  Hi Dipesh.... \xF0\x9F\x98\x83  \\n\\n No email found for " + str(name) +" given email is " + str(email) + "  \\n \xF0\x9F\x98\x83 \xF0\x9F\x98\x83 \",\r\n  \"phone\": " +str("918284990439") +"\r\n}"
    headers = {
      'Content-Type': 'application/json'
    }
    
    response = requests.request("GET", url, headers=headers, data=payload)
    logging.info(response.text)
    
    return




def alternativePlatform(name,otherPlatform):
    lg.finalLog()
    url = "https://api.chat-api.com/"+ str(instanceid) +"/sendMessage?token=bfllgpii7xqb42zq"
    
    payload="{\r\n  \"body\": \"*Alert* \\n\\n  Hi Dipesh.... \xF0\x9F\x98\x83  \\n\\n alternativr platform  found for " + str(name) +" given platform is " + str(otherPlatform) + "  \\n \xF0\x9F\x98\x83 \xF0\x9F\x98\x83 \",\r\n  \"phone\": " +str("918284990439") +"\r\n}"
    headers = {
      'Content-Type': 'application/json'
    }
    
    response = requests.request("GET", url, headers=headers, data=payload)
    logging.info(response.text)
