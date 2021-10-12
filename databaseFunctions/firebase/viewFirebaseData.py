from firebase import firebase
import pandas as pd
from basicFunctions.LessLinkOpeningsPsychologist import findTop4PsychologistwithLessLinkOpenings
import databaseFunctions.firebase.createFirebaseData as inst 


firebase=firebase.FirebaseApplication("https://firstfirebaseproject-ced34-default-rtdb.firebaseio.com/",None)

def viewcalendlyLinks():
    result=firebase.get('/calendlyLinks','')
    data=pd.DataFrame(result)
    data=data.T
    list(data.values)
    return list(data.values)




def isPsyHavingSessionOn(psy,date):
    result=firebase.get('/scheduledSessions','')
    data=pd.DataFrame(result)
    data=data.T
    data=data[(data["psychologist"]==psy) &( data["date"]==date)]
    if data.empty==True:
        print(False)
    else:
      print(True)


    




def LinkOpenedinLast24Hrs(psy):
    result=firebase.get('/linkAccessed','')
    data=pd.DataFrame(result)
    data=data.T
    data=data[(data["name"]==psy)]
    return ( int(data['LinkOpenedinLas24Hrs'])+int(data['linkOpenedSinceLastSync']) )




def getCalendlyInfo(psychologists,date):

    psyWithNoOfTimesLinkAccess=dict()
    result=firebase.get('/calendlyLinks','')
    data=pd.DataFrame(result)
    data=data.T
# =============================================================================
#     for psy in psychologists:
#          if isPsyHavingSessionOn(psy,date)==False : #returning true or false based on if the psycholofist is having session on given day or not.. will be checking from ScheduledSession Table
#              psyWithNoOfTimesLinkAccess[psy]=LinkOpenedinLast24Hrs(psy)
# 
#     psychologists=findTop4PsychologistwithLessLinkOpenings(psyWithNoOfTimesLinkAccess) # will return list of psychologist name    
# 
# =============================================================================
    data = viewcalendlyLinks()

    return data
  


def updateLinkAccessed(name,val):
    result=firebase.get('/linkAccessed','')  
    data=pd.DataFrame(result)
    data=data.T
    data1=data[(data['name']==name)].index
    print(data1)
    for i in data1:
        result=firebase.put('/linkAccessed/{}'.format(i),"LinkOpenedinLas24Hrs",'{}'.format(val)) 
        result=firebase.put('/linkAccessed/{}'.format(i),"linkOpenedSinceLastSync",'0') 

#updateLinkAccessed('dips','val')
def detailsFromLinkAccessed():
     result=firebase.get('/linkAccessed')  
     data=pd.DataFrame(result)
     data=data.T
     for val in data:
         if val[1]==0:
             continue
         else: 
             total=int(val[1]) + int(val[2])
             updateLinkAccessed(val[0],total)            # update both fields
        

def readCadLinksAndKeys(psycho):
    result=firebase.get('/calendlyLinks')
    data=pd.DataFrame(result)
    data=data.T
    data=data['Name'].isin(psycho)
    print(data)




def checkingWaitingListprority(email):
    result=firebase.get('/waitingListPrority','')
    data=pd.DataFrame(result)
    data=data.T
    data=data[data["email"]==email]
    print(data)
    if data.empty==True:
        print(False)
    else:
      print(True)


def checkingWaitingList(email):
    result=firebase.get('/waitingList','')
    data=pd.DataFrame(result)
    data=data.T
    data=data[data["email"]==email]
    print(data)
    if data.empty==True:
        print(False)
    else:
      print(True)



def checkingScheduledSessions(email):
    try:
        result=firebase.get('/scheduledSessions','')
        data=pd.DataFrame(result)
        data=data.T
        data=data[data["email"]==email]
        #print(data)
        if data.empty==True:
            return False
        else:
          return True
    except:
         return False



def deletingFromWaitinglist(email):
    result=firebase.get('/GF1/','')
    data2=pd.DataFrame(result)

    data2=data2.T

    data_new=data2[(data2["email"]==email)].index

    for i in  data_new:
        result=firebase.delete('/GF1/{}'.format(i),'')

        data=pd.DataFrame(result)
        data=data.T

    if data.empty==True:
        print(False)
    else:
        print(True)


def isavailable(email,contact):
    try:
        result=firebase.get('/clientDetails','')
        data=pd.DataFrame(result)
        data=data.T
        data=data[(data["email"]==email) | (data["contactNumber"]==contact)]
        if data.empty==True:
            return False
        else:
            return list(data.iloc[0])
    except KeyError:
        return False



def getURlForPsychologist(name):
    result=firebase.get('/calendlyLinks','')
    data=pd.DataFrame(result)
    data=data.T
    data=data[(data["Name"]==name)]
    return list(data['calendlyLinks'])


def listOfScheduledSesions():
    result=firebase.get('/scheduledSessions','')
    data=pd.DataFrame(result)
    data=data.T
    return data.values


def listOfClients():
    result=firebase.get('/clientDetails','')
    data=pd.DataFrame(result)
    data=data.T
    return data.values

def getThePsychologistName(mailId):
    result=firebase.get('/calendlyLinks','')
    data=pd.DataFrame(result)
    data=data.T
    data=data([data["email"]==mailId])
    print(data["Name"])



def getClientDetails(mailId):
    result=firebase.get('/clientDetails','')  
    data=pd.DataFrame(result)
    data=data.T
    data=data([data["email"]==mailId])
    print(data[["name",'contactNumber']])    

def getThePsychologistList():
    result=firebase.get('/calendlyLinks','')
    data=pd.DataFrame(result)
    data=data.T
    return list(data["Name"].values)





def tranferScheduledSession(mailId):
    result=firebase.get('/scheduledSessions/','')  
    data=pd.DataFrame(result)
    data=data.T
    data=data[data["email"]==mailId]
    for id,email,status,psychologist,date,time,paidornot in zip(data['id'],data['email'],data['status'],data['psychologist'],data['date'],data['time'],data['paidOrNot']):
        inst.completedsession(id,paidornot,email,date,time,status,psychologist)
    data_new=data[data["email"]==mailId].index
    for i in  data_new:
        result=firebase.delete('/scheduledSessions/{}'.format(i),'')


    







            







