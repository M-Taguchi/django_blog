from django.conf import settings
from django.db import models
from django.utils import timezone
from markdownx.models import MarkdownxField

class Category(models.Model):
    name = models.CharField(max_length=255)

    def __str__(self):
        return self.name


class Tag(models.Model):
    name = models.CharField(max_length=255)

    def __str__(self):
        return self.name

# Create your models here.
class Post(models.Model):
    title = models.CharField(max_length=200)
    text = MarkdownxField()
    created_date = models.DateTimeField(default=timezone.now)
    updated_date = models.DateTimeField(blank=True, null=True)
    published_date = models.DateTimeField(blank=True, null=True)
    is_public = models.BooleanField(default=False)

    category = models.ForeignKey(Category, on_delete=models.PROTECT)
    tags = models.ManyToManyField(Tag, blank=True)

    class Meta:
        ordering = ['-created_date']

    def __str__(self):
        return self.title