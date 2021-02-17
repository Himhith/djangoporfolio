from django.shortcuts import render
from home.models import Home
from django.core.mail import  send_mail
from djangoportfo.settings import EMAIL_HOST_USER
# Create your views here.

def home_detail(request):

    home = Home.objects.get(pk=1)



    context ={
         'home' : home,

    }
    if request.method =="POST" :
        message_name = request.POST['txtName']
        message_phone =request.POST['txtPhone']
        message_email = request.POST['txtEmail']
        message_message = request.POST['txtMsg']
        context['message_name'] = message_name
        context['message_phone'] = message_phone
        context['message_email'] = message_email
        context['message_message'] = message_message

        #send email

        send_mail('Contact Form from'+message_message,
                  message_message+"\n given phone number: "+message_phone+"\n given email adress: "+message_email,
                  'michal.ogorzalek@zohomail.eu',
                  ['michal.ogorzalek@gmail.com'])
        return render(request, 'home_detail.html', context)
    else:
        return render(request, 'home_detail.html',context)