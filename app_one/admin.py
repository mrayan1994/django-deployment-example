from django.contrib import admin
from app_one.models import Topic, Webpage, AccessRecord, UserProfileInfo

# Register your models here.

admin.site.register(Topic)
admin.site.register(Webpage)
admin.site.register(AccessRecord)
admin.site.register(UserProfileInfo)
