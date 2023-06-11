# -*- coding: utf-8 -*-
"""
Created on Sat Mar 12 16:28:54 2022

@author: George

Manage all email logic
"""

from .DarkArt.EmailTool import EmailApp

class Emailer(EmailApp):
    """ Manage all email activities"""
    def __init__(self, request):
        super().__init__(request)
          
    def sendEmailVerification(self, userID, email: str, emailpin: str):
        #print(self.MY_URL+"/verify/"+user_id+"/"+emailpin)
        title = ""
        message = ""
        self.sendMail(subject=title, email=email, messageBody=message)
        
    def sendPasswordResetMail(self, email, passwordResetValue):
        #print(self.MY_URL+"/resetpassword/"+rpv)
        title = ""
        message = ""
        self.sendMail(subject=title, email=email, messageBody=message)

    def otpMail(self, otp, email):
        subject = 'Accounting App - One time password'
        message = 'Your Accounting App OTP.'
        print("error in sending otp")
        self.sendMail(subject=subject, email=email, messageBody=message)





