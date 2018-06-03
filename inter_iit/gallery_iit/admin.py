from django.contrib import admin
from gallery_iit.models import Image, Video
# from embed_video.admin import AdminVideoMixin
# from .models import MyModel
# from .models import Item


admin.site.register(Image)
admin.site.register(Video)
# admin.site.register(Item)

# class MyModelAdmin(AdminVideoMixin, admin.ModelAdmin):
    # pass

# admin.site.register(MyModel, MyModelAdmin)

