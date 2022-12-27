from django.shortcuts import render, redirect
from django.urls import reverse
from django.http import HttpResponse, HttpResponseRedirect
from django.template import loader
from tempfile import tempdir
from django.contrib.auth import authenticate, login,logout
from django.contrib import messages
from django.contrib.auth.decorators import login_required


# Create your views here.

def home(request):
  jobs = Job.objects.all()
  context = {
    'jobs': jobs
  }
  return render(request, 'home.html',context)

def registerPage(request):
      form = CreateUserForm()
      if request.method == 'POST':

          form = CreateUserForm(request.POST)
          if form.is_valid():
              form.save()
              user = form.cleaned_data.get('username')
              messages.success(request, 'Account was created for ' + user)
              return redirect('index')

      context = {'form': form}
      return render(request, 'register.html', context)

def loginPage(request):
    if request.method == 'POST':
        username = request.POST.get('username')
        password = request.POST.get('password')

        user = authenticate(request, username=username, password=password)

        if user is not None:
            login(request, user)
            return redirect('index')
        else:
            messages.info(request, 'username OR password is incorrect')
    context = {}
    return render(request, 'login.html', context)

def my_profile(request):
    context = {}
    return render(request, 'profile.html',context)

def delete(request, id):
  if request.method == 'POST':
    user = Job.objects.get(pk=id)
    user.delete()
  return HttpResponseRedirect(reverse('index'))