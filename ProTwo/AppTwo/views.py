from django.shortcuts import render
from django.http import HttpResponse

# Create your views here.

def index(request):
    my_dict = {'insert_me':"Motherfucker!!!"}
    return render(request, 'AppTwo/index.html',context=my_dict)

def help(request):
    new_dict = {'help_me': 'This is the new Help!'}
    return render(request,'AppTwo/help.html',context=new_dict)
