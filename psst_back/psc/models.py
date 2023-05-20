from django.db import models


class PlayScript(models.Model):
    title = models.CharField(max_length=50, default='名称未設定')
    plot = models.CharField(max_length=500, default='')


class Character(models.Model):
    sortkey = models.IntegerField(default=0)
    name = models.CharField(max_length=50, default='名称未設定')
    desc = models.CharField(max_length=200, default='')
    sample = models.CharField(max_length=500, default='')


class Scene(models.Model):
    sortkey = models.IntegerField(default=0)
    headline = models.CharField(max_length=50, default='名称未設定')
    chars = models.ManyToManyField(Character)
    sofar = models.CharField(max_length=500, default='')
    sofar_gen = models.CharField(max_length=500, default='')
    outline = models.CharField(max_length=500, default='')
    outline_gen = models.CharField(max_length=500, default='')
    lines = models.CharField(max_length=2000, default='')
    lines_gen = models.CharField(max_length=2000, default='')
