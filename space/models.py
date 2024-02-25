from pyexpat import model
from django.contrib.auth.models import AbstractBaseUser, PermissionsMixin
from django.db import models
from django.utils import timezone
from django.utils.translation import gettext_lazy as _
from django.dispatch import receiver
from django.urls import reverse
from django_rest_passwordreset.signals import reset_password_token_created
from django.core.mail import send_mail
from .managers import CustomUserManager
#for production deployment add/comment out below line  and comment upperline
#from django.conf import settings


class CustomUser(AbstractBaseUser, PermissionsMixin):
    full_name = models.CharField(max_length=100, default=False)
    email = models.EmailField(unique=True)
    password = models.CharField(max_length=12)
    confirm_password = models.CharField(max_length=12)

    is_staff = models.BooleanField(default=False)
    is_active = models.BooleanField(default=True)
    date_joined = models.DateTimeField(default=timezone.now)

    USERNAME_FIELD = 'email'
    REQUIRED_FIELDS = []

    objects = CustomUserManager()

    def __str__(self):
        return self.email

@receiver(reset_password_token_created)
def password_reset_token_created(sender, instance, reset_password_token, *args, **kwargs):

    # email_plaintext_message = "{}?token={}".format(reverse('password_reset:reset-password-request'), reset_password_token.key)
    #email_plaintext_message = "{} token={} {}\n{} {}".format("Your Password Reset " , reset_password_token.key, "(copy this token id)", "Click the given url and Enter Token ", " http://127.0.0.1:8000/space/api/password_reset/confirm/")
     #for_only_backend_use
    #email_plaintext_message = "{} token={} {}\n{} {}".format("Your Password Reset " , reset_password_token.key, "(copy this token id)", "Click the given url and Enter Token ", " http://127.0.0.1:8000/space/api/password_reset/confirm/")
    #email_plaintext_message = "{}\n{}".format("Your Password Reset " , reset_password_token.key, "(copy this token id)" ),
    #for_backend/frontend use
    email_plaintext_message = "{} token={} {}".format("Your Password Reset " , reset_password_token.key, "(copy this token id)")
    
    send_mail(
        # title:
        "Password Reset for {title}".format(title="Reset Password"),
        # message:
        email_plaintext_message,
        # from:
        "noreply@somehost.local",
        #for production deployment add/comment out below line and comment upperline
        #settings.EMAIL_HOST_USER,
        # to:
        [reset_password_token.user.email]
    )