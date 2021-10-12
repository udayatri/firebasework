from os import link
from firebase import firebase
from firebase import firebase
import firebase_admin
from firebase_admin import credentials
import time
import pandas as pd

 
#creating service account key
 
#initializing the app
firebase =firebase=firebase.FirebaseApplication("https://firstfirebaseproject-ced34-default-rtdb.firebaseio.com/",None)


def delCadVal(name):
    result=firebase.get('/calendlyLinks/','')
    data=pd.DataFrame(result)
    data=data.T   
    data_new=data[(data["Name"]==name)].index

    for i in  data_new:
        result=firebase.delete('/calendlyLinks/{}'.format(i),'')

    return



