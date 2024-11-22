from django.contrib import admin
from .models import Device, Clienti, Firmware, Download, Learning_Snapshot, Installations

admin.site.register(Device)
admin.site.register(Clienti)
admin.site.register(Firmware)
admin.site.register(Download)
admin.site.register(Learning_Snapshot)
admin.site.register(Installations)
