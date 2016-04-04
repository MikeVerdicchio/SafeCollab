from django.db import models

# Models for data tables
# https://docs.djangoproject.com/en/1.9/topics/db/models/

class User(models.Model):
    username = models.CharField(max_length=128)
    site_manager = models.BooleanField()

    def __str__(self):              # __unicode__ on Python 2
        return self.name

class Group(models.Model):
    GROUP_CHOICES = (
        ('G1', 'Group 1'),
        ('G2', 'Group 2'),
        ('G3', 'Group 3'),
    )
    group = models.CharField(max_length=3, choices=GROUP_CHOICES)
    members = models.ManyToManyField(User, through='Membership')

    def __str__(self):              # __unicode__ on Python 2
        return self.name

class Membership(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    group = models.ForeignKey(Group, on_delete=models.CASCADE)
