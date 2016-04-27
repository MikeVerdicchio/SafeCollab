from django.db import models
from django.contrib.auth.models import User
<<<<<<< HEAD
from FileUpload.models import Document
=======
from auth.models import UserProfile
>>>>>>> b01d9693660604cda7e65049623f08c08ef814c8
import uuid

# Create your models here.
class Report(models.Model):
    creator = models.ForeignKey(User, related_name='report_creator')
    report_name = models.CharField(max_length=50, default='Unnamed')
    date = models.DateField()
    sdesc = models.CharField(max_length=60, blank=False, null=False)
    ldesc = models.CharField(max_length=1000, blank=False, null=False)
    private = models.BooleanField(default=False)
    f1n = models.CharField(max_length=50, blank=True, null=True)
    file_1 = models.FileField(upload_to='documents', blank=True, null=True)
    #file_1 = models.ForeignKey(Document, related_name='file1')
    encrypt_1 = models.BooleanField(default=False)
    f2n = models.CharField(max_length=50, blank=True, null=True)
    file_2 = models.FileField(upload_to='documents', blank=True, null=True)
    #file_2 = models.ForeignKey(Document, related_name='file2')
    encrypt_2 = models.BooleanField(default=False)
    f3n = models.CharField(max_length=50, blank=True, null=True)
    file_3 = models.FileField(upload_to='documents', blank=True, null=True)
    #file_3 = models.ForeignKey(Document, related_name='file3')
    encrypt_3 = models.BooleanField(default=False)
    delete_report = models.BooleanField(default=False)
    uniqueid = models.CharField(default=uuid.uuid4, unique=True, max_length=100, null=True, blank=True)
    folderid = models.CharField(max_length=100, null=True, blank=True)


    def __str__(self):
        return self.report_name



class Folder(models.Model):
    creator = models.ForeignKey(User, related_name='folder_creator')
    folder_name = models.CharField(max_length=50, default='Unnamed')
    shared_users = models.ManyToManyField(User)
    uniqueid = models.CharField(default=uuid.uuid4, unique=True, max_length=100, null=True, blank=True)
    private = models.BooleanField(default=False)

    def __str__(self):
        return self.folder_name
