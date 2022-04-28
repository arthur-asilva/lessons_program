import email
from json import tool
from tokenize import group
from django.db import models
from tools.private_data import ACCESS_GROUPS_NAME


class User(models.Model):
    name = models.CharField(max_length=254)
    email = models.CharField(max_length=254, unique=True)
    password = models.CharField(max_length=10)
    group = models.IntegerField(choices=[(key, value) for key, value in ACCESS_GROUPS_NAME.items()])
    status = models.BooleanField(default=True, null=True, blank=True)
    is_staff = False

    @property
    def is_staff(self):
        return self.group < 0


class Patient(User):
    adivisor = models.ForeignKey('User', related_name='adivisor_fk', on_delete=models.PROTECT)
    guardian = models.ForeignKey('User', related_name='guardian_fk', on_delete=models.PROTECT)
