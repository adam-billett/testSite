from django.db import models


# Create your models here.
class Users(models.Model):
    username = models.CharField(max_length=50)
    user_pass = models.CharField()
    first_name = models.CharField()
    last_name = models.CharField()
    role = models.CharField()
