from django.db import models
from django.contrib.auth.models import User

# Create your models here.
class Report(models.Model):
    creator = models.ForeignKey(User)
    report_name = models.CharField(max_length=50, default='Unnamed')
    date = models.DateField()
    sdesc = models.CharField(max_length=60, blank=False, null=False)
    ldesc = models.CharField(max_length=1000, blank=False, null=False)
    private = models.BooleanField(default=False)
    file_1 = models.FileField(upload_to='documents', blank=True, null=True)
    file_2 = models.FileField(upload_to='documents', blank=True, null=True)
    file_3 = models.FileField(upload_to='documents', blank=True, null=True)


    def __str__(self):
        return self.report_name