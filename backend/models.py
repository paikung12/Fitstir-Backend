from django.db import models
class TagType(models.Model):
    name = models.CharField(max_length=255)

    def __str__(self):
        return '{}'.format(self.name)

class Tag(models.Model):
    type = models.ForeignKey(TagType, on_delete=models.CASCADE)
    name = models.CharField(max_length=255)

    def __str__(self):
        return '{},{}'.format(self.type.name,self.name)

class Video(models.Model):
    name = models.CharField(max_length=255)
    video = models.FileField(upload_to='videos/', null=True, verbose_name="Video File")
    tag = models.ManyToManyField(Tag)

    def __str__(self):
        return '{}'.format(self.name)



