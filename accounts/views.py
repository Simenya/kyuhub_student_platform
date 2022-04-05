from django.shortcuts import render, redirect
from django.contrib.auth.forms import UserCreationForm
from django.contrib import messages
from .forms import UserForm

def register(request):
    if request.method == 'POST':
        form = UserForm(request.POST)
        if form.is_valid():
            form.save()
            username = form.cleaned_data.get('username')
            messages.success(request, f'Account Has been Created For {username}!!')
            return redirect('login')
        else:
            print('*********form Not Valid*********')

    else:
        form = UserForm()
        print('Registration failed******')
    cnx = {'form':form}
    return render(request, 'account/register.html', cnx)

# def login(request):
#     cnx = {}
#     return render(request, 'account/login.html', cnx)