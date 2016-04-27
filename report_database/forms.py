from django import forms
from django.forms.extras.widgets import SelectDateWidget
from datetime import datetime
from .models import Report

class ReportForm(forms.Form):
    report_name = forms.CharField(label='Report Name*', max_length=50)
    date = forms.DateField(label="Date*", widget=SelectDateWidget(years=[ str(k) for k in range(2000,2051)]))
    sdesc = forms.CharField(label='Short Description*', max_length=60)
    ldesc = forms.CharField(label=(u"Long Description*"), widget=forms.Textarea(attrs={'rows': '10', 'cols':'30'}), max_length=1000)
    private = forms.BooleanField(label='Private', required=False)
    file_1 = forms.FileField(label='File 1', required=False)
    encrypt_1 = forms.BooleanField(label='Encrypt File 1', required=False)
    file_2 = forms.FileField(label='File 2', required=False)
    encrypt_2 = forms.BooleanField(label='Encrypt File 2', required=False)
    file_3 = forms.FileField(label='File 3', required=False)
    encrypt_3 = forms.BooleanField(label='Encrypt File 3', required=False)

class FolderForm(forms.Form):
    folder_name = forms.CharField(label='Folder Name*', max_length=50)
    shared_user_field = forms.CharField(label='Users Given Access (Seperate by Commas)', max_length=1000, required=False)
    private = forms.BooleanField(label='Private', required=False)

class EditReportForm(forms.Form):
    report_name = forms.CharField(label='Report Name*', max_length=50)
    date = forms.DateField(label="Date*", widget=SelectDateWidget(years=[str(k) for k in range(2000, 2051)]))
    sdesc = forms.CharField(label='Short Description*', max_length=60)
    ldesc = forms.CharField(label=(u"Long Description*"), widget=forms.Textarea(attrs={'rows': '10', 'cols': '30'}), max_length=1000)
    private = forms.BooleanField(label='Private', required=False)
    file_1 = forms.FileField(label='File 1', required=False)
    encrypt_1 = forms.BooleanField(label='Encrypt File 1', required=False)
    file_2 = forms.FileField(label='File 2', required=False)
    encrypt_2 = forms.BooleanField(label='Encrypt File 2', required=False)
    file_3 = forms.FileField(label='File 3', required=False)
    encrypt_3 = forms.BooleanField(label='Encrypt File 3', required=False)


class deleteReportForm(forms.Form):
    report_delete = forms.BooleanField(label='Delete Report?', required=False)
