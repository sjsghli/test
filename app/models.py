from django.contrib.auth.models import AbstractUser
from django.db import models
from autoslug import AutoSlugField
from taggit.managers import TaggableManager
from django.conf import settings


# Create your models here.
# 
# 
class Subject(models.Model):
    name = models.CharField(max_length=255)
    slug = AutoSlugField(populate_from='name', unique=True)
# 
# 
# 
class Article(models.Model):
    class Status(models.TextChoices):
            DRAFT = 'draft', 'Draft'
            PUBLISHED = 'published', 'Published'
            
            
    status = models.CharField(max_length=20, choices=Status.choices, default=Status.DRAFT)
    title = models.CharField(max_length=1000)
    slug = AutoSlugField(populate_from='title', unique=True)
    text = models.TextField(blank=True)
    summary = models.TextField(blank=True)
    meta_description = models.CharField(max_length=160, blank=True)
    subject = models.ForeignKey(Subject, on_delete=models.PROTECT)
    published = models.DateTimeField(null=True, blank=True)  # set manually when publishing
    created = models.DateTimeField(auto_now_add=True)
    updated = models.DateTimeField(auto_now=True)
    author = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.PROTECT)
    hero_image = models.ImageField(upload_to='articles/%Y/%m/', blank=True)
    hero_text = models.CharField(max_length=1000, blank=True)
    video = models.URLField(blank=True)
    tags=TaggableManager(blank=True)
    
    @property
    def reading_time_minutes(self):
        word_count = len(self.text.split())
        return max(1, round(word_count / 200))

    def __str__(self):
        return self.title
    
    class Meta:
        ordering = ['-published']

class ArticleImage(models.Model):
    article = models.ForeignKey(Article, on_delete=models.CASCADE)
    image = models.ImageField(upload_to='article_images/%Y/%m/', blank=True)
    alt_text = models.CharField(max_length=1000, blank=True)
    caption = models.CharField(max_length=1000, blank=True)
