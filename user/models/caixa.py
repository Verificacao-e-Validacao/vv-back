import uuid
from django.db import models
from django.contrib.auth.models import AbstractUser

class Caixa(AbstractUser):

    groups = models.ManyToManyField(
        'auth.Group',
        related_name='caixa',
        blank=True,
        help_text='The groups this user belongs to.',
        verbose_name='groups',
    )

    user_permissions = models.ManyToManyField(
        'auth.Permission',
        related_name='caixa',
        blank=True,
        help_text='Specific permissions for this user.',
        verbose_name='user permissions',
    )

    class Meta:
        app_label = 'user'
        verbose_name = 'Caixa'
        verbose_name_plural = 'Caixas'