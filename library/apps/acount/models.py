from enum import Enum
from django.core import validators
from django.contrib.auth.models import (
    AbstractBaseUser,
    PermissionsMixin,
    BaseUserManager,
)
from django.db import models


class UserManager(BaseUserManager):


class Role(Enum):

    USER = 'user'
    ADMIN = 'admin'
    SUBSCRIPTION = 'subscription'

class User(AbstractBaseUser, PermissionsMixin):

    ROLE = [
        (Role.USER, Role.USER),
        (Role.ADMIN, Role.ADMIN),
        (Role.SUBSCRIPTION, Role.SUBSCRIPTION)
    ]

    email = models.EmailField(
        db_index=True,
        validators=[validators.validate_email],
        unique=True,
        blank=False,
        null=False,
        verbose_name='email'
    )

    avatar = models.ImageField(
        upload_to='photos/%y/%m/%d',
        null=True,
        blank=True,
        verbose_name='изображение'
    )

    first_name = models.CharField(
        max_length=100,
        blank=True,
        null=True,
        verbose_name='Имя'
    )

    last_name = models.CharField(
        max_length=100,
        blank=True,
        null=True,
        verbose_name='Фамилия'
    )

    role = models.CharField(
        choices=ROLE,
        default="user",
        max_length=100,
        null=False,
        blank=False,
        verbose_name="Роль"
    )

    date_create = models.DateTimeField(
        auto_now_add=True,
        verbose_name="Дата регистрации"
    )

    is_staff = models.BooleanField(default=False, verbose_name="Персонал")
    is_active = models.BooleanField(default=True, verbose_name="Активный")
    is_superuser = models.BooleanField(default=False, verbose_name="Админ")

    USERNAME_FIELD = 'email'
    REQUIRED_FIELDS = ['password']
    object = UserManager()

    class Meta:
        verbose_name = 'пользователь'
        verbose_name_plural = 'пользователи'

    def __str__(self):
        return self.email