from richdjango.models import IDManager
from typing import Union, List
from django.db.models.manager import BaseManager
from .MagicBox import ArrayDBData, ReverseReplaceTOHtmlCharacter, ListDBData
#from datetime import datetime
from datetime import datetime, date, time
import re
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
        self.exceptionFieldKeys = ["objects", "MultipleObjectsReturned", "DoesNotExist", "__module__","__str__","__doc__", "_meta"] #"id",
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
        self.query = {}
        self.field: MASTER_TYPE = self

    def connect(self, field, value, additional={}):
        self.query = {f"{field}": value}
        self.query.update(additional)
        item = self.fuseTable.objects.complex_filter(self.query)
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
        self.query = {}
        return self
    
    def convert_to_date_time(self, value: str):
        formats = [
            (r"^\d{4}-\d{2}-\d{2} \d{2}:\d{2}:\d{2}\.\d+$", "%Y-%m-%d %H:%M:%S.%f", datetime),
            (r"^\d{4}-\d{2}-\d{2} \d{2}:\d{2}:\d{2}$", "%Y-%m-%d %H:%M:%S", datetime),
            (r"^\d{4}-\d{2}-\d{2}$", "%Y-%m-%d", date),
            (r"^\d{2}:\d{2}:\d{2}\.\d+$", "%H:%M:%S.%f", time),
            (r"^\d{2}:\d{2}:\d{2}$", "%H:%M:%S", time),
            (r"^\d{4}-\d{2}-\d{2} \d{2}:\d{2}:\d{2}\.\d+\+\d{2}:\d{2}$", "%Y-%m-%d %H:%M:%S.%f%z", datetime)
        ]
        
        for regex, fmt, fmt_type in formats:
            if re.match(regex, value):
                try:
                    dt = datetime.strptime(value, fmt)
                    if fmt_type == datetime:
                        return dt
                    elif fmt_type == date:
                        return dt.date()
                    elif fmt_type == time:
                        return dt.time()
                except ValueError:
                    continue
        return value
    
    def getArray(self):
        if self.bodyField:
            data = ArrayDBData(self.bodyField, self.__dbName)
            for key in data.keys():
                if key.__contains__('time') or key.__contains__('date'):
                    data[key] = self.convert_to_date_time(data[key])
                if type(data[key]) not in [bool, int, float, datetime, time, date]:
                    data[key] = ReverseReplaceTOHtmlCharacter(data[key])
            return data
        return {}
    
    def getListOfArray(self) -> List[dict]:
        if self.bodyFields:
            datas = ListDBData(self.bodyFields, self.__dbName)
            for i in range(len(datas)):
                item: dict = datas[i]
                for key in item.keys():
                    if key.__contains__('time') or key.__contains__('date'):
                        item[key] = self.convert_to_date_time(item[key])
                    if type(item[key]) not in [bool, int, float, datetime, time, date]:
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
        
        connectKeys = list(connect.keys())
        # ensure connection field are contain in the main table fields(self.fieldKeys)
        for key in connectKeys:
            if key not in self.fieldKeyList: return False

        if isConnected and keys and self.isFuseConnected:
            updater = self.fuseTable.objects.get(**self.query)
            for key in keys:
                updater.__dict__[key] = fields[key]
                self.__setattr__(key, fields[key])
            updater.save()
            return True
        elif not isConnected and connectKeys:
            #connectKey = connectKeys[0]
            #connectValue = connect[connectKeys]
            updater = self.fuseTable.objects.get(**connect)
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
        newColumn: ModelFuseType = self.fuseTable(**fields)
        newColumn.save()
        return True

    def delete(self, field: dict={}):
        """The delete function for user in database.

        Example field={"firstname": "George"} or fields={"date": "20/10/2023", "isActive": True}
        This will search for items containing this fields in the table and delete the items,
        in a case where field is not spacified, then everything in the table is deleted.

        Args:
            fields (dict[field,value]): fields and values to filter with. Defaults to {}.
            
        Returns:
            bool: Return's True when user or users body field is deleted from the database.
                and False when the user is not found and connected to the database.
        """

        if self.isFuseConnected:
            self.isFuseConnected = False
            self.bodyFields.delete()
            return True
        else:
            if field:
                keys = list(field.keys())
                # ensure all field are contain in the main table fields(self.fieldKeys)
                for key in keys:
                    if key not in self.fieldKeyList:
                        print('The field: ', key, ' is Not in main field cross',
                              ' check the spelling in ', self.__dbName,' of models.py')
                        return False

                item = self.fuseTable.objects.complex_filter(field)
                if item:
                    self.isFuseConnected = False
                    item.delete()
                    return True

            items = self.fuseTable.objects.all()
            if items:
                self.isFuseConnected = False
                items.delete()
                return True

        return False

    def all(self) -> List[dict]:
        """
        Get all the items in a model table and prepare it in a dictionary format.

        Warning: Do not use this approach if your table has a large amount of data.

        Returns:
            List[dict]: List of all the items in the database table model
        """
        items = self.fuseTable.objects.all()
        if items.count():
            datas = ListDBData(items, self.__dbName)
            self.bodyFields = items
            self.isFuseConnected = True
            self.bodyField = items
            for i in range(len(datas)):
                item: dict = datas[i]
                for key in item.keys():
                    if type(item[key]) not in [bool, int, float]:
                        item[key] = ReverseReplaceTOHtmlCharacter(item[key])
                datas[i] = item
            return datas
        return []

    def count(self, fields={}) -> int:
        """
        Count items in the model table. count items base on fields specified.
        Example field={"firstname": "George"} or fields={"date": "20/10/2023", "isActive": True}
        This will search for items containing this fields in the table and return the
        total number of the items found having such fields.

        Args:
            fields (dict[field,value]): fields and values to filter with. Defaults to {}.

        Returns:
            int: Total number of items found
        """
        totalItems = 0
        if not self.isFuseConnected:
            if fields:
                totalItems = self.fuseTable.objects.complex_filter(fields).count()
            else:
                totalItems = self.fuseTable.objects.all().count()
        else:
            totalItems = self.bodyFields.count()
        return totalItems
