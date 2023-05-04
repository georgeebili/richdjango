from django.db import models
import django.utils.timezone
#date = models.DateField(auto_created=True, default=django.utils.timezone.localtime)
#time = models.TimeField(auto_created=True, default=django.utils.timezone.localtime)
# firstLogin = models.BooleanField(default=True)

class IDManager(models.Model):
    value = models.TextField(default="")
    name = models.TextField(default="")
    def __str__(self):
        return f"{{'value':'''{self.value}''', 'name':'''{self.name}'''}}"

class App(models.Model):
    username = models.TextField(default="admin")
    password = models.TextField(default="pass")
    name = models.TextField(default="Admin")
    session = models.TextField(default="0.0")
    email = models.EmailField(default="", max_length=50)
    def __str__(self):
        return f"{{'username':'''{self.username}''' , 'password':'''{self.password}''',\
            'name':'''{self.name}''', 'session':'''{self.session}''', 'email':'''{self.email}'''}}"
