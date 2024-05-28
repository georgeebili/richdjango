from Component.Assembler import render, HttpRequest

from Component.ExampleApp import ExampleSignUp

def indexPage(request: HttpRequest):
    return render(request, 'index.html')

def signupPage(req):
    # example of how to use component. Now export this function to urls.py and link it to a url as the function.
    return ExampleSignUp(req).signup()


# Activate Admin
"""
python manage.py runserver
python manage.py makemigrations richdjango
python manage.py migrate

python manage.py shell
from richdjango.models import App
a = App()
a.save()
exit()
"""

