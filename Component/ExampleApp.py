# -*- coding: utf-8 -*-
"""
Created on Mon May 31 01:51:09 2021

@author: George

Example of SignUp component.
"""

#Importing External Apps
from Component.Assembler import (ReplaceTOHtmlCharacter, render, 
    HttpResponseRedirect,  MultipleRequestPostText,
    UniqueIDApp, HttpResponse, HttpRequest, Emailer,
    UploadFileHandler, MediaDirecory # ClientDBFuse,
)


class ExampleSignUp(object):
    def __init__(self, request: HttpRequest):
        """Request parameter from view is passed here."""
        #initialize
        self.request = request
        self.emailApp = Emailer(self.request)
        self.cookie: str = request.META.get('CSRF_COOKIE')
        #self.access = ClientAccess(request)
        # Unique ID components
        self.uniqueID = UniqueIDApp()
        self.context = {
            "error": {
                "message":"Email Already Exist!!!",
                "className":"by-gap by-space bg-red c-white",
                "user": {
                    "create": {
                        'email': 'Email address already exist.',
                        'phoneNumber': 'Phone number already exist.'
                    }
                }
            },
            "title": "Example Title",
            "desc": "Example signup page description",
            "siteUrl": self.emailApp.siteURL
        }
       # self.clientFuse = ClientDBFuse()
        self.tempdir = 'user/'
        self.headurl = ''
        self.signupLink = self.headurl + "/signup"
        self.dashboardLink = self.headurl + "/home"
        self.signupPageFile = self.tempdir + "example-signup.html"

    def signup(self): 
        if self.request.method == "POST":
            # capture the posted data
            firstname, lastname, phoneNumber, emailAddress, password = MultipleRequestPostText(self.request,
                    ['firstname', 'lastname', 'phonenumber', 'email', 'password'], ReplaceTOHtmlCharacter)
            dbFields = ['firstName', 'lastName', 'phoneNumber', 'email', 'password']
            dbValues = [firstname, lastname, phoneNumber, emailAddress, password]

            # check if email address already exist in the app b4 completing the registration
            """
            self.clientFuse.connect("email", emailAddress)
            if self.clientFuse.isFuseConnected or not emailAddress:
                self.context["isEmailError"] = True
                return render(self.request, self.signupPageFile, self.context)
            
            # check if phone number already exist in the app b4 completing the registration
            clit = ClientDBFuse().connect("phoneNumber", phoneNumber)
            if clit.isFuseConnected or not phoneNumber:
                self.context["isPhoneNumberError"] = True
                return render(self.request, self.signupPageFile, self.context)
            
            # check if an account already exist with the same cookies
            if self.clientFuse.connect("session", self.cookie).isFuseConnected or not password:
                # only bot can do this
                return HttpResponse("Process End, hahaha er caught you.")
            """
            # get profile pics file
            newProfilePicsFileName = ''
            if self.request.FILES.__contains__('image'):
                proofFile = self.request.FILES['image']
                fileID = self.uniqueID.file()
                extention = str(proofFile.name).split('.')[-1]
                newProfilePicsFileName = fileID + '.' + extention
                # save file
                UploadFileHandler(proofFile, newProfilePicsFileName, MediaDirecory)
                
            # create a unique user id and email verification code
            emailPin, userID = "1234", "1" #self.uniqueID.emailPin(), self.uniqueID.client()    
            allFields = dbFields + ["uniqueID", "emailVerificationValue", "session", 'profilePics']
            allValues = dbValues + [userID, emailPin, self.cookie, newProfilePicsFileName]
            
            arrangedFields = dict(zip(allFields, allValues))
            
            # Save the user data on the database
            """
            if self.clientFuse.createNewField(arrangedFields):
                self.clientFuse.connect('uniqueID', userID)
                if self.clientFuse.isFuseConnected:
                    pass
                pass
            """
            
            # send verification email
            # self.emailApp.sendEmailVerification(userID, emailAddress, emailPin)
            
            return HttpResponseRedirect(self.dashboardLink)

        elif self.request.method == "GET":
            """ self.clientFuse.connect("session", self.cookie)
            if self.clientFuse.isFuseConnected:
                return HttpResponseRedirect(self.dashboardLink)
            """
        return render(self.request, self.signupPageFile,  self.context)


# Usage in views.py

