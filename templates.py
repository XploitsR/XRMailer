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
# Twitter: https://twitter.com/solomon97062                          #
# Instagram: @_xploitsr_author_1                                     #
# Email: solomonnarh97062@gmail.com                                  #
######################################################################

####################################
#	XploitsR Templates	   #
####################################

def friendly():
   friendly = """\
<!doctype html>
<html>
<head>
<meta http-equiv="Content-Type" content="text/html">
</head>
<body style="background-image: linear-gradient(rgba(77,96,164,.6), rgba(0,0,0,.8)), url('https://cdn.pixabay.com/photo/2019/04/05/17/51/forest-4105676_960_720.jpg');background-size:cover;background-repeat: no-repeat;background-attachment: fixed;margin:0;padding:10px;">
<div class="container" style="position:relative;margin:auto;border:solid 1px #fff;border-radius:10px;width:500px;font-family:'Amaranth',sans-serif;">
<div class="header" style="position:relative;text-align:center;padding:20px;color:#fff;border-radius:10px 10px 0 0;background-color:#636a7f;font-weight:bold;font-size:20px;">
%s
</div>
<div class="content" style="position:relative;padding:10px;font-family:'Amaranth',sans-serif;color:#5d5858;color:#fff;">
<p class="salutation" style="font-weight:bold;font-size:20px;">
%s
</p>
<p class="body" style="font-size:16px;position:relative;">
%s
</p>
</div>
<div class="footer" style="position:relative;text-align:center;padding:20px;color:#fff;border-radius:0 0 10px 10px;background-color:#636a7f;">
<span style="font-size:20px"><b>SOCIAL</b></span><br />
<span><a style="color:#fff" href="%s">Facebook</a>&nbsp;<a style="color:#fff" href="%s">Twitter</a></span>
</div>
</div>
</body>
</html>
   """
   return friendly

def business():
   business = """\
<!doctype html>
<html>
<head>
<meta http-equiv="Content-Type" content="text/html">
</head>
<body style="background-image: linear-gradient(rgba(77,96,164,.6), rgba(0,0,0,.8)), url('https://cdn.pixabay.com/photo/2019/04/06/15/28/business-4107640_960_720.jpg');background-size:cover;background-repeat: no-repeat;background-attachment: fixed;margin:0;padding:10px;">
<div class="container" style="position:relative;margin:auto;border:solid 1px #fff;border-radius:10px;width:500px;">
<div class="header" style="position:relative;text-align:center;padding:20px;color:#423c3c;border-radius:10px 10px 0 0;font-weight:bold;font-size:19px;background-color:#fff;">
<img src="https://xploitsr.tk/assets/csxp_img/logo/icon.png" width="50px"><br/>
<b>%s</b>
</div>
<div class="content" style="position:relative;padding:10px;font-family:'Amaranth',sans-serif;color:#5d5858;color:#fff;">
<p class="salutation" style="font-weight:bold;font-size:18px;">
%s
</p>
<p class="body" style="font-size:17px;position:relative;">
%s
</p>
</div>
<div class="footer" style="position:relative;text-align:justify;padding:20px;color:#423c3c;border-radius:0 0 10px 10px;background-color:#fff;font-size:12px">
<p> 
&copy; %s, <a style="color:dodgerblue" href="https://maps.google.com/?q=%s"> %s </a>
</p>
<p>This message was sent to %s and intended for you.</p>
</div>
</div>
</body>
</html>
   """
   return business

def customHtml():
    customHtml = """\
%s

"""
    return customHtml

def customText():
    customText = """\
%s

"""
    return customText
