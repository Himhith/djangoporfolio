from django.shortcuts import render
from home.models import Home

# Create your views here.

def home_detail(request):

    home = Home.objects.get(pk=1)



    context ={
         'home' : home,

    }

    return render(request, 'home_detail.html',context)