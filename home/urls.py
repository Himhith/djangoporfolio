from django.urls import path
from . import views

urlpatterns = [
   # path('admin/', admin.site.urls),
    path('', views.home_detail, name= 'home_detail'),

]
