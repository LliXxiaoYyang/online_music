from django.db import models
from datetime import datetime

# Create your models here.


class Singers(models.Model):
    """
    歌手信息
    """
    sexs = (
        ('male', '男'),
        ('female', '女'),
    )
    singer_name = models.CharField(verbose_name='歌手名', max_length=30)
    sex = models.CharField(verbose_name='性别', max_length=6, choices=sexs, default='male')
    birthday = models.DateTimeField(verbose_name="添加时间", null=True)
    desc = models.TextField(verbose_name='歌手介绍', max_length=500, null=True)
    search_num = models.IntegerField(verbose_name='搜索量', default=0)
    image = models.ImageField(verbose_name='歌手图片', upload_to='images/', null=True)
    add_time = models.DateTimeField(verbose_name="添加时间", default=datetime.now)

    class Meta:
        db_table = 'Singers'
        verbose_name = '歌手信息'
        verbose_name_plural = verbose_name

    def __str__(self):
        return self.singer_name



class Album(models.Model):
    """
    专辑信息
    """
    album_name = models.CharField(verbose_name='专辑名', max_length=30)
    singer = models.ForeignKey(Singers, verbose_name='歌手', on_delete=models.CASCADE)
    desc = models.TextField(verbose_name='专辑介绍', max_length=500, null=True)
    image = models.ImageField(verbose_name='专辑图片', upload_to='images/', null=True)
    play_num = models.IntegerField(verbose_name='播放量', default=0)
    add_time = models.DateTimeField(verbose_name="添加时间", default=datetime.now)

    class Meta:
        db_table = 'Album'
        verbose_name = '专辑信息'
        verbose_name_plural = verbose_name

    def __str__(self):
        return self.album_name


class Music(models.Model):
    """
    歌曲信息
    """
    songname = models.CharField(verbose_name='歌曲名', max_length=100, unique=True)
    songurl = models.FilePathField(verbose_name='歌曲文件地址', path='music/')
    singer = models.ForeignKey(Singers, verbose_name='歌手', on_delete=models.CASCADE)
    album = models.ForeignKey(Album, verbose_name='专辑', on_delete=models.CASCADE)
    type = models.CharField(verbose_name='歌曲类型', max_length=30)
    search_num = models.IntegerField(verbose_name='搜索量', default=0)
    download_num = models.IntegerField(verbose_name='下载量', default=0)
    play_num = models.IntegerField(verbose_name='播放量', default=0)
    is_new = models.BooleanField(verbose_name="是否新歌", default=False)
    is_hot = models.BooleanField(verbose_name="是否热歌", default=False)
    add_time = models.DateTimeField(verbose_name="添加时间", default=datetime.now)

    class Meta:
        db_table = 'Music'
        verbose_name = '歌曲信息'
        verbose_name_plural = verbose_name

    def __str__(self):
        return self.songname


class Lyric(models.Model):
    """
    歌词信息
    """
    song = models.ForeignKey(Music, verbose_name='歌曲', on_delete=models.CASCADE)
    lyric_url = models.FilePathField(verbose_name='歌词文件地址', path='music/')

    class Meta:
        db_table = 'Lyric'
        verbose_name = '歌词信息'
        verbose_name_plural = verbose_name

    def __str__(self):
        return self.song.songname


