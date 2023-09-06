from django.contrib import admin

from .models import User, Country, University, UserInfo

admin.site.register(User)
admin.site.register(UserInfo)
admin.site.register(Country)
admin.site.register(University)