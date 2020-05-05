from django.contrib.auth.models import User

class EmailAuthBackend(object):
    """
    Authenticate using an e-mail address.
    authenticate(): We try to retrieve a user with the given email address and check
    the password using the built-in check_password() method of the user model. 
    This method handles the password hashing to compare the given password against the 
    password stored in the database.
    get_user(): We get a user through the ID set in the user_id parameter. 
    Django uses the backend that authenticated the user to retrieve the User object 
    for the duration of the user session.
    """
    def authenticate(self, request, username=None, password=None):
        try:
            user = User.objects.get(email=username)
            if user.check_password(password):
                return user
            return None
        except User.DoesNotExist:
            return None
    def get_user(self, user_id):
        try:
            return User.objects.get(pk=user_id)
        except User.DoesNotExist:
            return None