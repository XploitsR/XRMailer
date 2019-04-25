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


import sys,csv,os
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
red = '\033[91m'
#text = " "
#temp = " "

#Email Service Providers
print(
"""
###########################
# EMAIL SERVICE PROVIDERS #
###########################
 """
)
print(" 1: Gmail\n 2: Yahoo")
userProv = int(input("[#] Choose: "))


#Verify Email Service Providers
if userProv == 1:
   smtp_server = "smtp.gmail.com"
   port = 465
elif userProv == 2:
   smtp_server = "smtp.mail.yahoo.com"
   port = 465
else:
   print(" ")
   print("[!] Error:: Please choose from available list");
   print(red + "[!] Aborting...");
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
print(" 1: PlainText\n 2: HTML\n 3: PlainText With Attachment\n 4: HTML With Attachment")
userType = int(input("[#] Choose: "))
#userType.strip()

#Verify Email Type
if userType == 1:
   from Templates.templates import customText
   Emtype = "plain"
   userDocBool = None

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
   try:

     cText = str(input("[#] File (eg: sample.txt): "))
     if len(cText.strip()) > 0:
        verifyTEXTFile = open("Templates/" + cText.strip())
        if verifyTEXTFile is not None:
           with verifyTEXTFile as f:
                r = f.read()
                temp = customText() %(r.strip())
                f.close()
      
     else:
       print(" ")
       print("[!] Error:: Please Specify A .txt File")
       print(red + "[!] Aborting...");
       
   except FileNotFoundError as e:
      print("[!] File Not Found")
   
elif userType == 2:
   Emtype = "html"
   Temp = True
   userDocBool = None

elif userType == 3:
   from Templates.templates import customText
   Emtype = "plain"

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
   try:

     cText = str(input("[#] File (eg: sample.txt): "))
     if len(cText.strip()) > 0:
        verifyTEXTFile = open("Templates/" + cText.strip())
        if verifyTEXTFile is not None:
           with verifyTEXTFile as f:
                r = f.read()
                temp = customText() %(r.strip())
                f.close()
        else:
           print(" ")
           print("[!] Error:: Please Specify A .txt File")
           print(red + "[!] Aborting...");
           quit()
     else:
        print(" ")
        print("[!] Error:: Space Cant Be Empty");
        print(red + "[!] Aborting...");
        quit()
   except FileNotFoundError as e:
     print("[!] File Not Found")

   print(" ")
   time.sleep(1)
  

#Document
   print(
"""
#############################
# ::Specify The FILE::      #
# Put your File             #
# Into The Files Folder     #
# And Specify The Name Here #
# Example: sample.png       #
#############################
 """
   )
   userDoc = str(input("[#] File(eg: sample.png): "))
   if len(userDoc.strip()) > 0:
      verifyDOCFile = open("Files/" + userDoc.strip(),"rb")
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
                f"attachment; filename= {userDoc}",
              )
      else:
           print(" ")
           print("[!] Error:: Please Specify A File")
           print(red + "[!] Aborting...");
           quit()
         
   else:
       print(" ")
       print("[!] Error:: Space Cant Be Empty");
       print(red + "[!] Aborting...");
       quit()     

elif userType == 4:
   Emtype = "html"
   Temp = True
   
   #Document
   print(
"""
#############################
# YOUR FILE                 #
# Put your File             #
# Into The Files Folder     #
# And Specify The Name Here #
# Example: sample.png       #
#############################
 """
   )
   userDoc = str(input("[#] File(eg: sample.png): "))
   if len(userDoc.strip()) > 0:
      verifyDOCFile = open("Files/" + userDoc.strip(),"rb")
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
                f"attachment; filename= {userDoc}",
              )
      else:
           userDocBool = None
           print(" ")
           print("[!] Error:: Please Specify A File")
           print(red + "[!] Aborting...");
           quit()
         
   else:
       userDocBool = None
       print(" ")
       print("[!] Error:: Space Cant Be Empty");
       print(red + "[!] Aborting...");
       quit()


