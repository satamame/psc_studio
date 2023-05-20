# Generated by Django 4.2.1 on 2023-05-20 07:24

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Character',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('sortkey', models.IntegerField(default=0)),
                ('name', models.CharField(default='名称未設定', max_length=50)),
                ('desc', models.CharField(default='', max_length=200)),
                ('sample', models.CharField(default='', max_length=500)),
            ],
        ),
        migrations.CreateModel(
            name='PlayScript',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(default='名称未設定', max_length=50)),
                ('plot', models.CharField(default='', max_length=500)),
            ],
        ),
        migrations.CreateModel(
            name='Scene',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('sortkey', models.IntegerField(default=0)),
                ('headline', models.CharField(default='名称未設定', max_length=50)),
                ('sofar', models.CharField(default='', max_length=500)),
                ('sofar_gen', models.CharField(default='', max_length=500)),
                ('outline', models.CharField(default='', max_length=500)),
                ('outline_gen', models.CharField(default='', max_length=500)),
                ('lines', models.CharField(default='', max_length=2000)),
                ('lines_gen', models.CharField(default='', max_length=2000)),
                ('chars', models.ManyToManyField(to='psc.character')),
            ],
        ),
    ]