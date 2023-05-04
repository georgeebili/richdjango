"""
Usage:
"""
import typing

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
    import os
    filePath = os.path.join(fileUploadPath, filename)
    try:
        with open(filePath, 'wb+') as destination:
            for chunk in file.chunks():
                destination.write(chunk)
        return True
    except:
        return False
