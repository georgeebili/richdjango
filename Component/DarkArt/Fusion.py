from richdjango.models import IDManager
from typing import Union, List
from django.db.models.manager import BaseManager
from .MagicBox import ArrayDBData, ReverseReplaceTOHtmlCharacter, ListDBData
MASTER_TYPE = Union[IDManager, IDManager]

class ModelFuseType(BaseManager):
    def __init__(self, *args, **kwargs) -> BaseManager:...
    class cooks:
        #def filters(*args, **kwargs) -> BaseManager:...
        def get(*args, **kwargs) -> MASTER_TYPE:...
        #def complex_filter(*args, **kwargs) -> Union[MODEL_TYPE, useful]:...
    objects: Union[BaseManager, cooks] = cooks
    def save(): ...

class Fuse(object):
    """
    Fuse is a component that interact with django database models for simple and efficent actions.
    """
    def __init__(self, FuseTable: ModelFuseType) -> None:
        self.fuseTable: ModelFuseType = FuseTable #"Package"
        self.fieldKeyList = list(self.fuseTable.__dict__.keys())
        self.exceptionFieldKeys = ["objects", "id", "MultipleObjectsReturned", "DoesNotExist", "__module__","__str__","__doc__", "_meta"]
        self.fieldKeyWordExceptions = ["get_next_by", "get_previous_by"]
        for field in self.fieldKeyList:
            if field in self.exceptionFieldKeys:
                self.fieldKeyList.remove(field)
            else:
                for avoid in self.fieldKeyWordExceptions:
                    if field.startswith(avoid):
                        self.fieldKeyList.remove(field)
        for i in self.fieldKeyList:
            self.__setattr__(i, None)
        self.bodyField: BaseManager = None
        self.bodyFields: BaseManager = None
        self.isFuseConnected = False
        self.__dbName = FuseTable.__name__ #"Package"
        self.__connectionField = ""
        self.__connectionValue = ""
        self.field: MASTER_TYPE = self

    def connect(self, field, value, additional={}):
        query = {f"{field}": value}
        query.update(additional)
        item = self.fuseTable.objects.complex_filter(query)
        if item.exists():
            if item.count() == 1:
                self.__connectionField = field
                self.__connectionValue = value
                self.bodyFields = item
                self.isFuseConnected = True
                self.bodyField = item
                arrayData: dict = self.getArray()
                for i in arrayData.keys():
                    self.__setattr__(i, arrayData[i])
                return self
            else:
                self.__connectionField = field
                self.__connectionValue = value
                self.isFuseConnected = True
                self.bodyField = None
                self.bodyFields = item
                for i in self.fieldKeyList:
                    self.__setattr__(i, None)
                return self
            
        for i in self.fieldKeyList:
            self.__setattr__(i, None)
        self.isFuseConnected = False
        self.bodyField = None
        self.bodyFields = None
        return self
    
    def getArray(self):
        if self.bodyField:
            data = ArrayDBData(self.bodyField, self.__dbName)
            for key in data.keys():
                data[key] = ReverseReplaceTOHtmlCharacter(data[key])
            return data
        return {}
    
    def getListOfArray(self) -> List[dict]:
        if self.bodyFields:
            datas = ListDBData(self.bodyFields, self.__dbName)
            for i in range(len(datas)):
                item: dict = datas[i]
                for key in item.keys():
                    item[key] = ReverseReplaceTOHtmlCharacter(item[key])
                datas[i] = item
            return datas
        return []
    
    def updateField(self, isConnected=True, connect: dict={}, fields: dict ={}):
        """
        Function for updating a table in the database.
        1. fields parameter, should contain data that are to be stored in the database table in dictionary form.
        Example {"dbcolumn": "value to set on the column"}, {"userID": value, "firstName": value}.
        2. connet parameter, should contain data that will be used for creating connection with the database table.
        Example {"id": 1}. Note that isConnected parameter has to be set to False.
        3. isConnected parameter, must contain a boolean value which decides either to use existing connection details for
        creating a new connection to the database table in other to update fields. 
        """
        keys = list(fields.keys())
        # ensure all field are contain in the main table fields(self.fieldKeys)
        for key in keys:
            if key not in self.fieldKeyList: return False
        
        connectKey = list(connect.keys())
        # ensure connection field are contain in the main table fields(self.fieldKeys)
        for key in connectKey:
            if key not in self.fieldKeyList: return False

        if isConnected and keys and self.isFuseConnected:
            updater = self.fuseTable.objects.get(**{self.__connectionField: self.__connectionValue})
            for key in keys:
                updater.__dict__[key] = fields[key]
                self.__setattr__(key, fields[key])
            updater.save()
            return True
        elif not isConnected and connectKey:
            connectKey = connectKey[0]
            connectValue = connect[connectKey]
            updater = self.fuseTable.objects.get(**{connectKey: connectValue})
            for key in keys:
                updater.__dict__[key] = fields[key]
                self.__setattr__(key, fields[key])
            updater.save()
            return True
        return False
    
    def createNewField(self, fields: dict ={}):
        keys = list(fields.keys())
        # ensure all field are contain in the main table fields(self.fieldKeys)
        for key in keys:
            if key not in self.fieldKeyList:
                return False
        newColumn = self.fuseTable(**fields)
        newColumn.save()
        return True

    def all(self) -> List[dict]:
        items = self.fuseTable.objects.all()
        if items.count():
            datas = ListDBData(items, self.__dbName)
            for i in range(len(datas)):
                item: dict = datas[i]
                for key in item.keys():
                    item[key] = ReverseReplaceTOHtmlCharacter(item[key])
                datas[i] = item
            return datas
        return []
 