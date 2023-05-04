from Component.Assemble import render

def indexPage(request): return render(request, 'index.html')


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

