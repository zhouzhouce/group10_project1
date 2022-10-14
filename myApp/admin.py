from django.contrib import admin
from .models import GeeksModel
from .models import GeeksWithFieldModel
from .models import Song
from .models import Album

# Register your models here.
admin.site.register(GeeksModel)
admin.site.register(GeeksWithFieldModel)
admin.site.register(Song)
admin.site.register(Album)