from django.db import IntegrityError
from django.shortcuts import render, redirect
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User
from django.http import HttpResponse
from django.contrib.auth import login

def signupuser(request):
    if request.method == 'GET':
       return render(request, 'todo/signupuser.html', {'form':UserCreationForm()})
    else:
        if request.POST['password1']==request.POST['password2']:

        #create a new user
            try:
              user=User.objects.create_user(request.POST['username'], password=request.POST['password1'])
              user.save()
              login(request, user)
              return redirect('currenttodos')
            except IntegrityError:
                return render(request, 'todo/signupuser.html', {'form':UserCreationForm(), 'error':'The username has already been taken, please choose a different username'})
               

        else:
            #Tell the user the passwords didnt match
            return render(request, 'todo/signupuser.html', {'form':UserCreationForm(), 'error':'Passwords didnt match'})

def currenttodos(request):
    return render(request, 'todo/currenttodos.html')
    


# Create your views here.
