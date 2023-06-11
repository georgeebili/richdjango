"""
The Assemble component is a center of importing library, framework and other independent component that
we will be using all across our application.
"""
import time
import os
from django.shortcuts import render
from django.http import HttpResponseRedirect, HttpResponse, JsonResponse, HttpRequest

#from richdjango.models import 

from pathlib import Path
# for building like DIR_Path / 'subdir'.
AppDirectory = Path(__file__).resolve().parent.parent
MediaDirecory = AppDirectory / 'cdn' / 'resources'
#MediaDirecory = AppDirectory.parent / 'accounting-app.errorcake.com' / 'cdn' / 'resources'

from .DarkArt.MagicBox import (MultipleRequestPostText, ReplaceTOHtmlCharacter,
    ReverseReplaceTOHtmlCharacter, ArrayDBData, ListDBData, UploadFileHandler,
    ConvertDBDataTOArray, ConvertDBDataTOList, GetDictKey
)

