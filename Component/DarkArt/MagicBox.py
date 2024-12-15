"""
Usage:
"""
import typing
#from django.core.validators import validate_email
import re
import os

def MultipleRequestPostText(request, fields=[], reactiveFunc=None) -> typing.List[str]:
	data = []
	for fid in fields:
		item = request.POST[fid]
		if reactiveFunc:
			item = reactiveFunc(item)
		data.append(item)
	return data

def ReplaceTOHtmlCharacter(mydata):
    """Covert raw character to html type"""
    return str(mydata).replace('&','&amp;').replace("'",'&apos;').replace('"','&quot;').replace("\\","&bsol;").replace("\r","").replace("\n","&#10;").replace(">","&gt;").replace("<","&lt;")

def ReverseReplaceTOHtmlCharacter(mydata):
    """ Convert html type of data to raw character"""
    return str(mydata).replace('&amp;', '&').replace('&apos;', "'").replace('&quot;', '"').replace("&bsol;", "\\").replace("&#10;", "\n").replace("&gt;", ">").replace("&lt;", "<")

def ConvertDBDataTOArray(db_data, classname):
    st1 = str(db_data).replace("<QuerySet", "{'QuerySet':").replace("<"+classname+":", "").replace("']>","']").replace(">","}")
    return eval(st1)
    
def ConvertDBDataTOList(db_data, classname):
    data = eval(str(list(db_data)).replace(
        "<QuerySet", "{'QuerySet':").replace("<"+classname+":", "").replace("']>","']").replace(">","}"))
    return data
    
def GetDictKey(dict):
    list = []
    for key in dict.keys():
        list.append(key)
    return list

def ArrayDBData(db_data, classname) -> dict:
    prepareString = str(db_data).replace("<QuerySet", "{'QuerySet':").replace("<"+classname+":", "").replace("]>","]}").replace(">","")
    evalString = eval(prepareString)
    return evalString['QuerySet'][0]

def ListDBData(db_data, classname):
    prepareString = str(list(db_data)).replace("<QuerySet", "{'QuerySet':").replace("<"+classname+":", "").replace("]>","]}").replace(">","")
    evalString = eval(prepareString)
    return evalString
    
def UploadFileHandler(file, filename: str, fileUploadPath: str):
    """	where f is the file posted, example request.FILES['img'], \
    	filename is either the name of the file posted or a new name that we like and \
        fileUploadPath is the system location to store the file.
    """
    filePath = os.path.join(fileUploadPath, filename)
    try:
        with open(filePath, 'wb+') as destination:
            for chunk in file.chunks():
                destination.write(chunk)
        return True
    except:
        return False

def DeleteFile(filePath: str) -> bool:
    try:
        os.remove(filePath)
        return True
    except:
        return False


def isUrlDetected(text):
    url_pattern = re.compile(
        r'((http|https|ftp)://)?'  # Optional scheme
        r'((([a-zA-Z0-9_-]+\.)+[a-zA-Z]{2,6})'  # Domain
        r'|localhost|'  # or localhost
        r'(\d{1,3}\.){3}\d{1,3}|'  # or IPv4
        r'\[?[A-F0-9]*:[A-F0-9:]+\]?)'  # or IPv6
        r'(:\d+)?'  # Optional port
        r'(/[-a-zA-Z0-9@:%_\+.~#?&//=]*)?'  # Path
    )
    class _UrlDetail:
        urls = url_pattern.findall(text)
        urlFound = url_pattern.findall(text).__len__() > 0
        length = url_pattern.findall(text).__len__()
    return _UrlDetail

__symbols__ = ['~','`','!','@','#','$','%','^','&','*','(',')',
    '_','+','=','-','{','}','\\','|',':','"',';','<','>','?',
    '.',',',"'",'/'
]

def isTextLengthValid(text: str, wordMinLenght=1, wordMaxLenght=1,
        minLength=1, maxLength=15):
    cleanText = text.strip()
    if cleanText.__len__() > maxLength: return False
    if cleanText.__len__() < minLength: return False
    if cleanText.split(' ').__len__() > wordMaxLenght: return False
    if cleanText.split(' ').__len__() < wordMinLenght: return False
    return True

def isNameFieldValid(text: str, wordMinLenght=1, wordMaxLenght=1,
        minLength=1, maxLength=15, exceptCharacter=[]):
    
    # check text length
    if not isTextLengthValid(
        text, wordMinLenght, wordMaxLenght, minLength, maxLength):
        return False
    
    # check is number in text
    numbers = ['1','2','3','4','5','6','7','8','9','0'] 
    nums = [n for n in numbers if not exceptCharacter.__contains__(n)]
    for n in nums:
        if n in text: return False

    # check is symbol in text
    _symbols = [ x for x in __symbols__ if not exceptCharacter.__contains__(x) ]
    for s in _symbols:
        if s in text: return False
    
    return True
    
def isNumberOnlyFieldValid(text: str, minLength=1, maxLength=15, exceptCharacter=[], strict=False):
    smallLetters = 'abcdefghijkLmnopqrstuvwxyz'
    capsLetters = 'ABCDEFGHIJKLMNOPQRSTUVWXYZ'
    # symbols #.+
    # check small Letters in text
    for l in smallLetters:
        if l in text: return False
    # check caps Letters in text
    for cL in capsLetters:
        if cL in text: return False

    # check if symbol in text
    _symbols = [ x for x in __symbols__ if not exceptCharacter.__contains__(x) ]
    for s in _symbols:
        if s in text: return False

    # check text length
    if not isTextLengthValid(text, 1, 1, minLength, maxLength): return False

    if strict:
        try:
            if int(text): pass
        except:
            return False

    return True
    

