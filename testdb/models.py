from django.db import models


# Create your models here.
class Users(models.Model):
    username = models.CharField(max_length=50)
    user_pass = models.CharField()


class TestingTable(models.Model):
    testVar = models.CharField(max_length=5)
    age = models.IntegerField()


class MoreTest(models.Model):
    ident = models.IntegerField()
    length = models.IntegerField()
    Shape = models.CharField(max_length=100)

