from django.contrib.auth.models import User

class RegisterUser(User):
    def create(user, username, email, password):
        user = User.objects.create_user(username=username, email=email, password=password)
        user.save()

        return user
