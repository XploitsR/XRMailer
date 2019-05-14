######################################################################
# Copyright (c). All rights reserved                                 #
# GNU GENERAL PUBLIC LICENSE                                         #
# Version 3, 29 June 2007                                            #
#                                                                    #
# Coded by Solomon Narh (::XploitsR Author::)                        #
# Github: https://github.com/XploitsR/XRSmtp                         #
# Facebook: https://facebook.com/RXploits                            #
# Twitter: https://twitter.com/RXploits                              #
# Telegram: https://t.me/RXploits                                    #
# Website: https://xploitsr.tk                                       #
#                                                                    #
#             ::PERSONAL ME::                                        #
# Github: https://github.com/Solomon97062                            #
# Facebook: https://facebook.com/solomon.narh.311                    #
# Twitter: https://twitter.com/Solomon97062                          #
# Instagram: @_xploitsr_author_1                                     #
# Email: solomonnarh97062@gmail.com                                  #
######################################################################

#=begin == 
"""""""""""""""""""""""""""""""""""""""""
XRSmtp is a module to auto fetch any smtp 
server details by just knowing the smtp 
providers name.
"""""""""""""""""""""""""""""""""""""""""
#=define class == 
class XRSmtp:
  #SSL port
  def smtp_portSSL(self,provider):
      port =  465
      try:
        if str(provider) is not None and len(str(provider)) > 0 and type(provider) == str:
           if str(provider.lower()) == "gmail":
              server,port = "smtp.gmail.com",port
           elif str(provider.lower()) == "yahoo":
              server,port = "smtp.mail.yahoo.com",port
           elif str(provider.lower()) == "outlook":
              server,port = "smtp-mail.outlook.com",port
           elif str(provider.lower()) == "hotmail":
              server,port = "smtp.live.com",port
           elif str(provider.lower()) == "office365":
              server,port = "smtp.office365.com",port
           elif str(provider.lower()) == "aim":
              server,port = "smtp.aim.com",port
           elif str(provider.lower()) == "yandex":
              server,port = "smtp.yandex.com",port
           else:
              print("[!] SMTP provider not found")
              print("[+] Make custom using smtp_customSmtp(smtp_server)")
              print("[+] Make custom using smtp_customPort(port)")
              quit()
        else:
           print("[!] Don't be silly, str() expected")
           quit()
      except:
        raise
        quit()
      return [server,port]
  #TLS port
  def smtp_portTLS(self,provider):
      port = 578
      try:
        if str(provider) is not None and len(str(provider)) > 0 and type(provider) == str:
           if str(provider.lower()) == "gmail":
              server,port = "smtp.gmail.com",port
           elif str(provider.lower()) == "yahoo":
              server,port = "smtp.mail.yahoo.com",port
           elif str(provider.lower()) == "outlook":
              server,port = "smtp-mail.outlook.com",port
           elif str(provider.lower()) == "hotmail":
              server,port = "smtp.live.com",port
           elif str(provider.lower()) == "office365":
              server,port = "smtp.office365.com",port
           elif str(provider.lower()) == "aim":
              server,port = "smtp.aim.com",port
           elif str(provider.lower()) == "yandex":
              server,port = "smtp.yandex.com",port
           else:
              print("[!] SMTP provider not found")
              print("[+] Make custom using smtp_customSmtp(smtp_server)")
              print("[+] Make custom using smtp_customPort(port)")
              quit()
        else:
           print("[!] Don't be silly, str() expected")
           quit()
      except:
        raise
        quit()
      return [server,port]

