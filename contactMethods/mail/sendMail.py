from email.message import EmailMessage
import smtplib
import imghdr
from contactMethods.whatsapp import msgToAdmin as mta


def send_mail(name,reciever):

    EMAIL_ADDRESS = "drivekraft@gmail.com"
    EMAIL_PASSWORD = 'kxgudynwonausuqh'
    
    msg1="Hi " + str(name)+" \nYou registered for the interactive session with Drivekraft and here we are as promised 😃 .  \nIt's great that you are ready to talk and remember it's never too late."
    
    msg2="\n\n https://forms.gle/dFdsNJMErDgeauWy5"
    
    msg3="\n\nCan you please this above form😃  \nThis will help to know more about you and assign you the best match of psychologist 😇 😇  \n\nDo let us know once you filled the form , I will proceed with schedule it  "

    msg = EmailMessage() 
    msg['Subject'] = 'Greetings From Drivekraft!!'
    msg['From'] = EMAIL_ADDRESS
    msg['To'] = reciever

    msg.set_content(msg1 + msg2  + msg3)

    #msg.add_alternative(content(), subtype='html')

    try:
        with smtplib.SMTP_SSL('smtp.gmail.com', 465) as smtp:
            smtp.login(EMAIL_ADDRESS, EMAIL_PASSWORD)
            smtp.send_message(msg)
    except:
         mta.mailNotFOundMsgToAdmin(name,reciever)


    return    