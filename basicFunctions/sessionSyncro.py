# -*- coding: utf-8 -*-
"""
Created on Sat Aug 28 09:12:04 2021

@author: hp
"""

from googleapiclient.discovery import build
from google_auth_oauthlib.flow import InstalledAppFlow
import pickle
from datetime import datetime,timedelta
import databaseFunctions.firebase.viewFirebaseData as vwdt
import databaseFunctions.firebase.createFirebaseData as inst 
import databaseFunctions.whattsappTakeover as wt
import logging
from logging.handlers import RotatingFileHandler
import basicFunctions.logfille as lg



def syncro():
    lg.finalLog()
    credentials = pickle.load(open("basicFunctions/token.pkl", "rb"))
    service = build("calendar", "v3", credentials=credentials)
    result = service.calendarList().list().execute()
    
    ids=result['items']
    now = datetime.now() - timedelta(days = 2)
    minDate=now.strftime('%Y-%m-%dT%H:%M:%S') + str("+05:30")
    
    #taking over whatsapp
    wt.whattsappTakeover()
    
    for val in ids:
        eventlist=service.events().list(calendarId=val['id'],orderBy="updated",updatedMin=minDate).execute()
        #eventlist=service.events().list(calendarId="dipesh0439@gmail.com",orderBy="updated",updatedMin=minDate).execute()
        
        allEvents=eventlist['items']
        
        for itm in allEvents:
                    try:
                        desc=itm['description']
                    except:
                        continue
                
                
                    if desc.lower().find('drivekraft')>0 or itm['summary'].lower().find('drivekraft')>0 :
                        
                        
                        if itm['summary'].lower().find('drivekraft')>0:
                            data=desc.split("Invitee Email:")[1]
                            cltId=data.split("Additional details:")[0]
                            cltId=cltId.split("Event Type")[0]
                            cltId=cltId.replace("\n","")
                            cltId=cltId.replace(" ","")
                            bookTheSession(itm,cltId,val['id'])
                            
                       
                        for atd in range(0,len(itm['attendees'])):
                    
                            logging.info(itm['attendees'][atd]['email'])
                            if itm['attendees'][atd]['email']==val['id']:
                                continue
                            
                            bookTheSession(itm,itm['attendees'][atd]['email'],val['id'])
                            
                            
                            
        

    return
                        
    

#the  below function will delete entry from prioritywaiting list and wiaitng list and will be send confirmation message to psychologist and client 

def bookTheSession(itm,cltmail,psychoId):
    lg.finalLog()
    
    logging.info("here we are",cltmail,psychoId,"\n\n")
    
    avail=vwdt.checkingScheduledSessions(cltmail)
                            
    try:
        if avail==False:
            
            Payment='No'
            
            email=cltmail
            avail=vwdt.isavailable(email,"NA")
            ide,Name,email,contactnumber,country,Psychologist=avail
            problemStatement = "NA"
            
            #print(ide,email, problemStatement)
            psychologist= vwdt.getThePsychologistName(psychoId)[0]
            #psychologist= vwdt.getThePsychologistName('dipesh0439@gmail.com')[0]
            date, time=itm['start']['dateTime'].split('T')
            paidOrNot=Payment
            inst.createScheduledSessions(email, problemStatement, psychologist, date, time, "Yes")
            vwdt.updateClientPsyologistName(email,"cnumber", psychologist)
            logging.info("here we are",cltmail,psychoId,"44","\n\n")
    except Exception as e:
            logging.info(e)
            return

    return 


     

# =============================================================================
# #insertIntoWaitingList('23','drishi_be16@thapar.edu', problemStatement)
# insertIntoWaitingList('1','drishi_be16@thapar.edu','bahut diakt he' )
# 
# connection = sqlite3.connect('quality.db')
# con = connection.cursor()
# 
# con.execute("SELECT * FROM waitingList")
# data=con.fetchall()
# connection.close() 
# 
# 
# 
# 
# ide,email, problemStatement, psychologist, date, time, paidOrNot="1","dkemail","prob","akshi","3-Sept-2020","3:00","yesno"
# 
#  #connecting with database -- these lines shouldn't edited
# connection = sqlite3.connect('quality.db')
# con = connection.cursor()
# 
# con.execute("""Insert into scheduledSessions
# (id,email, problemStatement, psychologist, date, time, paidOrNot) values(?,?,?,?,?,?,?)""",(str(ide),str(email),str(problemStatement),str(psychologist),str(date),str(time),str(paidOrNot)))
# 
# connection.commit()
# connection.close()
# 
# 
# connection = sqlite3.connect('quality.db')
# con = connection.cursor()
# 
# con.execute("Delete from scheduledSessions")
# 
# connection.commit()
# connection.close()
# =============================================================================
