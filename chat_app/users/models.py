from django.contrib.auth.base_user import AbstractBaseUser, BaseUserManager
from django.contrib.auth.models import PermissionsMixin, AbstractUser
from django.db import models


# Create your models here.

class CustomUserManager(BaseUserManager):

    def create_user(self, phone, password, **extra_fields):
        if not phone:
            raise ValueError({"message": "Phone is empty or not found!"})

        extra_fields.setdefault('is_active', True)

        user = self.model(phone=phone, **extra_fields)
        user.set_password(password)
        user.email = ""
        user.save()
        return user

    def create_super_user(self, phone, password, **extra_fields):
        if not phone:
            raise ValueError({"message": "Phone is empty or not found!"})

        extra_fields.setdefault('is_superuser', True)
        extra_fields.setdefault('is_active', True)

        return self.create_user(phone, password, **extra_fields)


class UserModel(AbstractUser):
    name = models.CharField(default="", max_length=255, verbose_name="Имя")
    username = models.CharField(default="", max_length=255, verbose_name="Фамилия")
    surname = models.CharField(default="", max_length=255, verbose_name="Имя пользователя")
    password = models.CharField(default="", max_length=30)
    image = models.ImageField(default="", upload_to="uploads/")
    phone = models.IntegerField(default=0, unique=True, verbose_name="Номер телефона")
    is_active = models.BooleanField(default=True)

    USERNAME_FIELD = "phone"
    REQUIRED_FIELDS = ["name", "surname", 'username']

    EMAIL_FIELD = None

    def __str__(self):
        return str(self.name) + " " + str(self.surname) + " " + "(" + str(self.username) + ")"
