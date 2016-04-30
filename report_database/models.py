from django.db import models
from django.contrib.auth.models import User

from FileUpload.models import Document

from auth.models import UserProfile

import uuid

# Create your models here.

class Folder(models.Model):
    creator = models.ForeignKey(User, related_name='folder_creator')
    folder_name = models.CharField(max_length=50, default='Unnamed', unique=True)
    shared_users = models.ManyToManyField(User)
    private = models.BooleanField(default=False)
    uniqueid = models.CharField(default=uuid.uuid4, unique=True, max_length=100, null=True, blank=True)

    def __str__(self):
        return self.folder_name

class Report(models.Model):
    creator = models.ForeignKey(User, related_name='report_creator')
    report_name = models.CharField(max_length=50, default='Unnamed')
    date = models.DateField()
    sdesc = models.CharField(max_length=60, blank=False, null=False)
    ldesc = models.CharField(max_length=1000, blank=False, null=False)
    private = models.BooleanField(default=False)

    #f1n = models.CharField(max_length=50, blank=True, null=True)
    #file_1 = models.FileField(upload_to='documents', blank=True, null=True)
    #encrypt_1 = models.BooleanField(default=False)
    #f2n = models.CharField(max_length=50, blank=True, null=True)
    #file_2 = models.FileField(upload_to='documents', blank=True, null=True)
    #encrypt_2 = models.BooleanField(default=False)
    #f3n = models.CharField(max_length=50, blank=True, null=True)
    #file_3 = models.FileField(upload_to='documents', blank=True, null=True)
    #encrypt_3 = models.BooleanField(default=False)
    delete_report = models.BooleanField(default=False)
    uniqueid = models.CharField(default=uuid.uuid4, unique=True, max_length=100, null=True, blank=True)
    folder = models.ForeignKey(Folder, related_name='Folder', blank=True, null=True)
    #shared_users = models.ManyToManyField(User)


    def __str__(self):
        return self.report_name

class Documents(models.Model):
    #creator = models.ForeignKey(User, related_name='file_creator')
    #fn = models.CharField(max_length=50, blank=True, null=True)
    docfile = models.FileField(upload_to='documents', blank=True, null=True)
    encrypt = models.BooleanField(default=False)
    #report = models.ForeignKey(Report, related_name='Report', blank = True, null = True)
    shared_users = models.ManyToManyField(User)
    report = models.ForeignKey(Report, related_name='report')
    private = models.BooleanField(default=False)
    #delete_doc = models.BooleanField(default=False)

