##Django-lat :parrot:

##Requirements
* Python 3.9
* Django 4.0
##Installation
Use `pip`:
```
pip install -r requirements.txt
```


##Installation Docker change db settings on:
```
DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.postgresql',
        'NAME': 'postgres',
        'USER': 'postgres',
        'PASSWORD': 'postgres',
        'HOST': 'pgdb',
        'PORT': 5432,
    }
}
```
###change:
```ALLOWED_HOSTS = ['*']```,
```DEBUG = False```
###add ```SECRET_KEY```