from django.db import models
from ckeditor.fields import RichTextField

# Create your models here.


class Category(models.Model):
    def __str__(self):
        return self.name
    name= models.CharField(max_length=30)

class Post(models.Model):
    def __str__(self):
        return self.title
    title = models.CharField (max_length=255)
    #body = models.TextField()
    body=RichTextField(blank=True, null=True)
    created_on = models.DateTimeField(auto_now_add=True)
    last_modified = models.DateTimeField(auto_now=True)
    categories = models.ManyToManyField('Category', related_name='posts')

class Comment(models.Model):
    author= models.CharField (max_length=60)
    body = models.TextField()
    created_on = models.DateTimeField(auto_now_add=True)
    post = models.ForeignKey('Post', on_delete= models.CASCADE)