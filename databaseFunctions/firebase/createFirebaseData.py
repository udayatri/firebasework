from os import link
from firebase import firebase
from firebase import firebase
import firebase_admin
from firebase_admin import credentials
import time

 
#creating service account key
 
#initializing the app
firebase =firebase=firebase.FirebaseApplication("https://firstfirebaseproject-ced34-default-rtdb.firebaseio.com/",None)




def createGf1(text1,text2,text3,text4,text5,text6,text7):
 start_time = time.time()



 tableNew1={
       
        'Name' :text1 ,
        'WhatsappNumber' : text2,
        'email': text3,
        'country': text4,
        'othermedium':text5,
        'issuse': text6,
        'Referral':text7
}


 result=firebase.post('/GF1',tableNew1)

# createGf1 
def createGf2(text1,text2,text3,text4):
 tableNew2={
        'Name': text1 ,
        'WhatsappNumber': text2,
        'email' :text3,
        'issuse':text4
       
 }
 result=firebase.post('/GF2',tableNew2)



# create table for calendly links and authentication  key
def calendlyLinks(text1,text2,text3,text4,text5,text6,text7):
 tableNew3={
        'Name' :text1 ,
        'email' :text2,
        'contact': text3,
        'calendlyLinks': text4 ,
        'imageName': text5,
        'Description': text6,
        'Type': text7
 }
 result=firebase.post('/calendlyLinks',tableNew3)


def createClientDetails(text1,text2,text3,text4,text5):
 tableNew4={ 
            'Name' :text1 ,
            'email' :text2,
            'contactNumber': text3,
            'country' :text4,
            'psychologist': text5
}       
 result=firebase.post('/clientDetails',tableNew4)      


#waitingList
def waitinglist(text1,text2,text3,text4):
 tableNew5={
        'id' :text1,
        'email': text2,
        'problemStatement': text3,
        'preferableTimings':text4
 }
 result=firebase.post('/waitingList',tableNew5)      


# waitingListPrority
def waitingListPrority (text1,text2,text3,text4):
 tableNew6={
        'id': text1,
        'email' :text2,
        'psychologist' :text3,
        'paidOrNot': text4
 }
 result=firebase.post('/waitingListPrority',tableNew6)    

   
  #scheduledSessions       
def createScheduledSessions(text2,text3,text4,text5,text6,text7):
 tableNew7={
        'email' :text2,
        'problemStatement': text3,
        'psychologist' :text4,
        'date' :text5,
        'time': text6,
        'paidOrNot' :text7
}
 result=firebase.post('/scheduledSessions',tableNew7)    
  #linkAccessed       
def createLinkAccessed(text1,text2,text3):
 tableNew8={
        'name': text1,
        'linkOpenedSinceLastSync': text2,
        "LinkOpenedinLas24Hrs" :text3 
 }
 result=firebase.post('/linkAccessed',tableNew8)  
 


def completedsession(text1,text2,text3,text4,text5,text6,text7):
 tableNew9={
            'client_id' :text1,    
            'paid': text2,
            'email': text3,
            'date' :text4,
           'time' :text5,
            'status': text6,
            "psychologist": text7
}
 result=firebase.post('/completedsession',tableNew9)    

def createreminder(text1,text2,text3,text4):

 tableNew10={
       
        'Name' :text1 ,
        'WhatsappNumber' : text2,
        'Status': text3,
        'Time':text4
}


 result=firebase.post('/Reminder',tableNew10)