import uuid

from django.db import models
from django.db.models.signals import post_save
from django.dispatch import receiver

from mhs_poc.apps.auth_azure_ad.models import User


class UserProfile(models.Model):
    """
    This UserProfile model encapsulate any app-specific information or behavior for the User.
    Example: User's role, user's Topics, user's list of pages etc

    This separates the concerns between User model (in auth_azure_ad by default) to only handle auth information
    And UserProfile handles app-specific information or behavior
    """

    user = models.OneToOneField(User, on_delete=models.CASCADE)

    MEMBER = 1
    LEAD = 2
    ADMIN = 3
    SUPERADMIN = 4

    USER_TYPE_CHOICES = (
        (MEMBER, "Member"),
        (LEAD, "Lead"),
        (ADMIN, "Admin"),
        (SUPERADMIN, "Super Admin"),
    )

    user_type = models.PositiveSmallIntegerField(
        choices=USER_TYPE_CHOICES, default=MEMBER
    )

    # Add any custom UserProfile properties here

    # END - Add any custom UserProfile properties here

    def __str__(self):
        return self.user.username

    def set_user_type(self, user_type: int):
        """
        Args:
            user_type (int): 1 for "Member", 2 for "Lead", 3 for "Admin", and 4 for "Super Admin".
        """
        self.user_type = self.USER_TYPE_CHOICES[user_type]

    def has_access_to_page(self, page_name):
        if self.user_type == self.SUPERADMIN or self.user_type == self.ADMIN:
            return True

        if self.pages.filter(name=page_name).count() == 1:
            return True
        else:
            return False

    def save(self, *args, **kwargs):

        if self.user_type == self.MEMBER:
            self.is_admin = False
            self.is_superuser = False

        if self.user_type == self.LEAD or self.user_type == self.ADMIN:
            self.is_admin = True
            self.is_superuser = False

        if self.user_type == self.SUPERADMIN:
            self.is_admin = True
            self.is_superuser = True

        if self.is_admin is True and self.is_superuser is True:
            self.user_type = self.SUPERADMIN

        # Add any custom business logic to be executed on .save() calls

        # END - any custom business logic to be executed on .save() calls

        super().save(*args, **kwargs)


# Save signals to create and save UserProfile when User object is created/saved
# See: https://simpleisbetterthancomplex.com/tutorial/2016/07/22/how-to-extend-django-user-model.html#proxy
@receiver(post_save, sender=User)
def create_user_profile(sender, instance, created, **kwargs):
    if created:
        UserProfile.objects.create(user=instance)


@receiver(post_save, sender=User)
def save_user_profile(sender, instance, **kwargs):
    instance.userprofile.save()


class Department(models.Model):
    dept_id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    name = models.CharField(
        max_length=128, error_messages={"required": "A dept name is required"}
    )
    teams = models.ManyToManyField("Team", related_name="departments", blank=True)

    # Add any custom Department properties here

    # END - Add any custom Department properties here

    def __str__(self):
        return self.name

    # Add any custom Department methods here

    # END - Add any custom Department methods here


class Team(models.Model):
    name = models.CharField(
        max_length=128, error_messages={"required": "A team name is required"}
    )
    description = models.TextField(blank=True)
    lead = models.OneToOneField(
        UserProfile,
        on_delete=models.CASCADE,
        primary_key=True,
        limit_choices_to={"user_type": UserProfile.LEAD},
    )
    members = models.ManyToManyField(
        UserProfile,
        related_name="teams",
        limit_choices_to={"user_type": UserProfile.MEMBER},
    )

    # Add any custom Team properties here

    # END - Add any custom Team properties here

    def __str__(self):
        return self.name

    # Add any custom Team methods here

    # END - Add any custom Team methods here

    def save(self, *args, **kwargs):
        # Add any custom business logic to be executed on .save() calls

        # END - any custom business logic to be executed on .save() calls

        super(Team, self).save(*args, **kwargs)
