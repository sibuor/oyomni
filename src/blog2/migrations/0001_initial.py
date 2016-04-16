# -*- coding: utf-8 -*-
# Generated by Django 1.9.5 on 2016-04-15 20:01
from __future__ import unicode_literals

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='Entry',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('author', models.CharField(max_length=200)),
                ('title', models.CharField(max_length=100, verbose_name='Headline')),
                ('title_detail', models.CharField(max_length=100, verbose_name='Headline detail')),
                ('body', models.TextField()),
                ('image', models.ImageField(blank=True, upload_to='title_images/%Y/%m/%d')),
                ('slug', models.SlugField(max_length=300, unique=True)),
                ('publish', models.BooleanField(default=True)),
                ('created', models.DateTimeField()),
                ('modified', models.DateTimeField()),
            ],
            options={
                'verbose_name_plural': 'Blog Entries',
                'verbose_name': 'Blog Entry',
                'ordering': ['-created'],
            },
        ),
        migrations.CreateModel(
            name='Tag',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('slug', models.SlugField(max_length=300, unique=True)),
            ],
        ),
        migrations.AddField(
            model_name='entry',
            name='tags',
            field=models.ManyToManyField(to='blog2.Tag'),
        ),
        migrations.AddField(
            model_name='entry',
            name='user',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL),
        ),
    ]
