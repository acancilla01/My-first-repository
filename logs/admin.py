from django.contrib import admin
from .models import Log_file, Filtri, DevicesEvent
# Register your models here.

admin.site.register(Log_file)
admin.site.register(Filtri)
admin.site.register(DevicesEvent)
