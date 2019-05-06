#!/usr/bin/python3

######################################################################
# Copyright (c). All rights reserved                                 #
# GNU GENERAL PUBLIC LICENSE                                         #
# Version 3, 29 June 2007                                            #
#                                                                    #
# Coded by Solomon Narh (::XploitsR Author::)                        #
# Github: https://github.com/XploitsR/XRMailer                       #
# Facebook: https://facebook.com/RXploits                            #
# Twitter: https://twitter.com/RXploits                              #
# Telegram: https://t.me/RXploits                                    #
# Website: https://xploitsr.tk                                       #
#                                                                    #
#             ::PERSONAL ME::                                        #
# Github: https://github.com/XploitsR/XRMailer                       #
# Facebook: https://facebook.com/solomon.narh.311                    #
# Twitter: https://twitter.com/Solomon97062                          #
# Instagram: @_xploitsr_author_1                                     #
# Email: solomonnarh97062@gmail.com                                  #
######################################################################

import sys,csv
import smtplib, ssl
import getpass
import time
from email import encoders
from email.mime.base import MIMEBase
from email.mime.text import MIMEText
from email.mime.multipart import MIMEMultipart

Temp = False
userMassBool = None
userDocBool = None
bBool = None

############################
# Pre-defined functions!!  #
############################

#SMTP
def smtp_portSSL(smtp_server):
   return [str(smtp_server),int(465)]
def smtp_portTLS(smtp_server):
   return [str(smtp_server),int(578)]

#Temps && files
def Tempt():
    return "Templates/"
def Email():
    return "Emails/"
def File():
    return "Files/"
def Templates():
    from Templates.templates import friendly,business,customHtml,customText
    return [friendly(),business(),customHtml(),customText()]

def print_customText():
    print(
"""
#############################
# ::CUSTOM TEXT::           #
# Put your Custom Text      #
# Into The Templates Folder #
# And Specify The Name Here #
# Save It As .txt           #
# Example: sample.txt       #
#############################
 """
         )

def print_customTextHtml():
    n = """
################################
# ::CUSTOM TEXT::              #
# Put your Custom Text         #
# Into The Templates Folder    #
# And Specify The Name Here    #
# Save It As .txt              #
# Example: sample.txt          #
# It can include any <body>    #
# Elements::example <b><a><i>  #
# <img><p><span> and many more #
################################
 """
    b = """
#############################
# ::CUSTOM HTML TEMPLATE::  #
# Put your Custom Template  #
# Into The Templates Folder #
# And Specify The Name Here #
# Example: sample.html      #
#############################
 """
    return [n,b]

def print_docText():
    print(
"""
###############################
# ::Specify your attachment:: #
# put your file               #
# into the files folder       #
# and specify the name here   #
# example: sample.png         #
###############################
 """
   )

def accept_file(fileDir,filetype,readType,fileExt):

   try:

      cText = str(input(f"[#] File (eg: {filetype}): "))
      if len(cText.strip()) > 0:
         verifyTEXTFile = open(fileDir + cText.strip(),f"{readType}")
         if verifyTEXTFile is not None:
            with verifyTEXTFile as f:
                 r = f.read()
                 temp = Templates()[3] %(r.strip())
                 f.close()
      
      else:
        print(f"[!] Don't be silly!, please specify a {fileExt} file")
        quit()

   except FileNotFoundError:
      print("[!] Don't be silly!, file not found")
      quit()
   return temp

def accept_docfile(filetype,readType):
   #Accept Attachment
   try:
      global userDocBool,doc;
      userDoc = str(input(f"[#] File(eg: {filetype}): "))
      if len(userDoc.strip()) > 0:
         verifyDOCFile = open(File() + userDoc.strip(),f"{readType}")
         if verifyDOCFile is not None:
            with verifyDOCFile as attachment:
                 #Add file as application/octet-stream
                 #The Email Client can download this attachment
                 userDocBool = True
                 doc = MIMEBase("application","octet-stream")
                 doc.set_payload(attachment.read())
                 encoders.encode_base64(doc)
                 doc.add_header(
                   "Content-Disposition",
                   f"attachment; filename={userDoc}",
                 )
      else:
        print("[!] Don't be silly!, please specify an attachment")
        quit()

   except FileNotFoundError:
      print("[!] Don't be silly!, file not found")
      quit()
  
def print_friendlyHdtext():
   print(
"""
#############################
# ::LETS EDIT THE FILE::    #
#        HEADER             #
#   Title,Content..etc      #
#############################
"""
          )

