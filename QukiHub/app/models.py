"""
Definition of models.
MVC pattern
Model: 데이터를 관리

null=True Vs. blank=True
CHAR and TEXT types are never saved as NULL by Django, so null=True is unnecessary.
"""
from django.db import models  # 모듈 import
from ckeditor.fields import RichTextField
from django.core.urlresolvers import reverse
from . import category_config
from taggit.managers import TaggableManager


class CategoryPost(models.Model):
    child = models.CharField(max_length=10, primary_key=True, choices=category_config.POST_CHILD_CHOICES)
    parent = models.CharField(max_length=10, choices=category_config.POST_PARENT_CHOICES)

    def __str__(self):
        return "%s(%s)" % (self.child, self.parent)

    class Meta:
        verbose_name = "Category(Post)"
        verbose_name_plural = "Categories(Post)"


class EntryQuerySet(models.QuerySet):
    def published(self):
        return self.filter(publish=True)


class Post(models.Model):
    number = models.AutoField(primary_key=True)
    title = models.CharField(max_length=100)
    overview = models.TextField(max_length=150)
    content = RichTextField()
    category = models.ForeignKey(
        CategoryPost,
        default='etc',
        null=True,
        on_delete=models.SET_DEFAULT,
    )
    created = models.DateTimeField()
    modified = models.DateTimeField(auto_now=True)
    slug = models.SlugField(max_length=200, unique=True)
    publish = models.BooleanField(default=True)
    tags = TaggableManager()
    objects = EntryQuerySet.as_manager()  # ????

    def __str__(self):
        return self.title

    def get_absolute_url(self):
        return reverse("post_item", kwargs={"slug": self.slug})

    class Meta:
        verbose_name = "Post"
        verbose_name_plural = "Posts"
        ordering = ["-created"]
