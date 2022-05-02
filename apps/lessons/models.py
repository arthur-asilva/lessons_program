from django.db import models
from apps.user.models import User





class Subject(models.Model):
    subject = models.CharField(max_length=254)
    user = models.ForeignKey(User, on_delete=models.PROTECT)
    description = models.CharField(max_length=254, blank=True, null=True)
    creation_date = models.DateField(blank=True, null=True, auto_now_add=True)
    
    def __str__(self):
        return self.subject





class Lesson(models.Model):
    user = models.ForeignKey(User, on_delete=models.PROTECT)
    subject = models.ForeignKey(Subject, on_delete=models.PROTECT)
    lesson_date = models.DateField()
    boosts = models.CharField(max_length=254)
    description = models.CharField(max_length=254, blank=True, null=True)
    is_active = models.BooleanField(default=False, blank=True, null=True)
    is_finish = models.BooleanField(default=False, blank=True, null=True)
    finish_date = models.DateField(blank=True, null=True)
    creation_date = models.DateField(blank=True, null=True, auto_now_add=True)

    @property
    def boosts_list_label(self):
        like_list = self.boosts.split(';')
        return ', '.join(like_list)





class SetChoice(models.Model):
    user = models.ForeignKey(User, on_delete=models.PROTECT)
    lesson = models.ForeignKey(Lesson, on_delete=models.PROTECT)
    sequence_number = models.IntegerField()
    choose = models.IntegerField()
    physical_help = models.CharField(max_length=2, blank=True, null=True)
    verbal_help = models.CharField(max_length=2, blank=True, null=True)
    answer_date = models.DateField()
    is_right = models.BooleanField(default=False)
    creation_date = models.DateField(blank=True, null=True, auto_now_add=True)
