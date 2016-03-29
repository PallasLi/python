'''
Created on 2016年3月22日

@author: lyt
'''
import smtplib
from smtplib import SMTPException

sender = 'liyongtao@atwasoft.net'
receivers = ['liyongtao@atwasoft.net']

message = """From: From Person 
To: To Person 
Subject: SMTP e-mail test

This is a test e-mail message.
"""

try:
#    smtpObj = smtplib.SMTP('localhost')
   smtpObj = smtplib.SMTP('mail.atwasoft.net', 25)
   smtpObj.sendmail(sender, receivers, message)         
   print ("Successfully send email")
   smtpObj.quit()
except SMTPException:
   print ("Error: unable to send email")

try:
#    smtpObj = smtplib.SMTP('localhost')
   smtpObj = smtplib.SMTP()
   smtpObj.connect('mail.atwasoft.net', 25)
   smtpObj.login(sender, "lyt870705")
   smtpObj.sendmail(sender, receivers, message)         
   print ("Successfully send email")
   smtpObj.quit()
except SMTPException:
   print ("Error: unable to send email")