# -*- coding: utf-8 -*-
"""
Created on Sun May  1 22:47:48 2022

@author: George

For managing and handling of I.D for the app
"""
from richdjango.models import IDManager
from random import choice

class IDApp():
    def __init__(self):
        self.numbers = "01234567890"
        self.capitalLetters = "ABCDEFGHIJKLMNOPQRSTUVWXYZ"
        self.smallLatters = "abcdefghijklmnopqrstuvwxyz"
        self.allLetters = "abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ"
        self.combination = "0aA1bB2cC3dD4eE5fF6gG7hH8iI9jJ0kK1lL2mM3nN4oO5pP6qQ7rR8sS9tT0uU1vV2wW3xX4yY5zZ"
    
    def checkID(self, typ, new_gen_id):
        record = IDManager.objects.filter(value = new_gen_id)
        if not record.exists():
            idm = IDManager(value=new_gen_id, name=typ)
            idm.save()
            return True
        return False
    
    def sc(self, value=[]):
        if len(value): return str(choice(value))
        characterList = [1,2,3]
        rainbowChoice = choice(characterList)
        if rainbowChoice == 1: return choice(self.numbers)
        elif rainbowChoice == 2: return choice(self.capitalLetters)
        else: return choice(self.allLetters)
    
    def guess(self, which="number", by=1):
        """
        This function will help pick/arrange the characters that will form the ID.
        which: this parameter will decide what type of charater will be used,
        when assembling the ID. By defualt is number, which means it return a string
        containing only numbers. this parameter values are "combine" or "number"
        or "all-letter" or "small-letter" or "capital-letter".
        by: this parameter will determine how many charater will be returned as the ID value.
        """
        idCharaters = ""
        if which == "number":
            for i in range(by): idCharaters += choice(self.numbers)
        elif which == "all-letter":
            for i in range(by): idCharaters += choice(self.allLetters)
        elif which == "small-letter":
            for i in range(by): idCharaters += choice(self.smallLatters)
        elif which == "capital-letter":
            for i in range(by): idCharaters += choice(self.capitalLetters)
        elif which == "combine":
            for i in range(by): idCharaters += choice(self.combination)
        else:
            for i in range(by): idCharaters += choice(self.combination)
        return idCharaters

    def deleteFromIDManager(self, value, name=""):
        record = IDManager
        if name:
            record = IDManager.objects.filter(value = value, name=name)
        else:
            record = IDManager.objects.filter(value = value)
        if record.exists():
            record.delete()

