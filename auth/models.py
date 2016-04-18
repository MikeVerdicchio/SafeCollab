from django.db import models

# Models for data tables
# https://docs.djangoproject.com/en/1.9/topics/db/models/
class User(models.Model):
    username = models.CharField(max_length=128)
    site_manager = models.BooleanField()

    def createReport(self, date, sdesc, ldesc, private):
        report = self.create(creator=self, date=date, sdesc=sdesc, ldesc=ldesc, private=private)
        return report

    def __str__(self):              # __unicode__ on Python 2
        return self.name

class UserProfile(models.Model):
    username = models.CharField(max_length=128, default='')
    site_manager = models.BooleanField(default=False)
    public_key = models.BinaryField(default=b'\x08')

    # def username(self):
    #     return self.user.username
    #
    # def public_key(self, bool):
    #     self.user.public_key = bool
    #     return self.user.site_manager
    #
    # def site_manager(self, bool):
    #     self.user.site_manager = bool
    #     return self.user.site_manager

    # Override the __unicode__() method to return out something meaningful!
    def __unicode__(self):
        return self.user.username

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

class Report(models.Model):
    creator = models.ForeignKey(User)
    date = models.DateField()
    sdesc = models.CharField(max_length=60)
    ldesc = models.CharField(max_length=1000)
    private = models.BooleanField(default=False)

    def __str__(self):
        return self.date