from django.db import models
from django.utils import timezone
from django.utils.translation import gettext_lazy as lazy
from django.contrib.auth.models import AbstractBaseUser, PermissionsMixin, BaseUserManager


class CustomAccount(BaseUserManager):
    def create_superuser(self, email, user_name, first_name, password, **other_fields):

        other_fields.setdefault('is_staff', True)
        other_fields.setdefault('is_superuser', True)
        other_fields.setdefault('is_active', True)
        other_fields.setdefault('is_drive', True)
        other_fields.setdefault('is_nomal', True)

        if other_fields.get('is_staff') is not True:
            raise ValueError(
                'Superuser must be assigned to is_staff=True.')
        if other_fields.get('is_superuser') is not True:
            raise ValueError(
                'Superuser must be assigned to is_superuser=True.')

        return self.create_user(email, user_name, first_name, password, **other_fields)

    def create_user(self, email, user_name, first_name, password, **other_fields):
        other_fields.setdefault('is_active', True)
        email = self.normalize_email(email)
        user = self.model(email=email, user_name=user_name,
                          first_name=first_name, **other_fields)

        user.set_password(password)
        user.save()

        return user


class NewUsers(AbstractBaseUser, PermissionsMixin):
    email = models.EmailField(lazy('email address'), unique=True)
    user_name = models.CharField(max_length=150, unique=True)
    first_name = models.CharField(max_length=100, blank=True)
    start_date = models.DateTimeField(default=timezone.now)
    about = models.TextField(lazy('about'), max_length=200, blank=True)
    image_account = models.ImageField(lazy('image'), null=True)
    is_staff = models.BooleanField(default=False)
    is_drive = models.BooleanField(default=False)
    is_active = models.BooleanField(default=True)
    is_nomal = models.BooleanField(default=False)
    objects = CustomAccount()

    USERNAME_FIELD = 'email'
    REQUIRED_FIELDS = ['user_name', 'first_name']

    def __str__(self):
        return self.user_name
