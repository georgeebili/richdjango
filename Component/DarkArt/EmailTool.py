# -*- coding: utf-8 -*-
"""
Created on Wenesday May 4, 16:28:54 2023

@author: George

Manage all email logic
"""

from richdjango.settings import EMAIL_HOST_USER
from django.core import mail
from django.template.loader import render_to_string
from django.utils.html import strip_tags

class EmailApp(object):
    """ Manage all email activities"""
    def __init__(self, request):
        #initialize
        self.request = request
        #self.MY_URL =  request.get_raw_uri().split(':')[0]+"://"+request._get_raw_host()
        self.domainName = request.META.get('HTTP_HOST')
        self.protocal = request.META.get('wsgi.url_scheme')
        self.siteURL = self.protocal + '://' + self.domainName
        self.fromEmail = EMAIL_HOST_USER
        self.overrideDomainCheck = False
        self.tempLocal = 'mail/'

    def isLocalServerCheck(self):
        if '127.0.0.1' in self.domainName or 'localhost' in self.domainName:
            print("local host detected on sending email!")
            if self.overrideDomainCheck:
                print("localhost byPassed!")
                return not self.overrideDomainCheck
            return not self.overrideDomainCheck
        return self.overrideDomainCheck
        
    def sendMail(self, subject, email, messageBody="", isHtml=False):
        if self.isLocalServerCheck(): return
        plain_message = strip_tags(messageBody)
        toEmail = email
        if isHtml:
            result = mail.send_mail(subject, plain_message, self.fromEmail, [toEmail],
                html_message=messageBody,
                fail_silently = False
            )
        else:
            result = mail.send_mail(subject, messageBody, self.fromEmail, [toEmail],
                fail_silently = False
            )
        return result
    
    def sendHtmlMail(self, title, emailAddress, htmlFileName, fileAttributes={}):
        # check if the html file is in th mail folder of templates
        html_message = render_to_string(f'{self.tempLocal}{htmlFileName}', fileAttributes)
        return self.sendMail(title, emailAddress, html_message, True)
        
    def test(self, email=""):
        subject = 'Test Mail'
        message = 'This is just a test mail.'
        
        html_message = render_to_string(f'{self.tempLocal}test.html', 
            {'context': message, "myurl":self.siteURL}
        )
        return self.sendMail(subject, html_message, email, True)
        
