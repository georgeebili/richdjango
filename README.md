# richdjango

Let make your python django application more flexible and rich with functionality and simple struture.
Note this application is strictly for Python3.

## Structure

richdjango(App root):
- playground: Test public web resources directory.
- cdn: Web public resources directory. Store all static files here.
- Component: Directory for app functionalities and components. 
    Write/Keep all core functions of the app here, then from here extend it to .
        
- - DarkArt.
- - - EmailTool.py
- - - Fusion.py
- - - IDApp.py
- - - MagicBox.py

- - AppStrings.py
        Assembler.py
        DatabaseFusion.py
        EmailUserApp.py
        IDHandler.py

- richdjango: Main django app root directory.
- templates: html template used across our app goes here.
- manage.py
- passenger_wsgi.py
- requirements.txt
