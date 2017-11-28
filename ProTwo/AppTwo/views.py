from django.shortcuts import render
from django.http import HttpResponse
from AppTwo.models import Topic,Webpage,AccessRecord,User


# Create your views here.

def index(request):
    webpage_list = AccessRecord.objects.order_by('date')
    date_dict = {'access_records': webpage_list}
    my_dict = {'insert_me':"Motherfucker!!!"}
    return render(request, 'AppTwo/index.html',context=date_dict)

def help(request):
    new_dict = {'help_me': 'This is the new Help!'}
    return render(request,'AppTwo/help.html',context=new_dict)

def users(request):
    list_users = User.objects.order_by('first_name')
    user_dict = {'user_records': list_users}
    return render(request,'AppTwo/users.html',context=user_dict)
