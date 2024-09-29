from django.shortcuts import render,HttpResponseRedirect
from user_handle.forms import loginForm
from django.contrib.auth import authenticate,login,logout
from django.urls import reverse_lazy,reverse
# Create your views here.
def homepage(request):
  return render(request,'base.html',context={})

def login_user(request):
  form=loginForm()
  if request.method=="POST":
    form=loginForm(data=request.POST)
    if form.is_valid():
      username=form.cleaned_data.get(username)
      password=form.cleaned_data.get('password')
      user=authenticate(username=username,password=password)
      if user is not None:
        login(request,user)
        # return HttpResponseRedirect(reverse('app_post:home'))
        
      
    
  return render(request,'user_handle/login.html',context={'form':form})