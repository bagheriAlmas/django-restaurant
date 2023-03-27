from django.contrib import admin
from .models import PublicUser,StaffUser
# Register your models here.

admin.site.register(PublicUser)
admin.site.register(StaffUser)