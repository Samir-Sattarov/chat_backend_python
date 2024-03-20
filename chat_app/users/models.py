from django.db import models


# Create your models here.
class UserModel(models.Model):
    name = models.CharField(default="", max_length=255)
    avatar = models.ImageField(default="", upload_to="uploads/")
