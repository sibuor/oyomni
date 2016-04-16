from django.db import models
from django.conf import settings
from django.contrib.auth.models import User
from django.core.urlresolvers import reverse
from django.contrib.auth import get_user_model as user_model
from django.utils import timezone
# Create your models here.

class Tag(models.Model):
    slug = models.SlugField(max_length=300, unique=True)

    def __str__(self):
        return self.slug

class EntryQuerySet(models.QuerySet):
    def published(self):
        return self.filter(publish=True)

class Entry(models.Model):
    user = models.ForeignKey(settings.AUTH_USER_MODEL,on_delete=models.CASCADE,)
    #user = models.ForeignKey(settings.AUTH_USER_MODEL)
    author = models.CharField(max_length=200)
    title = models.CharField('Headline',max_length=100)
    title_detail = models.CharField('Headline detail',max_length=100)
    body = models.TextField()
    image = models.ImageField(upload_to ='title_images/%Y/%m/%d', blank=True)
    slug = models.SlugField(max_length=300, unique=True)
    publish = models.BooleanField(default=True)
    created = models.DateTimeField()
    modified = models.DateTimeField()
    tags = models.ManyToManyField(Tag)

    objects = EntryQuerySet.as_manager()

    def __str__(self):
        return self.title


    def approved_comments(self):
        return self.comments.filter(approved_comment=True)


    def get_absolute_url(self):
        return reverse("entry_detail", kwargs={"slug":self.slug})
        pass

    class Meta:
        verbose_name = "Blog Entry"
        verbose_name_plural = "Blog Entries"
        ordering = ["-created"]




class Comment(models.Model):
    entry = models.ForeignKey('blog2.Entry', related_name='comments')
    author = models.CharField(max_length=200)
    text = models.TextField()
    created = models.DateTimeField(default=timezone.now)
    approved_comment = models.BooleanField(default=False)

    def approve(self):
        self.approved_comment = True
        self.save()

    def __str__(self):
        return self.text










