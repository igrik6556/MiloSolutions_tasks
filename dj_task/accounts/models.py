import random
from django.db import models
from django.contrib.auth.models import AbstractUser


class CustomUser(AbstractUser):
    """
    CustomUser class extends the default Django User.
    It has all the fields and permission setting of
    Django user and also adds two additional fields.
    """
    birthday = models.DateField(
        "Date of birth",
        blank=True,
        null=True
    )
    random_number = models.IntegerField(
        "Random number",
        blank=True,
        null=True
    )

    def save(self, *args, **kwargs):
        """
        Save CustomUser model and assigns
        a random number if that user does
        not exist in the database.
        """
        if not self.pk:
            self.random_number = random.randint(1, 100)

        super(CustomUser, self).save(*args, **kwargs)
