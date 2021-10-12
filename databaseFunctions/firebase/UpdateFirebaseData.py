from firebase import firebase
import pandas as pd
firebase=firebase.FirebaseApplication("https://firstfirebaseproject-ced34-default-rtdb.firebaseio.com/",None)

def updateGF1(col,name,update):
    result=firebase.get('/GF1','')  
    data=pd.DataFrame(result)
    data=data.T
    data1=data[(data['{}'.format(col)]==name)].index
    print(data1)
    for i in data1:
        result=firebase.put('/GF1/{}'.format(i),"{}".format(col),'{}'.format(update))
updateGF1('Name','Dipesh','dips')
   
def updateGF2(col,name,update):
    result=firebase.get('/GF2','')  
    data=pd.DataFrame(result)
    data=data.T
    data1=data[(data['{}'.format(col)]==name)].index
    print(data1)
    for i in data1:
        result=firebase.put('/GF2/{}'.format(i),"{}".format(col),'{}'.format(update))




def updatecalendlyLinks(col,name,update):
    result=firebase.get('/calendlyLinks','')  
    data=pd.DataFrame(result)
    data=data.T
    data1=data[(data['{}'.format(col)]==name)].index
    print(data1)
    for i in data1:
        result=firebase.put('/calendlyLinks/{}'.format(i),"{}".format(col),'{}'.format(update))


def updateclientDetails(col,email,update):
    result=firebase.get('/clientDetails','')  
    data=pd.DataFrame(result)
    data=data.T
    data1=data[(data['{}'.format(col)]==email)].index
    print(data1)
    for i in data1:
        result=firebase.put('/clientDetails/{}'.format(i),"{}".format(col),'{}'.format(update))



def updatewaitingList(col,name,update):
    result=firebase.get('/waitingList','')  
    data=pd.DataFrame(result)
    data=data.T
    data1=data[(data['{}'.format(col)]==name)].index
    print(data1)
    for i in data1:
        result=firebase.put('/waitingList/{}'.format(i),"{}".format(col),'{}'.format(update))




def updatewaitingListPrority(col,name,update):
    result=firebase.get('/waitingListPrority','')  
    data=pd.DataFrame(result)
    data=data.T
    data1=data[(data['{}'.format(col)]==name)].index
    print(data1)
    for i in data1:
        result=firebase.put('/waitingListPrority/{}'.format(i),"{}".format(col),'{}'.format(update))

    
def updatescheduledSessions(col,name,update):
    result=firebase.get('/scheduledSessions','')  
    data=pd.DataFrame(result)
    data=data.T
    data1=data[(data['{}'.format(col)]==name)].index
    print(data1)
    for i in data1:
        result=firebase.put('/scheduledSessions/{}'.format(i),"{}".format(col),'{}'.format(update))
    


def updatecompletedsession(col,name,update):
    result=firebase.get('/scheduledSessions','')  
    data=pd.DataFrame(result)
    data=data.T
    data1=data[(data['{}'.format(col)]==name)].index
    print(data1)
    for i in data1:
        result=firebase.put('/scheduledSessions/{}'.format(i),"{}".format(col),'{}'.format(update))
    
#update reminder table  
def updatereminder(col,name,update):
    result=firebase.get('/Reminder','')  
    data=pd.DataFrame(result)
    data=data.T
    data1=data[(data['{}'.format(col)]==name)].index
    print(data1)
    for i in data1:
        result=firebase.put('/Reminder/{}'.format(i),"{}".format(col),'{}'.format(update))
