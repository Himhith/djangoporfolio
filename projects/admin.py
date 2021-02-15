from django.contrib import admin
from projects.models import Project, Image

class ProjectAdmin (admin.ModelAdmin):
    pass
class ImageAdmin (admin.ModelAdmin):
    pass

admin.site.register(Project,ProjectAdmin)
# Register your models here.
admin.site.register(Image,ImageAdmin)