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
<body style="background-image: linear-gradient(rgba(77,96,224,.6), rgba(0,0,0,.8)), url('https://cdn.pixabay.com/photo/2013/07/18/20/26/boat-164989_960_720.jpg');background-size:cover;background-repeat: no-repeat;background-attachment: fixed;margin:0;padding:10px;">
<div class="container" style="position:relative;margin:auto;border-radius:10px;width:500px;font-family:'Amaranth',sans-serif;">
<div class="header" style="position:relative;text-align:center;padding:20px;color:#fff;border-radius:10px 10px 0 0;background-color:#0cbfdc;font-weight:bold;font-size:20px;">
%s
</div>
<div class="content" style="position:relative;padding:10px;font-family:'Amaranth',sans-serif;color:#08eae0;border-top:none;border-bottm:none;border-left:solid 1px #0cbfdc;border-right:solid 1px #0cbfdc;">
<p class="salutation" style="font-weight:bold;font-size:20px;">
%s
</p>
<p class="body" style="font-size:16px;position:relative;">
%s
</p>
</div>
<div class="footer" style="position:relative;text-align:center;padding:20px;color:#fff;border-radius:0 0 10px 10px;background-color:#0cbfdc;">
<span style="font-size:20px"><b>SOCIAL</b></span><br />
<span><a style="color:#fff" href="%s">facebook</a>&nbsp;<a style="color:#fff" href="%s">twitter</a></span>
</div>
</div>
</body>
   """
   return friendly

def business():
   business = """\
<body style="background-image: linear-gradient(rgba(77,96,164,.6), rgba(0,0,0,.8)), url('https://cdn.pixabay.com/photo/2019/04/06/15/28/business-4107640_960_720.jpg');background-size:cover;background-repeat: no-repeat;background-attachment: fixed;margin:0;padding:10px;">
<div class="container" style="position:relative;margin:auto;border:solid 1px #fff;border-radius:10px;width:500px;">
<div class="header" style="position:relative;text-align:center;padding:20px;color:#423c3c;border-radius:10px 10px 0 0;font-weight:bold;font-size:19px;background-color:#fff;">
<img src="https://pixabay.com/apple-touch-icon.png" width="50px"><br/>
<b>%s</b>
</div>
<div class="content" style="position:relative;padding:10px;font-family:'Amaranth',sans-serif;color:#0b91e0;">
<p class="salutation" style="font-weight:bold;font-size:18px;">
%s
</p>
<p class="body" style="font-size:17px;position:relative;line-height:1.6em">
%s
</p>
</div>
<div class="footer" style="position:relative;text-align:justify;padding:20px;color:#423c3c;border-radius:0 0 10px 10px;background-color:#fff;font-size:12px">
<p> 
&copy; %s, <a style="color:dodgerblue" href="https://maps.google.com/?q=%s"> %s </a>
</p>
<p>This message was sent to you and intended for you only.</p>
</div>
</div>
</body>
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
