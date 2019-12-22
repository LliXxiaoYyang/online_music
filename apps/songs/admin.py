from django.contrib import admin
from .models import Singers, Album, Music, AlbumImage, SingerImage
# Register your models here.

admin.site.register(Singers)
admin.site.register(Album)
admin.site.register(Music)
admin.site.register(AlbumImage)
admin.site.register(SingerImage)
