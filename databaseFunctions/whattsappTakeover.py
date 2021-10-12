import requests
import time
import json
import yaml
import logging
from logging.handlers import RotatingFileHandler
import basicFunctions.logfille as lg



def whattsappTakeover():
    lg.finalLog()



    #configurations need to read from configurations.yaml file
    with open("configuration.yml", "r") as ymlfile:
        cfg = yaml.load(ymlfile)

    #reading instance id   
    instanceid=cfg["instanceName"]

    url = "https://api.chat-api.com/"+ str(instanceid)+ "/takeover?token=bfllgpii7xqb42zq"

    payload={}
    headers = {}

    response = requests.request("GET", url, headers=headers, data=payload)

    if str(json.loads(response.text)['result'])=='Takeover request sent to WhatsApp':
        logging.CRITICAL("Instance takingover taking place , will take around 4-5 seconds")
        time.sleep(5)
    
    logging.info("Whattsapp instance is activated")

    return 



    