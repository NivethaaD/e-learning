from .base import *
DEBUG = False
ADMINS = (
    ('Nivethaa D', 'abc@gmail.com'),
)
ALLOWED_HOSTS = ['*']
DATABASES = {
    'default': {
     'ENGINE': 'django.db.backends.postgresql',
       'NAME': 'educa',
       'USER': 'educa',
       'PASSWORD': 'admin123n',
    
    }
}
