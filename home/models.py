from django.db import models
from ckeditor.fields import RichTextField
# Create your models here.


class Home(models.Model):

    body = RichTextField(blank=True, null=True)
    title = models.CharField(max_length=255)
    profilePicture = models.ImageField(null=True, blank=True, upload_to='home/images')
    #TO DO:
    ##PROJECT SLIDER
    ##CONTACT FORM

    def __str__(self):
        return self.title