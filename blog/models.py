from django.db import models
from ckeditor.fields import RichTextField
from django.utils import timezone


class Post(models.Model):
    body=RichTextField(blank=True,null=True)