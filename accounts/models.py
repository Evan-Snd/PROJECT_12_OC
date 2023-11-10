from django.db import models
from django.contrib.auth.models import AbstractUser


class CustomUser(AbstractUser):
    # username = None
    EQUIPE_GESTION = 'EG'
    EQUIPE_COMMERCIAL = 'EC'
    EQUIPE_SUPPORT = 'ES'

    USERS_STATUS = (
        (EQUIPE_GESTION, 'Gestion'),
        (EQUIPE_COMMERCIAL, 'Commercial'),
        (EQUIPE_SUPPORT, 'Support'),
    )

    first_name = models.CharField(max_length=255)
    last_name = models.CharField(max_length=255)
    username = models.EmailField(unique=True)
    # equipe = models.CharField(max_length=2,
    #                           choices=USERS_STATUS,
    #                           default=EQUIPE_COMMERCIAL)

    USERNAME_FIELD = 'username'
    REQUIRED_FIELDS = []

    def __str__(self):
        return self.first_name + ' ' + self.last_name
