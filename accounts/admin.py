from django.contrib import admin
from accounts.models import User, UploadFile
from django.contrib.auth.models import Permission

# @admin.register(User)
# class UserAdmin(admin.ModelAdmin):
#     pass

admin.site.register(User)


@admin.register(Permission)
class PermissionAdmin(admin.ModelAdmin):
    pass


@admin.register(UploadFile)
class FileUploadAdmin(admin.ModelAdmin):
    pass