def accept_friendlyFunc(t,s,m,f,tw,num):

  try:
     cTitl = str(input(f"[#] Your Title (eg: {t}): "))
     cSalu = str(input(f"[#] Your Salutation (eg: {s}): "))
     time.sleep(1)
     print(print_customTextHtml()[0])
     cBody = str(input(f"[#] Your Message(File) (eg: {m}): "))
     time.sleep(1)
     print(
"""
#############################
# ::LETS EDIT THE FILE::    #
#        FOOTER             #
#   How one gets in touch   #
#        with you.          #
#############################
"""
          )
     cFb = str(input(f"{f}"))
     cTw = str(input(f"{tw}"))
     
     try:
      if len(cTitl.strip()) > 0 and len(cSalu.strip()) > 0 and len(cBody.strip()) > 0 and len(cFb.strip()) > 0 and len(cTw.strip()) > 0:
         verifyCBodyFile = open(Tempt() + cBody.strip())
         if verifyCBodyFile is not None:
            with verifyCBodyFile as f:
                r = f.read()
                if num == 0:
                   temp = Templates()[num] %(cTitl.strip(),cSalu.strip(),r.strip(),cFb.strip(),cTw.strip())
                elif num == 1:
                   temp = Templates()[num] %(cTitl.strip(),cSalu.strip(),r.strip(),cFb.strip(),cTw.strip().replace(" ","+"),cTw.strip())
                f.close()
         else:
            print("[!] Don't be silly!, please specify your custom message file(.txt)")
            quit()
     except FileNotFoundError:
      print("[!] Don't be silly!, file not found")
      quit()

  except ValueError:
     print("[!] Don't be silly!, Unknown value")
     quit()
  return temp

######################
####### End ##########
######################

#this extends smtp_*()
print(
"""
###########################
# EMAIL SERVICE PROVIDERS #
###########################
"""
)

try:
   print(" 1: Gmail\n 2: Yahoo")
   userProv = int(input("[#] Choose: "))
   #Verify Email Service Providers
   if userProv == 1:
     smtp_S = smtp_portSSL("smtp.gmail.com")[0]
     smtp_P = smtp_portSSL(None)[1]
   elif userProv == 2:
     smtp_S = smtp_portSSL("smtp.mail.yahoo.com")[0]
     smtp_P = smtp_portTLS(None)[0]
   else:
     print("[!] Don't be silly!, choose from above list");
     quit()

except ValueError:
   print("[!] Don't be silly!, Unknown value")
   quit()

print(" ")
time.sleep(1)

#Email type
print(
"""
#################
# TYPE OF EMAIL #
#################
"""
)

try:
   from Templates.templates import customText
   print(" 1: PlainText\n 2: HTML\n 3: PlainText With Attachment\n 4: HTML With Attachment")
   userType = int(input("[#] Choose: "))

   #Verify Email Type
   if userType == 1:
     Emtype = "plain"
     userDocBool = None
     print_customText()
     temp = accept_file(Tempt(),"sample.txt","r",".txt")

   elif userType == 2:
     Emtype = "html"
     Temp = True
     userDocBool = None

   elif userType == 3:
     Emtype = "plain"
     print_customText()
     temp = accept_file(Tempt(),"sample.txt","r",".txt")
     print(" ")
     time.sleep(1)
     print_docText()
     accept_docfile("sample.pdf","rb")

   elif userType == 4:
     Emtype = "html"
     Temp = True
     print_docText()
     accept_docfile("sample.pdf","rb")

   else:
     print("[!] Don't be silly!, choose from above list");
     quit()

except ValueError:
   print("[!] Don't be silly!, Unknown value")
   quit()

print(" ")
time.sleep(1)

try:

 if Temp:
    print(
"""
###################
# CHOOSE TEMPLATE #
###################
"""
   )
    print(" 1: Friendly\n 2: Business\n 3: Custom ")
    userTemp = int(input("[#] Choose: "))

    if userTemp == 1:
       print_friendlyHdtext()
       fb = "[#] Facebook Link (eg: https://facebook.com/you): "
       tw = "[#] Twitter Link (eg: https://twitter.com/you): "
       temp = accept_friendlyFunc("Love letter","Hi Sarah","sample.txt",fb,tw,0)
 
    elif userTemp == 2:
       print_friendlyHdtext()
       fb = "[#] Companies Name (eg: Facebook inc): "
       tw = "[#] Companies Address (eg: 1601 Willow Road): "
       bTemp = accept_friendlyFunc("Webinar","Dear members,","sample.txt",fb,tw,1)
       bBool = True

    elif userTemp == 3:
       print(print_customTextHtml()[1])
       temp = accept_file(Tempt(),"sample.html","r",".html")
    else:
     print("[!] Don't be silly!, choose from above list");
     quit()

