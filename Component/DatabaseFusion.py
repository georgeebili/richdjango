"""
first thing is to import the models we want to create a fuse for before definding their fuse.
Example:
from richdjango.models import SourceCodeDB, UserDB

class ClientDBFuse(Fuse):
    def __init__(self) -> None:
        Fuse.__init__(self, SourceCodeDB)
        self.field: SourceCodeDB = self
 
class UserFuse(Fuse):
    def __init__(self):
        super().__init__(UserDB)
        self.field: UserDB = self

fuse = ClientDBFuse()
fuse.connect("emailVerification", True) #returns fuse
print(fuse.getArray())
#print(fuse.isFieldConnected)
#print(fuse.updateField(fields={"passwordReset":""}))
"""
from .DarkArt.Fusion import Fuse

