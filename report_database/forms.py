from django import forms
from django.forms.extras.widgets import SelectDateWidget
from datetime import datetime

class ReportForm(forms.Form):
    report_name = forms.CharField(label='Report Name*', max_length=50)
    date = forms.DateField(label="Date*", widget=SelectDateWidget(years=[ str(k) for k in range(2000,2051)]))
    sdesc = forms.CharField(label='Short Description*', max_length=60)
    ldesc = forms.CharField(label=(u"Long Description*"), widget=forms.Textarea(attrs={'rows': '10', 'cols':'30'}), max_length=1000)
    private = forms.BooleanField(label='Private', required=False)
    file_1 = forms.FileField(label='File_1', required=False)
    file_2 = forms.FileField(label='File_2', required=False)
    file_3 = forms.FileField(label='File_3', required=False)


