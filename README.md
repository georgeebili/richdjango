# richdjango

Let make your python django application more flexible and rich with functionality and simple struture.
Note this application is strictly for Python3.

## Structure

richdjango(folder | App root ):

    cdn(folder: web rending contents):
        css(folder)
        font(folder)
        image(folder)
        js(folder)

    Component(folder: Extra app utilities):
        DarkArt(folder):
            __init_.py
            EmailTool.py
            Fusion.py
            IDApp.py
            MagicBox.py

        AppStrings.py

        Assembler.py

        DatabaseFusion.py

        EmailUserApp.py

        IDHandler.py

    richdjango(folder: Main Django app root ):

        __inti_.py
        apps.py
        asgi.py
        models.py
        settings.py
        urls.py
        views.py
        wsgi.py

    templates(folder: html files used across our app):
        admin(folder)
        layouts(folder)
        mail(folder)

    manage.py

    passenger_wsgi.py

    requirements.txt
