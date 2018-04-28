import datetime

from django.db import models
from django.utils import timezone


class User(models.Model):
    user_id = models.IntegerField(primary_key=True)
    username = models.CharField(max_length=300)
    name = models.CharField(max_length=300)
    surname = models.CharField(max_length=300)
    reg_date = models.DateTimeField('date registered')
    birth_date = models.DateTimeField('birth date')
    last_pub = models.DateTimeField('date last published')

    def __str__(self):
        return self.username


class Toque(models.Model):
    toque_id = models.IntegerField(primary_key=True)
    name = models.CharField(max_length=300)
    author_id = models.ForeignKey(User, on_delete=models.CASCADE)
    author_username = models.CharField(max_length=300)
    audio = models.CharField(max_length=300)
    pub_date = models.DateTimeField('date published')

    def __str__(self):
        return self.name

    def was_published_recently(self):
        now = timezone.now()
        return now - datetime.timedelta(days=1) <= self.pub_date <= now
