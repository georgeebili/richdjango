"""New Concept for using strings all across the app."""
class StringBank:
    class link:
        index = '/'
        gift = index + 'gift'
        class user:
            main = '/'
            home = main + "home"
        class admin:
            main = '/app/'
            home = main + 'home'

    class File:
        gift = "gift.html"

class UrlString:
    index = '/'

class FileString:
    gift = "gift.html"
    
# example
StringBank.link.index
