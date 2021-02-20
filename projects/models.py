from django.db import models

# Create your models here.

class Project(models.Model):
    def __str__(self):
        return self.title
    title = models.CharField(max_length=100)
    description = models.TextField()
    technology = models.CharField(max_length = 20)
    image = models.ImageField(null=True, blank=True, upload_to='projects/images')
    #first image to activate slider and to be shown in thumbnail
    images = models.ManyToManyField('Image', related_name='projects')
    repoGitLink = models.CharField(max_length=100, null=True, blank=True)
    runningProgramLink = models.CharField(max_length=100, null=True, blank=True)

class Image(models.Model):
    #give a name to the picture by its picture name
    pic = models.ImageField(null=True, blank=True, upload_to='projects/images')