else:
   print(" ")
   print("[!] Error:: Please choose from available list");
   print(red + "[!] Aborting...");
   quit()  

time.sleep(1)


if Temp:
  
  from Templates.templates import *
  
  #Template
  print(" ")
  print(
"""
###################
# CHOOSE TEMPLATE #
###################
 """
  )
  print(" 1: Friendly\n 2: Business\n 3: Custom ")
  userTemp = int(input("[#] Choose: "))

  #Verify Template
  if userTemp == 1:
     print(
"""
#############################
# ::LETS EDIT THE FILE::    #
#        HEADER             #
#   Title,Content..etc      #
#############################
 """
          )
     cTitl = str(input("[#] Your Title (eg: Love Letter): "))
     cSalu = str(input("[#] Your Salutation (eg: Hi Sarah,): "))
     time.sleep(1)
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
     cBody = str(input("[#] Your Message(File) (eg: sample.txt): "))
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
     cFb = str(input("[#] Facebook Link (eg: https://facebook.com/you): "))
     cTw = str(input("[#] Twitter Link (eg: https://twitter.com/you): "))
     
     if len(cTitl.strip()) > 0 and len(cSalu.strip()) > 0 and len(cBody.strip()) > 0 and len(cFb.strip()) > 0 and len(cTw.strip()) > 0:
        verifyCBodyFile = open("Templates/" + cBody.strip())
        if verifyCBodyFile is not None:
           with verifyCBodyFile as f:
               r = f.read()
               temp = friendly() %(cTitl.strip(),cSalu.strip(),r.strip(),cFb.strip(),cTw.strip())
               f.close()
        else:
           print(" ")
           print("[!] Error:: Please Specify your custom message File(.txt)")
           print(red + "[!] Aborting...");
           quit()

     else:
        print(" ")
        print("[!] Please Specify fill blank spaces")
        print(red + "[!] Aborting...");
        quit()

  elif userTemp == 2:
     print(
"""
#############################
# ::LETS EDIT THE FILE::    #
#        HEADER             #
#   Title,Content..etc      #
#############################
 """
          )
     cTitl = str(input("[#] Your Title (eg: Webinar): "))
     cSalu = str(input("[#] Your Salutation (eg: Dear members,): "))
     time.sleep(1)
     print(
"""
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
          )
     cBody = str(input("[#] Your Message(File) (eg: sample.txt): "))
     cComp = str(input("[#] Companies Name (eg: Facebook inc): "))
     cAddr = str(input("[#] Companies Address (eg: 1601 Willow Road): "))
     time.sleep(1)
     if len(cTitl.strip()) > 0 and len(cSalu.strip()) > 0 and len(cBody.strip()) > 0 and len(cComp.strip()) > 0 and len(cAddr.strip()) > 0:
        verifyCBodyFile = open("Templates/" + cBody.strip())
        if verifyCBodyFile is not None:
           with verifyCBodyFile as f:
               r = f.read()
               bBool = business
               f.close()
        else:
           print(" ")
           print("[!] Error:: Please Specify your custom message File(.txt)")
           print(red + "[!] Aborting...");
           quit()

     else:
        print(" ")
        print("[!] Please Specify fill blank spaces")
        print(red + "[!] Aborting...");
        quit()
  elif userTemp == 3:
     print(
"""
#############################
# ::CUSTOM HTML TEMPLATE::  #
# Put your Custom Template  #
# Into The Templates Folder #
# And Specify The Name Here #
# Example: sample.html      #
#############################
 """
          )
     cTemp = str(input("[#] File (eg: sample.html): "))
     if len(cTemp.strip()) > 0:
        verifyHTMLFile = open("Templates/" + cTemp.strip())
        if verifyHTMLFile is not None:
           with verifyHTMLFile as f:
               r = f.read()
               temp = customHtml() %(r.strip())
               f.close()
        else:
           print(" ")
           print("[!] Error:: Please Specify A .html File")
           print(red + "[!] Aborting...");
           quit()
     else:
        print(" ")
        print("[!] Error:: Space Cant Be Empty");
        print(red + "[!] Aborting...");
        quit()  
  else:
     print("[!] Error:: Please choose from available list");
     print(red + "[!] Aborting...");
     quit()  

time.sleep(1)
print(" ")

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

   userMassFile = str(input("[#] File(eg: sample.csv): "))
   if len(userMassFile.strip()) > 0:
      verifyCSVFile = open("Emails/" + userMassFile.strip())
      if verifyCSVFile is not None:
         userMassBool = True
      else:
         userMassBool = None
         print(" ")
         print("[!] Error:: Please Specify A .csv File")
         print(red + "[!] Aborting...")
         quit()
elif userMass == 2:
   userMassBool == None

else:
   print(" ")
   print("[!] Error:: Please choose from available list")
   print(red + "[!] Aborting...")
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
   if len(to_addrs) < 0:
      print(" ")
      print("[!] Error:: Please Specify A Recipient")
      print(red + "[!] Aborting...")
      quit()  
subject =  str(input("[*] Subject: "))

#Multipart Email Module :: Multipart("alternate")
msg = MIMEMultipart()
msg["Subject"] = subject
msg["From"] = from_name

if len(from_addr.strip()) > 0 and len(password.strip()) > 0 and len(subject.strip()) > 0:

   print("[*] Sending Mail...Please Wait...")
   
   #create a secure SSL context 
   context = ssl.create_default_context()

   try:
     with smtplib.SMTP_SSL(smtp_server, port, context=context) as server:
        server.login(from_addr, password)

        if userMassBool is not None:
           with verifyCSVFile as file:
               reader = csv.reader(file)
               next(reader)  # Skip header row
               for number,email in reader:
                  #msg["To"] = email
                  #msg["Bcc"] = email
                  # Turn these into plain/html MIMEText objects
                  if userDocBool is None:
                     if bBool is not None:
                        temp = bBool() %(cTitl.strip(),cSalu.strip(),r.strip(),cComp.strip(),cAddr.strip().replace(" ","+"),cAddr.strip(),email.strip())
                     Emtype = MIMEText(temp, Emtype)
                     msg.attach(Emtype)
                     server.sendmail(
                         from_addr,
                         email.strip(),
                         msg.as_string(),
                     )
                  else:
                     if bBool is not None:
                        temp = bBool() %(cTitl.strip(),cSalu.strip(),r.strip(),cComp.strip(),cAddr.strip().replace(" ","+"),cAddr.strip(),email.strip())
                     Emtype = MIMEText(temp, Emtype)
                     msg.attach(Emtype)
                     msg.attach(doc)
                     server.sendmail(
                         from_addr,
                         email.strip(),
                         msg.as_string(),
                     )
 
                  print(f"[*] Mail Sent To {email} ")
                  
        else:
            msg["To"] = to_addrs.strip()
            if userDocBool is None:
               if bBool is not None:
                  temp = bBool() %(cTitl.strip(),cSalu.strip(),r.strip(),cComp.strip(),cAddr.strip().replace(" ","+"),cAddr.strip(),to_addrs.strip())
               Emtype = MIMEText(temp, Emtype)
               msg.attach(Emtype)
               server.sendmail(
                   from_addr,
                   to_addrs.strip(),
                   msg.as_string(),
               )
            else:
               if bBool is not None:
                  temp = bBool() %(cTitl.strip(),cSalu.strip(),r.strip(),cComp.strip(),cAddr.strip().replace(" ","+"),cAddr.strip(),to_addrs.strip())
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
   finally:
       quit()

else:
     print(" ")
     print("[!] Error:: Space(s) Cant Be Empty")
     print(red + "[!] Aborting...\n")
     quit()
