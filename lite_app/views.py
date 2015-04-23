from django.shortcuts import render
from django.http import HttpResponse, HttpResponseRedirect
from lite_app.forms import UserForm, UserProfileForm, UserFormChange, UserProfileFormChange
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.decorators import login_required
from lite_app.models import UserProfile
from django.contrib.auth.models import User
from django.core.mail import send_mail
from django.conf import settings
# Create your views here.

def index(request):
    current_user=request.user
    context_dict = {'boldmessage': 'Hi there!', "cur_user":current_user}
    return render(request, 'lite_app/index.html', context_dict)


def register(request):
    args={}
    registered=False

    if request.method=='POST':
        user_form=UserForm(data=request.POST)
        profile_form=UserProfileForm(data=request.POST)
        args['user_form']=user_form
        args['profile_form']=profile_form
        if user_form.is_valid() and profile_form.is_valid():
            user=user_form.save()
            user.set_password(user.password)
            user.save()

            profile=profile_form.save(commit=False)
            profile.user=user

            if 'picture' in request.FILES:
                profile.picture=request.FILES['picture']

            profile.save()

            registered=True
            
            username = user_form.cleaned_data['username']
            email = user_form.cleaned_data['email']
            password = user_form.cleaned_data['password']
            
            return HttpResponseRedirect('/lite/')
            
            #email_subject = 'Подтверждение регистрации'
            #email_body = "Hey {0}, thanks for signing up. Here is your username: {0}, and password: {1}".format(username, password)
            #if username and email and password:
            #    send_mail(email_subject, email_body, settings.EMAIL_HOST_USER,
            #            [email], fail_silently=False)
            #    return HttpResponseRedirect('/lite/')
            #else:
            #    pass

        else:
            print (user_form.errors, profile_form.errors)

    else:
        user_form= UserForm()
        profile_form= UserProfileForm()

    return render(request, 'lite_app/register.html',
        {'user_form': user_form, 'profile_form':profile_form, 'registered': registered})


def user_login(request):
    if request.method=='POST':
        username= request.POST.get('username')
        password= request.POST.get('password')

        user=authenticate(username=username, password=password)

        if user:
            if user.is_active:
                login(request, user)
                return HttpResponseRedirect('/lite/')
            else:
                return HttpResponse("Your account is inactive!")
        else:
            print ("Invalid login details: {0}, {1}". format(username, password))
            return HttpResponse("Invalid login details supplied")
    else:
        return render(request, 'lite_app/login.html', {})

@login_required
def user_logout(request):
    logout(request)
    return HttpResponseRedirect('/lite/')
        
def delete_profile(request):
    current_user=request.user.id
    user=User.objects.get(id=current_user)
    user.delete()
    #userp=UserProfile.objects.get(user=current_user)
    return HttpResponseRedirect('/lite/')
    #return HttpResponse("Your account is inactive!")

@login_required
def user_profile(request):
     if request.method == 'GET':
        current_user=request.user.id
        user=User.objects.get(id=current_user)
        userp=UserProfile.objects.get(user=current_user)
        profile_form= UserProfileForm()
        profile_change_form= UserProfileFormChange()
        context_dict={'cur_user':current_user, 'user':user, 'userp':userp, 'profile_form':profile_form, 'profile_change_form': profile_change_form}
        return render(request, 'lite_app/profile.html', context_dict)
