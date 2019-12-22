from django.db import models
from apps.songs.models import Music
from datetime import datetime

# Create your models here.


class User(models.Model):
    """
    用户的基本信息表
    """
    sexs = (
        ('male', '男'),
        ('female', '女'),
    )
    username = models.CharField(verbose_name='用户名', max_length=30, unique=True)
    password = models.CharField(verbose_name='密码', max_length=20)
    sex = models.CharField(verbose_name='性别', max_length=6, choices=sexs, default='male')
    moblie = models.CharField(verbose_name='移动电话', max_length=11, blank=True, null=True)
    email = models.CharField(verbose_name='邮箱', max_length=100, blank=True, null=True)
    add_time = models.DateTimeField(verbose_name='添加时间', default=datetime.now)

    class Meta:
        db_table = 'User'
        verbose_name = '用户信息'
        verbose_name_plural = verbose_name

    def __str__(self):
        return self.username


class UserFav(models.Model):
    """
    用户收藏
    """
    user = models.ForeignKey(User, verbose_name='用户', on_delete=models.CASCADE)
    song = models.ForeignKey(Music, verbose_name='歌曲', on_delete=models.CASCADE)
    add_time = models.DateTimeField(verbose_name='添加时间', default=datetime.now)

    class Meta:
        db_table = 'UserFav'
        unique_together = ('user','song')
        verbose_name = '用户收藏'
        verbose_name_plural = verbose_name

    def __str__(self):
        return self.user.username


class PlayHistory(models.Model):
    """
    用户播放列表
    """
    user = models.ForeignKey(User, verbose_name='用户', on_delete=models.CASCADE)
    song = models.ForeignKey(Music, verbose_name='歌曲', on_delete=models.CASCADE)
    add_time = models.DateTimeField(verbose_name='添加时间', default=datetime.now)

    class Meta:
        db_table = 'PlayHistory'
        unique_together = ('user', 'song')
        verbose_name = '用户播放列表'
        verbose_name_plural = verbose_name

    def __str__(self):
        return self.user.username


class UserComment(models.Model):
    """
    用户评论
    """
    user = models.ForeignKey(User, verbose_name='用户', on_delete=models.CASCADE)
    song = models.ForeignKey(Music, verbose_name='歌曲', on_delete=models.CASCADE)
    context = models.TextField(verbose_name='评论内容')
    add_time = models.DateTimeField(verbose_name='添加时间', default=datetime.now)

    class Meta:
        db_table = 'UserComment'
        verbose_name = '用户评论'
        verbose_name_plural = verbose_name

    def __str__(self):
        return self.user.username

