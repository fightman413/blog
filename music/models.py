import uuid

from django.db import models

# Create your models here.
#音乐素材表
class Music(models.Model):
    songs_id = models.UUIDField(primary_key=True, auto_created=True, default=uuid.uuid4, editable=False)
    singer = models.CharField(max_length=20)
    songs_name =models.CharField(max_length=20)
    MusicParentParamCode = models.CharField(max_length=50,default='')
    MusicParentParamID = models.CharField(max_length=100,default='')
    MusicParentParam = models.CharField(max_length=100,default='')
    MusicCode = models.CharField(max_length=20,default='')
    song_file_url =models.CharField(max_length=80)
    song_image_url = models.CharField(max_length=100)
    IsDeleted = models.BooleanField(default=False)
    CreateTime = models.DateTimeField(auto_now_add=True)
    UpdateTime = models.DateTimeField(auto_now=True)

#音乐文件表
class MusicFile(models.Model):
    songs_file_id = models.UUIDField(primary_key=True, auto_created=True, default=uuid.uuid4, editable=False)
    song_file =models.FileField(upload_to='music/musicfile',verbose_name="选择你的音乐")
    song_image = models.ImageField( upload_to='image/sufimage',verbose_name="封面图")
    IsDeleted = models.BooleanField(default=False)
    CreateTime = models.DateTimeField(auto_now_add=True)
    UpdateTime = models.DateTimeField(auto_now=True)

    def get_image_field(self):
        return 'song_image'

    def get_image_path(self):
        return 'image/sufimage/'

    def get_file_field(self):
        return 'song_file'

    def get_file_path(self):
        return 'music/musicfile/'