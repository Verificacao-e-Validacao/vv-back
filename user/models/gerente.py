import uuid
from django.db import models
from django.contrib.auth.models import AbstractUser

class Gerente(AbstractUser):

    id = models.UUIDField(
        primary_key=True, 
        default=uuid.uuid4, 
        editable=False
    )

    groups = models.ManyToManyField(
        'auth.Group',
        related_name='caixa_set',
        blank=True,
        help_text='The groups this user belongs to.',
        verbose_name='groups',
    )

    user_permissions = models.ManyToManyField(
        'auth.Permission',
        related_name='caixa_set',
        blank=True,
        help_text='Specific permissions for this user.',
        verbose_name='user permissions',
    )

    class Meta:
        app_label = 'user'
        verbose_name = 'Gerente'
        verbose_name_plural = 'Gerentes'