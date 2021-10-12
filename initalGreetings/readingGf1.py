#usig google api 
import databaseFunctions.firebase.createFirebaseData as inst 
import gspread
from oauth2client.service_account import ServiceAccountCredentials
import sqlite3
import pandas as pd 
import databaseFunctions.firebase.viewFirebaseData as vwdt
import basicFunctions.contactCorrection as bfun
from contactMethods.whatsapp import greetingMessages as whts
from contactMethods.whatsapp import schedulingLinkForwarding as slf
from contactMethods.mail import sendMail as sdm
from contactMethods.whatsapp import msgToAdmin as mta
import databaseFunctions.whattsappTakeover as wt
import yaml


def readingGF1():

    #configurations need to read from configurations.yaml file
    with open("configuration.yml", "r") as ymlfile:
        cfgMain = yaml.load(ymlfile)  

    #taking over whatsapp
    wt.whattsappTakeover()

    #mainsheet name
    sheetName=cfgMain["mainSheetName"]      
    lastreadindex=cfgMain["gf1LastReadIndex"] 

    #file path
    scope = ["https://spreadsheets.google.com/feeds",'https://www.googleapis.com/auth/spreadsheets',"https://www.googleapis.com/auth/drive.file","https://www.googleapis.com/auth/drive"]

    credentials = ServiceAccountCredentials.from_json_keyfile_name('cred.json',scope)
    client = gspread.authorize(credentials)


    #reading data from Google form 1 
    gf1Spreadsheet = client.open(str(sheetName)).worksheet("GF1")
    gf1Data = gf1Spreadsheet.get_all_values()
    headings= gf1Data[0]
    gf1RemainingData=gf1Data[lastreadindex:]

    print("processing "+ str(len(gf1RemainingData)) + " enteries ")
    entryNumber=1

    for entry in gf1RemainingData:

        timeStamp=entry[0]
        name= entry[1]
        number= entry[2]
        email=entry[3]
        country=entry[4]
        otherPlatform=entry[5]
        issue=entry[6]
        referral=entry[7] 

        if len(otherPlatform)<3:
            otherPlatform="NA"

        inst.createGf1(name,number,email,country,otherPlatform,issue,referral)
        val=vwdt.isavailable(email,number)


        if val==False:
            contactVerifierd=bfun.contactCorrection(number,country)
            inst.createClientDetails(name,email,contactVerifierd,country,'NA')
            if(whts.send_Message(name,contactVerifierd)==False):
                sdm.F(name,email)
                mta.alternativePlatform(name,otherPlatform)
            

        else:
            Name,contactnumber,country,email,Psychologist=val
            #inst.insertIntoWaitingListPrority(client_id,email, Psychologist, "NO")
            slf.schedulingLinkForwarding(Name,contactnumber)


        print("Currently processing----------->" + str(entryNumber) + " out of "+ str(len(gf1RemainingData)))
        lastreadindex=lastreadindex+1
        entryNumber=entryNumber+1


    cfgMain["gf1LastReadIndex"]= lastreadindex
    with open('configuration.yml', 'w') as fp:
        yaml.dump(cfgMain, fp)
    

    return

   
   