from django.db import models

# Create your models here.

class Project(models.Model):
    def __str__(self):
        return self.title
    title = models.CharField(max_length=100)
    description = models.TextField()
    technology = models.CharField(max_length = 20)
    # image = models.FilePathField(path='projects/static/projects' ) #first image
    image = models.ImageField(null=True, blank=True, upload_to='projects/images')
    images = models.ManyToManyField('Image', related_name='projects')
    repoGitLink = models.CharField(max_length=100, null=True, blank=True)
    runningProgramLink = models.CharField(max_length=100, null=True, blank=True)

class Image(models.Model):
    #give a name to the picture by its picture name
    # image = models.FilePathField(path='projects/static/projects')
    pic = models.ImageField(null=True, blank=True, upload_to='projects/images')
   #name=pic.name
