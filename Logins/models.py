from django.db import models


# Create your models here.
class Logins_model(models.Model):
    id = models.AutoField(primary_key=True)
    login = models.CharField(max_length=100)
    password = models.CharField(max_length=100)
    status = models.BooleanField(default=True)


class User(models.Model):
    id = models.AutoField(primary_key=True)
    name = models.CharField(max_length=100)
    tg_id = models.BigIntegerField()
    sending = models.BooleanField(default=False)
