from django.db import models
import django.utils.timezone
#date = models.DateField(auto_created=True, default=django.utils.timezone.localtime)
#time = models.TimeField(auto_created=True, default=django.utils.timezone.localtime)
# firstLogin = models.BooleanField(default=True)

class IDManager(models.Model):
    value = models.TextField(default="")
    name = models.TextField(default="")
    def __str__(self):
        items = self.__dict__
        if items.__contains__('_state'): del items['_state']
        for i in items.keys():
            if type(items[i]) is not bool: items[i] = str(items[i])
        return str(items)

class App(models.Model):
    username = models.TextField(default="admin")
    password = models.TextField(default="pass")
    name = models.TextField(default="Admin")
    session = models.TextField(default="0.0")
    email = models.EmailField(default="", max_length=50)
    def __str__(self):
        items = self.__dict__
        if items.__contains__('_state'): del items['_state']
        for i in items.keys():
            if type(items[i]) is not bool: items[i] = str(items[i])
        return str(items)