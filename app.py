from flask import Flask, render_template,request,redirect, url_for,send_file
import yaml
import  initalGreetings.readingGf1 as ig1
import  initalGreetings.readingGF2 as ig2
import schedulingAlgo.basicFunctions as basFun
import databaseFunctions.firebase.viewFirebaseData as vwdt
import databaseFunctions.firebase.createFirebaseData as inst 
import databaseFunctions.firebase.deleteFirebaseData as dlt
import basicFunctions.downloadData as dwd
import basicFunctions.resetLinkAccess as rst
import basicFunctions.resetconf as res
import basicFunctions.sessionSyncro as sync
from datetime import date,timedelta
import logging
from logging.handlers import RotatingFileHandler
import basicFunctions.logfille as lg




app = Flask(__name__) #create a flask object

@app.route('/')
def home():
    ig1.readingGF1()
    ig2.readingGF2()
    sync.syncro()
    return "execution completed2"



@app.route('/resetlink')
def resetlink():
    rst.resetLinkedAccess()
    return "completed"

@app.route('/resetconf')
def resetconf():
    res.resetconf()
    return "completed"    


@app.route('/directsession')
def directsession():
    psychoList=vwdt.getThePsychologistList()
    return render_template('directSession.html',psychoList=psychoList)


@app.route('/directSessionGateWay',methods=["POST"])
def directSessionGateWay():

 #fetching the values filled by user  
  cnumber=request.values.get('cnumber')
  email=request.values.get('email')
  psycho=request.values.get('psychologist')

  val=vwdt.isavailable(email,cnumber)
  if val==False:
      return render_template("you are a new user kindky fill the below form or check your email Id or contact number")  
  else:  
      url=vwdt.getURlForPsychologist(psycho)
      return redirect(url[0])


@app.route('/insertDirectCleintDataTemplate')
def insertDirectCleintDataTemplate():
    psychoList=vwdt.getThePsychologistList()
    return render_template('admin/insertDirectCleintData.html',psychoList=psychoList)

@app.route('/insertingDirectClientData',methods=["POST"])
def insertingDirectClientData():

  #fetching the values filled by user  
  name=request.values.get('name')
  cnumber=request.values.get('cnumber')
  email=request.values.get('email')
  country=request.values.get('country')
  psycho=request.values.get('psychologist')

  inst.createClientDetails(name,email,cnumber,country,psycho)

  return "inserted data"





@app.route('/template')
def scheduling():
    now = date.today() + timedelta(days=1)
    mindate=now.strftime("%Y-%m-%d")
    Date_req = now + timedelta(days=4)
    maxdate=Date_req.strftime("%Y-%m-%d")
    return render_template("bookAppointment.html",mindate=mindate,maxdate=maxdate)


@app.route('/processing',methods=["POST"])
def processing():

  #fetching the values filled by user  
  date=request.values.get('date')
  freeTimeFrom=request.values.get('freeTimeFrom')
  freeTimeTo=request.values.get('freeTimeTo')

  print(date,freeTimeFrom,freeTimeTo )
  
  #print(date,freeTimeFrom,freeTimeTo)

  #getting day for the corresponding date
  day=basFun.dayOfWeek(date)

  #getting free slots of psychologist on that day  
  psychologistFreeSlots=basFun.gettingPsychologistFreeSlotsOnDay(day)

  #checking the availabaity of psychologist at time asked by user  
  psychologists=basFun.psychologistFreeAtRequiredTime(psychologistFreeSlots,freeTimeFrom,freeTimeTo)

  #checking calednly urls and names of psychologist of with least openings of URL in last 24 hours  
  gettingLinksOfCadely= vwdt.getCalendlyInfo(psychologists,date)  

  return render_template('cadleyIntegration.html',desc=gettingLinksOfCadely)


@app.route('/psychologist/<keys>/<name>') #issue
def gettingUrls(keys,name):
    #vwdt.incrementLinkOpen(name)
    url=vwdt.getURlForPsychologist(name)[0]   
    return redirect(url)     




@app.route('/admin')
def admin():
    return render_template("admin/adminauth.html")


@app.route('/verifyAdmin',methods=["POST"])
def verifyAdmin():  
    #reading password value
    password=request.values.get('password')

    if password=='Amadeus': 
        #password is correct
        return render_template("admin/adminLib.html")
    else:
        #password is wrong    
        return "kripya bahar jae"



    

@app.route('/addingCaledlydetails')
def addingCaledlydetails():
    return render_template("admin/CalendlyLinkAddition.html")

@app.route('/addingCalendlyUrlInfo',methods=["POST"])
def addingCalendlyUrlInfo():
    lg.finalLog()
    name=request.values.get('name')
    email=request.values.get('email')
    contact=request.values.get('contact')
    url=request.values.get('url')
    imageName=request.values.get('imageName')
    Description=request.values.get('Description')
    Type=request.values.get('Type')

    logging.info("value",name,email,contact,url,imageName,Description,Type)
    inst.calendlyLinks(name,email,contact,url,imageName,Description,Type)
    inst.createLinkAccessed(name,0,0)
    return "Done"


@app.route('/delCadlink')
def defCadlink():
    return render_template("admin/delCadLink.html")


@app.route('/delCadLinkValue')
def delCadLinkValue():
    name=request.values.get('name')
    dlt.delCadVal(name)
    return "done"


@app.route('/scldSessions')
def scldSessions():
    data=vwdt.listOfScheduledSesions()
    return render_template('admin/listOfsessions.html',data=data)


@app.route('/cltList')
def clinetlist():
    data=vwdt.listOfClients()
    return render_template('admin/listOfClients.html',data=data)

@app.route('/viewCaledlydetails')
def viewCaledlydetails():
    data=vwdt.viewcalendlyLinks()
    return render_template("admin/CalendlyLinkview.html",data=data)



@app.route('/sessioncompletd/<mailid>')
def sessioncompletdBypsycho(mailid):   
    inst.sessionCompleted(mailid) #issue
    return
   

@app.route('/delete')
def delete():   
    connection = sqlite3.connect('quality.db')
    con = connection.cursor()
    con.execute("Delete from GF1")
    con.execute("Delete from GF2")
    con.execute("Delete from clientDetails")
    con.execute("Delete from waitingList")
    con.execute("Delete from waitingListPrority")
    con.execute("Delete from scheduledSessions")
    connection.commit()
    connection.close()
    return "deleted everything finally"
   



@app.route('/download')
def download():
    dwd.download()
    return render_template('admin/download.html')


@app.route('/download2')
def download_file():
    path="dataTable.xlsx"
    return send_file(path,as_attachment=True) 



if __name__ == '__main__':
    app.run(debug= False ) #debug enabled is creating warning and error

