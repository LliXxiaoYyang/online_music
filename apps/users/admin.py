from django.contrib import admin
from .models import User,UserFav,PlayHistory,UserComment

# Register your models here.

admin.site.register(User)
admin.site.register(UserFav)
admin.site.register(PlayHistory)
admin.site.register(UserComment)
