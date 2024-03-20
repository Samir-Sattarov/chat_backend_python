from django.db import models


# Create your models here.
class UserModel(models.Model):
    name = models.CharField(default="", max_length=255)
    surname = models.CharField(default="", max_length=255)
    email = models.CharField(default="", max_length=255)
    image = models.ImageField(default="", upload_to="uploads/")
    phone = models.IntegerField(default=0)



