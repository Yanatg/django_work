from django.contrib.auth.tokens import PasswordResetTokenGenerator
from app_users.models import CustomUser


class ActivationTokenGenerator(PasswordResetTokenGenerator):
    def _make_hash_value(self, user: CustomUser, timestamp):
        return (
            str(user.id) + str(timestamp) + str(user.is_active)
        )

    def _make_token_with_timestamp(self, user, timestamp):
        ts_b36 = self._timestamp_to_base36(timestamp)
        hash_value = self._make_hash_value(user, timestamp)
        return f"{ts_b36}-{hash_value}"

    def _make_token(self, user):
        return self._make_token_with_timestamp(user, self._num_seconds(self._now()))

    def check_token(self, user, token):
        if not (user and token):
            return False

        try:
            ts_b36, hash_value = token.split("-")
        except ValueError:
            return False

        try:
            ts = self._base36_to_timestamp(ts_b36)
        except ValueError:
            return False

        return (
            self._make_token_with_timestamp(user, ts) == token
            and not self._is_token_expired(ts)
        )

    def make_token(self, user):
        return self._make_token(user)

    def get_token(self, user):
        return self._make_token(user)


activation_token_generator = ActivationTokenGenerator()
