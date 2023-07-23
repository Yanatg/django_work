from django.contrib.auth.tokens import PasswordResetTokenGenerator
from app_users.models import CustomUser


class ActivationTokenGenerator(PasswordResetTokenGenerator):
    def _make_hash_value(self, user: CustomUser, timestamp):
        return (
            str(user.id) + str(timestamp) + str(user.is_active)
        )


activation_token_generator = ActivationTokenGenerator()
