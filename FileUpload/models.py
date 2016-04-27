from django.db import models
from django.contrib.auth.models import User
#from report_database.models import Report

# Create your models here.
class Document(models.Model):
    docfile = models.FileField(upload_to='documents', blank=True, null = True)
