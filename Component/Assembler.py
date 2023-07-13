"""
The Assemble component is a center of importing library, framework and other independent component that
we will be using all across our application.
"""
import time
import os
from django.shortcuts import render
from django.http import HttpResponseRedirect, HttpResponse, JsonResponse, HttpRequest

# Django time customization
from richdjango.production import DjangoTime

# Email component
from Component.EmailUserApp import Emailer

# Application Directory path
from richdjango.production import AppDirectory, MediaDirecory

# Import component that is responsible for creating unique IDs
from Component.IDHandler import UniqueIDApp, DeleteID

from Component.DarkArt.MagicBox import (MultipleRequestPostText, ReplaceTOHtmlCharacter,
    ReverseReplaceTOHtmlCharacter, ArrayDBData, ListDBData, UploadFileHandler,
    ConvertDBDataTOArray, ConvertDBDataTOList, GetDictKey, DeleteFile
)
