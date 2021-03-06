import requests
import yaml
import databaseFunctions.viewData as vwdt
import logging
from logging.handlers import RotatingFileHandler
import basicFunctions.logfille as lg


def sendingMsgToPsychologist(psychologistName,psychologistContact,cName, cContact,email,cProblem,Date, Time):
    with open("configuration.yml", "r") as ymlfile:
        cfgMain = yaml.load(ymlfile)  

    #mainsheet name
    herokuInstance=cfgMain["link"] 

    link="https://"+ str(herokuInstance) +".herokuapp.com/sessioncompletd/" + str(email)

    url = "https://api.chat-api.com/instance294124/sendLink?token=bfllgpii7xqb42zq"

    payload="{\r\n  \"body\": \"Autogenerated Message \xF0\x9F\x98\x83  \\n*Session Alert* \\n\\nName : "+ str(cName)+ " \\nContact : "+ str(cContact) +"  \\n\\nProblem : " + str(cProblem) +"\\n\\nDate : " + str(Date) +" \\nTimings : " + str(Time)+"\\n Link to click on completion "+str(link) + "  \",\r\n  \"phone\": " + str(psychologistContact)+"\r\n}"
    headers = {
    'Content-Type': 'application/json'
    }

    response = requests.request("POST", url, headers=headers, data=payload.encode('utf-8'))

    #print(response.text) 

    return


def sendingMsgToClient(cName, cContact,date, time):
    


    url = "https://api.chat-api.com/instance294124/sendMessage?token=bfllgpii7xqb42zq"

    payload="{\r\n  \"body\": \"Hi " + str(cName) +"\xF0\x9F\x98\x83  \\n*Session Alert* \\n\\n Your Session has been confirmed . Our Psychologist will make you a normal call at the following time  \\n\\nDate : " + str(date) +" \\nTimings : " + str(time)+"\",\r\n  \"phone\": " + str(cContact)+"\r\n}"
    headers = {
    'Content-Type': 'application/json'
    }

    response = requests.request("POST", url, headers=headers, data=payload)

    #print(response.text) 

    return


def sendSessionConfirmationMSg(email, problemStatement, psychologist, date, time, paidOrNot):
    lg.finalLog()

    logging.info("sendSessionConfirmationMSg")
    psychologistContact=vwdt.getPsychologistConatct(psychologist)
    cName, cContact= vwdt.getClientDetails(email)
    time=(time.split("+"))[0]
    sendingMsgToPsychologist(psychologist,psychologistContact,cName, cContact,email,problemStatement,date, time)
    sendingMsgToClient(cName, cContact,date, time)

    return











