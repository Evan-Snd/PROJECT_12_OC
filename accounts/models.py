from django.db import models
from django.contrib.auth.models import AbstractUser


class CustomUser(AbstractUser):
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
    email = models.EmailField(unique=True)
    # equipe = models.CharField(max_length=2,
    #                           choices=USERS_STATUS,
    #                           default=EQUIPE_COMMERCIAL)
    username = None
    USERNAME_FIELD = 'email'
    REQUIRED_FIELDS = []

    def __str__(self):
        return self.first_name + '' + self.last_name

