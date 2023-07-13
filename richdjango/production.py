from pathlib import Path
# for building like DIR_Path / 'subdir'.
AppDirectory = Path(__file__).resolve().parent.parent

# production state
LIVE = False

# development version of django settings goes here
DEBUG = True
ALLOWED_HOSTS = ["*"]
EMAIL_HOST = "" #'example.com'
EMAIL_PORT = "465" #'26'
EMAIL_HOST_USER = "" #'username@example.com'
EMAIL_HOST_PASSWORD = "" #'email password'
TIME_ZONE = "UTC"
MediaDirecory = AppDirectory / 'cdn' / 'resources'

# production version of django settings goes here
if LIVE:
    DEBUG = False
    ALLOWED_HOSTS = ["*"]
    EMAIL_HOST = "" #'example.com'
    EMAIL_PORT = "465" #'26'
    EMAIL_HOST_USER = "" #'username@example.com'
    EMAIL_HOST_PASSWORD = "" #'email password'
    TIME_ZONE = "Africa/Lagos"
    # TIME_ZONE = "UTC"
    MediaDirecory = AppDirectory.parent / 'public_html' / 'cdn' / 'resources'

# fixed version of development - Django time customization
try:
    import django.utils.timezone as DjangoTime
except:
    import pytz
    from datetime import datetime
    DjangoTime = datetime.now(pytz.timezone(TIME_ZONE))
