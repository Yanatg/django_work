from django.contrib.auth.backends import ModelBackend
from django.db.models import Q
from app_users.models import CustomUser

class EmailBackend(ModelBackend):
    def authenticate(self, request, username=None, password=None, **kwargs):
        user: CustomUser = None
        try:
            user = CustomUser.objects.get(Q(username__iexact=username) | Q(email__iexact=username))
            is_correct_password = user.check_password(password)
            is_active = self.user_can_authenticate(user)
            if not is_correct_password or not is_active:
                raise Exception("Invalid username/password")

        except CustomUser.DoesNotExist:
            pass
        return user

    def get_user(self, user_id):
        try:
            user = CustomUser.objects.get(id=user_id)
            if not self.user_can_authenticate(user):
                raise Exception("User is inactive")
        except CustomUser.DoesNotExist:
            return None

