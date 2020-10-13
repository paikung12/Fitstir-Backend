from django.contrib.auth.models import User
from django.db import models
from polymorphic.models import PolymorphicModel


class UserDetail(models.Model):
    birthday = models.DateField()
    address = models.TextField(max_length=255)
    high = models.IntegerField()
    weight = models.IntegerField()
    bmi = models.FloatField()
    user = models.ForeignKey(User, on_delete=models.CASCADE,)

    def __str__(self):
        return '{},{}'.format(self.birthday, self.address)



class Tag(models.Model):
    name = models.CharField(max_length=255)

    def __str__(self):
        return '{}'.format(self.name)


class Challenge(models.Model):
    name = models.CharField(max_length=255)
    recommend = models.BooleanField()

    def __str__(self):
        return '{}'.format(self.name)


class TagDetail(models.Model):
    name = models.CharField(max_length=255)
    detail = models.ForeignKey(Tag, on_delete=models.CASCADE, null=True)

    def __str__(self):
        return '{}'.format(self.name)


class Video(models.Model):
    image = models.FileField(upload_to='videos/', null=True, verbose_name="Video Image")
    name = models.CharField(max_length=255)
    video = models.FileField(upload_to='videos/', null=True, verbose_name="Video File")
    tag_type = models.OneToOneField(TagDetail, on_delete=models.CASCADE)

    # video_playlist = models.ManyToManyField(VideoPlayList)

    def __str__(self):
        return '{},{}'.format(self.name, self.tag_type)


class VideoPlayList(PolymorphicModel):
    image = models.FileField(upload_to='images', null=True, verbose_name="Playlist Image")
    name = models.CharField(max_length=255)
    video = models.ManyToManyField(Video, null=True, blank=True)

    def __str__(self):
        return '{}'.format(self.name)


class ExerciseTable(VideoPlayList):
    level = models.ForeignKey(Challenge, on_delete=models.CASCADE, )
    day = models.IntegerField()

    # find way unique

    def __str__(self):
        return '{}'.format(self.day)
