# richdjango

Let make your python django application more flexible and rich with functionality and simple struture.
Note this application is strictly for Python3.

## Structure

richdjango(App root):

- playground: Test public web resources directory.
- cdn: Web public resources directory. Store all static files here.
- Component: Directory for app functionalities and components.
    Write/Create all core functions of the app here, then from this directory extend it to
    the main django app root(richdjango) and other part of the app.
- - DarkArt: Extra functionalities to help the app development. All components here are reusble.
- - - EmailTool.py: For sending email message. Look at EmailUserApp.py for usage.
- - - Fusion.py: Database model extention for utilizing and easy use of database models. Look at
    DatabaseFusion.py for usage. This pattern is called *Model Fusion*.
- - - IDApp.py: For generating unique IDs. Look at IDHandler.py for usage.
- - - MagicBox.py: Contains extra functions for backend data collection and protection such as
    post request field data and model data.
- - AppStrings.py: Write all strings that you want to reuse here.
- - Assembler.py: For importing/storing all components, varaibles and functions that we
    want to make global across our app.
- - DatabaseFusion.py: Write all model Fusion with Fuse class here. The Fuse class is found in [Fusion.py](https://github.com/georgeebili/richdjango/blob/main/Component/DarkArt/Fusion.py).
- - EmailUserApp.py
- - IDHandler.py

- richdjango: Main django app root directory.
- templates: html template used across our app goes here.
- manage.py
- passenger_wsgi.py
- requirements.txt
