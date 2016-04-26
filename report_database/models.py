from django.db import models
from django.contrib.auth.models import User
from auth.models import UserProfile
import uuid

# Create your models here.
class Report(models.Model):
    creator = models.ForeignKey(UserProfile.User)
    report_name = models.CharField(max_length=50, default='Unnamed')
    date = models.DateField()
    sdesc = models.CharField(max_length=60, blank=False, null=False)
    ldesc = models.CharField(max_length=1000, blank=False, null=False)
    private = models.BooleanField(default=False)
    file_1 = models.FileField(upload_to='documents', blank=True, null=True)
    encrypt_1 = models.BooleanField(default=False)
    file_2 = models.FileField(upload_to='documents', blank=True, null=True)
    encrypt_2 = models.BooleanField(default=False)
    file_3 = models.FileField(upload_to='documents', blank=True, null=True)
    encrypt_3 = models.BooleanField(default=False)
    delete_report = models.BooleanField(default=False)
    uniqueid = models.CharField(default=uuid.uuid4, unique=True, max_length=100, null=True, blank=True)


    def __str__(self):
        return self.report_name
