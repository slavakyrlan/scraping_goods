from django.contrib import admin
from .models import Warehouse, Device, Information, Error

admin.site.register(Warehouse)
admin.site.register(Device)
admin.site.register(Information)
admin.site.register(Error)

