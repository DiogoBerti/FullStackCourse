from django.shortcuts import render
from AppTwo import forms
from django.http import HttpResponse
from AppTwo.models import Topic,Webpage,AccessRecord,User,Monster


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

def new_page(request):
    return render(request,'AppTwo/new.html')

def form_name_view(request):
    form = forms.FormName()

    if request.method == 'POST':
        form = forms.FormName(request.POST)

        if form.is_valid():
            print('_____________')
            print('Validating Data!')
            print('name: {}'.format(form.cleaned_data['name']))
            print('email: {}'.format(form.cleaned_data['email']))
            print('Text: {}'.format(form.cleaned_data['text_area']))
            print('_____________')

    return render(request,'AppTwo/form_page.html',context={'form':form})

def form_user(request):
    form = forms.NewUserForm()

    if request.method == 'POST':
        form = forms.NewUserForm(request.POST)

        if form.is_valid():
            form.save(commit=True)
            print('_____________')
            print('Validating Data!')
            print('_____________')
            return index(request)
        else:
            print('Error!')

    return render(request,'AppTwo/user_input.html',context={'form':form})

def form_monster(request):
    form = forms.MonsterForm()
    list_monsters = Monster.objects.order_by('name')
    monster_dict = {'monster_records': list_monsters}
    if request.method == 'POST':
        form = forms.MonsterForm(request.POST)

        if form.is_valid():
            form.save(commit=True)
            print('_____________')
            print('Validating Data!')
            print('_____________')
            return index(request)
        else:
            print('Error!')

    return render(request,'AppTwo/user_input.html',context={'form':form,
                                                            'monster_records': list_monsters})
