# User Model and Authentication
We are using django.contrib.auth `s User model which give as a default User with id, username, email. In addition to that we are creating authentication.py class to add custom authentication.
We are checking user's email and password .
After we need to add this code block to settings.py

``` python
AUTHENTICATION_BACKENDS = [
    'django.contrib.auth.backends.ModelBackend',
    'account.authentication.EmailAuthBackend',
]
```
In this code block we first try to use ModelBackend to authenticate user, after that if needed 
we can authenticate user with EmailAuthBackend it basically follow the order.

*The order of the backends listed in the AUTHENTICATION_BACKENDS setting matters. If the same credentials are valid for multiple backends, Django will stop at the first backend that successfully authenticates the user.*
