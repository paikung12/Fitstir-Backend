from django.contrib import admin

# Register your models here.
from backend.models import TagType, Tag, Video

admin.site.register(TagType)
admin.site.register(Tag)

class VideoAdminModel(admin.ModelAdmin):
    filter_horizontal = ('tag',)

admin.site.register(Video,VideoAdminModel)