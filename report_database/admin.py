from django.contrib import admin
from .models import Report
from .models import Folder

# Register your models here.
admin.site.register(Report)
admin.site.register(Folder)