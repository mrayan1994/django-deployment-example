from django.db import models
from django.contrib.auth.models import User

# Create your models here.


class UserProfileInfo(models.Model):

    user = models.OneToOneField(User, on_delete=models.PROTECT)

    portfolio = models.URLField(blank=True)
    picture = models.ImageField(upload_to='profile_pics', blank=True)

    def __str__(self):

        return self.user.username


class Topic(models.Model):

    top_name = models.CharField(max_length=128, unique=True)

    def __str__(self):

        return self.top_name


class Webpage(models.Model):

    topic = models.ForeignKey(Topic, on_delete=models.PROTECT)
    name = models.CharField(max_length=128, unique=True)
    url = models.CharField(max_length=128, unique=True)

    def __str__(self):

        return self.name


class AccessRecord(models.Model):

    webpage = models.ForeignKey(Webpage, on_delete=models.PROTECT)
    date = models.DateField()

    def __str__(self):

        return str(self.webpage) + " was accessed on " + str(self.date)
