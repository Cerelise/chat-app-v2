from django.db import models
from django.contrib.auth.models import User
from django.utils import timezone
from django.utils.timezone import now


# Create your models here.
class ArticleSeries(models.Model):
    title = models.CharField(max_length=200)
    # subtitle = models.CharField(max_length=200, default='', blank=True)
    # slug = models.SlugField("分类", null=False, blank=False, unique=True)
    published = models.DateTimeField(default=timezone.now)

    class Meta:
        verbose_name_plural = "Series"
        ordering = ['-published']


class Article(models.Model):
    title = models.CharField(max_length=200)
    subtitle = models.CharField(max_length=200, default="", blank=True)
    # article_slug = models.SlugField("笔记分类", null=False, blank=False, unique=True)
    content = models.TextField()
    published = models.DateTimeField(auto_now_add=True, blank=True, null=True)
    # modified = models.DateTimeField("最后编辑", default=timezone.now)
    # series = models.ForeignKey(ArticleSeries,
    #                            default="",
    #                            verbose_name="Series",
    #                            on_delete=models.SET_DEFAULT)
    # view = models.IntegerField(default=0)
    belong = models.ForeignKey(User,
                               on_delete=models.CASCADE,
                               null=True,
                               blank=True,
                               related_name='article_user')

    def __str__(self):
        return self.title

    # @property
    # def slug(self):
    #     return self.article_slug

    class Meta:
        verbose_name_plural = "Article"
        ordering = ['-published']