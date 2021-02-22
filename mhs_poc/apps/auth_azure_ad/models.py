from datetime import datetime, timedelta

from django.contrib.auth.models import AbstractUser
from django.db import models
from django.db.models.signals import post_save
from django.dispatch import receiver


# Create your models here.
class User(AbstractUser):
    email = models.EmailField(
        verbose_name="email address",
        max_length=255,
        unique=True,
    )

    # Token field
    access_token = models.CharField(max_length=3000, blank=True)
    id_token = models.CharField(max_length=2048, blank=True)
    token_expires = models.DateTimeField(blank=True, null=True)

    account_expiry = models.DateField(default=datetime(2100, 1, 1))

    # USERNAME_FIELD = "email"
    REQUIRED_FIELDS = ["email"]

    def __str__(self):
        return self.email


@receiver(post_save, sender=User)
def create_user(sender, instance, created, **kwargs):
    if created:
        # Set account_expiry here and not as default value in User model
        instance.account_expiry = datetime.now() + timedelta(days=365)
