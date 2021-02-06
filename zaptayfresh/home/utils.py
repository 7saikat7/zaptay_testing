from django.contrib.auth.tokens import PasswordResetTokenGenerator
import six


class Tokengenerator(PasswordResetTokenGenerator):

    def _make_hash_value(self,user,timestap):
      return (
          six.text_type(user.pk)+six.text_type(timestap)+six.text_type(user.is_active)

        )
account_activation_token=Tokengenerator() 