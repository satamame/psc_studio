from django.db import models

from accounts.models import User


class PlayScript(models.Model):
    owner = models.ForeignKey(User, on_delete=models.CASCADE, default=None)
    title = models.CharField(max_length=50, default='名称未設定')
    plot = models.CharField(max_length=500, default='')

    def __str__(self):
        return self.title


class Character(models.Model):
    script = models.ForeignKey(
        PlayScript, on_delete=models.CASCADE, default=None)
    sortkey = models.IntegerField(default=0)
    name = models.CharField(max_length=50, default='名称未設定')
    desc = models.CharField(max_length=200, default='')
    sample = models.CharField(max_length=500, default='')

    def __str__(self):
        return self.name


class Scene(models.Model):
    script = models.ForeignKey(
        PlayScript, on_delete=models.CASCADE, default=None)
    sortkey = models.IntegerField(default=0)
    headline = models.CharField(max_length=50, default='名称未設定')
    chars = models.ManyToManyField(Character)
    sofar = models.CharField(max_length=500, default='')
    sofar_gen = models.CharField(max_length=500, default='')
    outline = models.CharField(max_length=500, default='')
    outline_gen = models.CharField(max_length=500, default='')
    lines = models.CharField(max_length=2000, default='')
    lines_gen = models.CharField(max_length=2000, default='')

    def __str__(self):
        return self.headline
