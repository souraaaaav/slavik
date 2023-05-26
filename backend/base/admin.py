from django.contrib import admin

from . import models

# Register your models here.

admin.site.register(models.User)
admin.site.register(models.ContactInfo)
admin.site.register(models.MetroArea)
admin.site.register(models.CompanyInfo)
admin.site.register(models.PersonalUser)
admin.site.register(models.BusinessUser)