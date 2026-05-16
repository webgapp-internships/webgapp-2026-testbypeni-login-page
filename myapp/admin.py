from django.contrib import admin
from .models import *

# Register your models here.

# from .models import Profile

# @admin.register(Profile)
# class ProfileAdmin(admin.ModelAdmin):
#     list_display = ("user", "phone", "dob", "gender")

# admin.site.register(Forms)


from django.contrib import admin
from import_export.admin import ImportExportModelAdmin
from .models import Forms
from .resources import FormsResource

@admin.register(Forms)
class FormsAdmin(ImportExportModelAdmin):
    resource_class = FormsResource
    list_display = ('id', 'full_name', 'email', 'phone', 'dob', 'gender', 'agree_terms', 'created_at')
    search_fields = ('full_name', 'email', 'phone')
    list_filter = ('gender', 'agree_terms', 'created_at')
