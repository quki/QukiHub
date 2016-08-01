"""
Definition of models.
MVC pattern
Model: 데이터를 관리
"""

from django.db import models  # 모듈 import
from ckeditor.fields import RichTextField
from django.core.urlresolvers import reverse
from . import category_config


class Category(models.Model):
    main = models.CharField(max_length=30, choices=category_config.POST_MAIN_CHOICES)
    sub = models.CharField(max_length=30, unique=True)

    def __str__(self):  # __unicode__ on Python 2
        return "%s - %s" % (self.main, self.sub)

    class Meta:
        verbose_name = "Post Category"
        verbose_name_plural = "Post Categories"


class EntryQuerySet(models.QuerySet):
    def published(self):
        return self.filter(publish=True)


class Post(models.Model):
    title = models.CharField(max_length=100)
    overview = models.TextField(max_length=150)
    number = models.AutoField(primary_key=True)
    content = RichTextField()
    category = models.ForeignKey(Category, default=None, on_delete=models.PROTECT)
    created = models.DateTimeField(auto_now_add=True, blank=True)
    modified = models.DateTimeField(auto_now=True, blank=True)
    slug = models.SlugField(max_length=200, unique=True)
    publish = models.BooleanField(default=True)
    objects = EntryQuerySet.as_manager()  # ????

    def __str__(self):
        return self.title

    def get_absolute_url(self):
        return reverse("entry_detail", kwargs={"slug": self.slug})

    class Meta:
        verbose_name = "Blog Post"
        verbose_name_plural = "Blog Posts"
        ordering = ["-created"]


