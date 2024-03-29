# Generated by Django 2.1.7 on 2019-12-21 19:28

import datetime
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Album',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('album_name', models.CharField(max_length=30, verbose_name='专辑名')),
                ('desc', models.TextField(max_length=500, null=True, verbose_name='专辑介绍')),
                ('image', models.ImageField(null=True, upload_to='images/', verbose_name='专辑图片')),
                ('play_num', models.IntegerField(default=0, verbose_name='播放量')),
                ('add_time', models.DateTimeField(default=datetime.datetime.now, verbose_name='添加时间')),
            ],
            options={
                'verbose_name': '专辑信息',
                'verbose_name_plural': '专辑信息',
                'db_table': 'Album',
            },
        ),
        migrations.CreateModel(
            name='Lyric',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('lyric_url', models.FilePathField(path='music/', verbose_name='歌词文件地址')),
            ],
            options={
                'verbose_name': '歌词信息',
                'verbose_name_plural': '歌词信息',
                'db_table': 'Lyric',
            },
        ),
        migrations.CreateModel(
            name='Music',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('songname', models.CharField(max_length=100, unique=True, verbose_name='歌曲名')),
                ('songurl', models.FilePathField(path='music/', verbose_name='歌曲文件地址')),
                ('type', models.CharField(max_length=30, verbose_name='歌曲类型')),
                ('search_num', models.IntegerField(default=0, verbose_name='搜索量')),
                ('download_num', models.IntegerField(default=0, verbose_name='下载量')),
                ('play_num', models.IntegerField(default=0, verbose_name='播放量')),
                ('is_new', models.BooleanField(default=False, verbose_name='是否新歌')),
                ('is_hot', models.BooleanField(default=False, verbose_name='是否热歌')),
                ('add_time', models.DateTimeField(default=datetime.datetime.now, verbose_name='添加时间')),
                ('album', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='songs.Album', verbose_name='专辑')),
            ],
            options={
                'verbose_name': '歌曲信息',
                'verbose_name_plural': '歌曲信息',
                'db_table': 'Music',
            },
        ),
        migrations.CreateModel(
            name='Singers',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('singer_name', models.CharField(max_length=30, verbose_name='歌手名')),
                ('sex', models.CharField(choices=[('male', '男'), ('female', '女')], default='male', max_length=6, verbose_name='性别')),
                ('birthday', models.DateTimeField(null=True, verbose_name='添加时间')),
                ('desc', models.TextField(max_length=500, null=True, verbose_name='歌手介绍')),
                ('search_num', models.IntegerField(default=0, verbose_name='搜索量')),
                ('image', models.ImageField(null=True, upload_to='images/', verbose_name='歌手图片')),
                ('add_time', models.DateTimeField(default=datetime.datetime.now, verbose_name='添加时间')),
            ],
            options={
                'verbose_name': '歌手信息',
                'verbose_name_plural': '歌手信息',
                'db_table': 'Singers',
            },
        ),
        migrations.AddField(
            model_name='music',
            name='singer',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='songs.Singers', verbose_name='歌手'),
        ),
        migrations.AddField(
            model_name='lyric',
            name='song',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='songs.Music', verbose_name='歌曲'),
        ),
        migrations.AddField(
            model_name='album',
            name='singer',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='songs.Singers', verbose_name='歌手'),
        ),
    ]
