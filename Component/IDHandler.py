from .DarkArt.IDApp import IDApp

class UniqueIDApp(IDApp):
    """
    A unique component that helps you generate ID all acrose your application.
    Define functions like the test function sample to be generating unique ID for your usage.
    check the guess method in the IDApp component for more options about the "which" parameter.
    """
    def __init__(self):
        super().__init__()
        
    def test(self):
        while True:
            freshID = 'U' + self.guess(by=7) + self.guess(which="all-letter", by=3) + self.guess(which="combine", by=2)
            if self.checkID("test", freshID): return freshID