except ValueError:
   print("[!] Don't be silly!, Unknown value")
   quit()

time.sleep(1)

try:
  print(
"""
#######################
# TO MULTIPLE USERS ? #
#######################
 """
  )
  print(" 1: Yes\n 2: No")
  userMass = int(input("[#] Choose: "))
  time.sleep(1)
  print(" ")

  if userMass == 1:
     print(
"""
#############################
# Put A File In Emails      #
# Folder Containing Your    #
# Emails...                 #
# First Line Of The File    #
# Should Be *number,email*  #
# Without the asterisks (*) #
# For Each Column, Specify  #
# The Number...             #
# File Should Be Saved With #
# An Extension as .csv in   #
# Emails Folder...          #
#                           #
# ::You can Check a sample::# 
# ::File in Emails Folder:: #
#                           #
# ::Example:: sample.csv    #
#                           #
# number,email              #
# 1,abc@mailServer.com      #
# 2,efg@mailServer.co       #
# 3,xyz@mailServer.net      #
#############################
 """
         )

     try:
       userMassFile = str(input("[#] File(eg: sample.csv): "))
       if len(userMassFile.strip()) > 0:
          verifyCSVFile = open(Email() + userMassFile.strip())
          if verifyCSVFile is not None:
             userMassBool = True

       else:
          print("[!] Don't be silly!, please specify your .csv file")
          quit()

     except FileNotFoundError:
       print("[!] Don't be silly!, file not found")
       quit()

  elif userMass == 2:
   userMassBool = None

except ValueError:
   print("[!] Don't be silly!, Unknown value")
   quit()

time.sleep(1)

print(
"""
#############
# SEND MAIL #
#############
 """
)

from_addr = str(input("[*] Senders email: "))
from_addr.strip()
password = getpass.getpass("[*] Senders password: ")
from_name = str(input("[*] Senders name: "))
if userMassBool is None:
   to_addrs = str(input("[*] Recipients email: "))
subject =  str(input("[*] Subject: "))

#Multipart Email Module :: Multipart("alternate")
msg = MIMEMultipart()
msg["Subject"] = subject
#Bug in Gmail is ;)
msg["From"] = from_name + " ;)"

if len(from_addr.strip()) > 0 and len(password.strip()) > 0 and len(subject.strip()) > 0:

   print("[*] Sending Mail...Please Wait...")
   
   #create a secure SSL context 
   context = ssl.create_default_context()
   try:
     with smtplib.SMTP_SSL(smtp_S, smtp_P, context=context) as server:
        server.login(from_addr, password)
        if userMassBool is not None and userDocBool is None:
           with verifyCSVFile as file:
                reader = csv.reader(file)
                next(reader)  # Skip header row
                if bBool is not None:
                   temp = bTemp
                # Turn these into plain/html MIMEText objects
                Emtype = MIMEText(temp, Emtype)
                msg.attach(Emtype)
                for number,email in reader:
                    server.sendmail(
                        from_addr,
                        email.strip(),
                        msg.as_string(),
                    )
                    print(f"[*] Mail Sent To {email}")
        elif userMassBool is not None and userDocBool is not None:
           with verifyCSVFile as file:
                reader = csv.reader(file)
                next(reader)  # Skip header row
                if bBool is not None:
                   temp = bTemp
                # Turn these into plain/html MIMEText objects
                Emtype = MIMEText(temp, Emtype)
                msg.attach(Emtype)
                msg.attach(doc)
                for number,email in reader:
                    server.sendmail(
                        from_addr,
                        email.strip(),
                        msg.as_string(),
                    )
                    print(f"[*] Mail Sent To {email}")
        elif userMassBool is None and userDocBool is None:  
           msg["To"] = to_addrs.strip()
           if bBool is not None:
              temp = bTemp
           Emtype = MIMEText(temp, Emtype)
           msg.attach(Emtype)
           server.sendmail(
               from_addr,
               to_addrs.strip(),
               msg.as_string(),
           )
           print("[*] Mail Sent To " + to_addrs)
        elif userMassBool is None and userDocBool is not None:
           if bBool is not None:
              temp = bTemp
           Emtype = MIMEText(temp, Emtype)
           msg.attach(Emtype)
           msg.attach(doc)
           server.sendmail(
               from_addr,
               to_addrs.strip(),
               msg.as_string(),
           )
           print("[*] Mail Sent To " + to_addrs)
           server.quit()
   except Exception as e:
     print(e)
     quit()
else:
   print("[!] Don't be silly!, spaces cant be empty")
   quit()
