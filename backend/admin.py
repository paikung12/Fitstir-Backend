from django.contrib import admin
from polymorphic.admin import PolymorphicParentModelAdmin, PolymorphicChildModelAdmin
# Register your models here.
from backend.models import Tag, Video, TagDetail, ExerciseTable, UserDetail, Challenge, VideoPlayList


class VideoAdmin(admin.ModelAdmin):
    list_display = ('name', 'video', 'tag_type',)

class TagDetailInline(admin.TabularInline):
    model = TagDetail

class TagAdmin(admin.ModelAdmin):
    list_display = ('id', 'name',)
    inlines = [
        TagDetailInline
    ]

@admin.register(ExerciseTable)
class ExerciseChildAdmin(PolymorphicChildModelAdmin):
    base_model = ExerciseTable
    show_in_index = True
    filter_horizontal = ['video']


@admin.register(VideoPlayList)
class PlayListAdmin(PolymorphicParentModelAdmin):
    base_model = VideoPlayList
    child_models = (VideoPlayList, ExerciseTable,)
    filter_horizontal = ['video']





admin.site.register(Challenge)

admin.site.register(Tag, TagAdmin)
admin.site.register(Video, VideoAdmin)
admin.site.register(UserDetail)
admin.site.register(TagDetail)
