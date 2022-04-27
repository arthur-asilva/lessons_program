import email
from json import tool
from tokenize import group
from django.db import models
from django.contrib.postgres.fields import ArrayField
from tools.private_data import ACCESS_GROUPS_NAME


class User(models.Model):
    name = models.CharField(max_length=254)
    email = models.CharField(max_length=254)
    password = models.CharField(max_length=10)
    group = models.IntegerField(choices=[(key, value) for key, value in ACCESS_GROUPS_NAME.items()])
    status = models.BooleanField(default=True, null=True, blank=True)
    is_staff = False

    @property
    def is_staff(self):
        return self.group < 0
