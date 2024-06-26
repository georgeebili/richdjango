# -*- coding: utf-8 -*-
"""
Created on Sat Mar 12 16:28:54 2022

@author: George

Manage all email logic
"""

from .DarkArt.EmailTool import EmailApp
from django.http import HttpRequest

class Emailer(EmailApp):
    """ Manage all email activities"""
    def __init__(self, request: HttpRequest):
        super().__init__(request)
          
    def sendEmailVerification(self, userID: str, email: str, emailpin: str):
        #print(self.siteURLL+"/verify/"+user_id+"/"+emailpin)
        title = ""
        message = ""
        self.sendMail(subject=title, email=email, messageBody=message)
        
    def sendPasswordResetMail(self, email: str, passwordResetValue: str):
        #print(self.siteURL+"/resetpassword/"+rpv)
        title = ""
        message = ""
        self.sendMail(subject=title, email=email, messageBody=message)

    def otpMail(self, otp, email):
        subject = 'App - One time password'
        message = 'Your App OTP.'
        print("error in sending otp")
        self.sendMail(subject=subject, email=email, messageBody=message)





