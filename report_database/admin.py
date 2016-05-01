from django.contrib import admin
from .models import Report
from .models import Folder
from .models import Documents

# Register your models here.
admin.site.register(Report)
admin.site.register(Folder)
admin.site.register(Documents)