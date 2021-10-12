#usig google api 
import databaseFunctions.firebase.createFirebaseData as inst 
import gspread
from oauth2client.service_account import ServiceAccountCredentials
import sqlite3
import pandas as pd 
import databaseFunctions.firebase.viewFirebaseData as vwdt
import databaseFunctions.insertData as inst
from contactMethods.whatsapp import schedulingLinkForwarding as slf
import basicFunctions.contactCorrection as bfun
import yaml 


def readingGF2():

    #configurations need to read from configurations.yaml file
    with open("configuration.yml", "r") as ymlfile:
        cfgMain = yaml.load(ymlfile)  


    #mainsheet name
    sheetName=cfgMain["mainSheetName"]      
    lastreadindex=cfgMain["gf2LastReadIndex"] 

    #file path
    scope = ["https://spreadsheets.google.com/feeds",'https://www.googleapis.com/auth/spreadsheets',"https://www.googleapis.com/auth/drive.file","https://www.googleapis.com/auth/drive"]

    credentials = ServiceAccountCredentials.from_json_keyfile_name('cred.json',scope)
    client = gspread.authorize(credentials)
   
    sheet = client.open(str(sheetName)).worksheet("GF2")
    data = sheet.get_all_records()
    #print(data)

    g=pd.DataFrame(data)

    gf2RemainingData=len(g)-lastreadindex
    print("processing "+ str(gf2RemainingData) + " enteries in GF2")

    for i in range(lastreadindex, len(g)):
    
        print(g["Email"][i])
        val=vwdt.isavailable(g["Email"][i],g["Contact"][i])
        Name,contactnumber,country,email,Psychologist=val
        #inst.insertIntoWaitingList(client_id,email, g["Issue"][i])
        contactVerifierd=   bfun.contactCorrection(contactnumber,country)
        slf.schedulingLinkForwarding(Name,contactVerifierd)

        print("Currently processing----------->" + str(i) + " out of "+ str(len(g)))

        lastreadindex=lastreadindex+1

    cfgMain["gf2LastReadIndex"]= lastreadindex

    with open('configuration.yml', 'w') as fp:
        yaml.dump(cfgMain, fp)
    

    return

