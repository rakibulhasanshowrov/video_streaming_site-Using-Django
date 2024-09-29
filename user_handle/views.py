from django.shortcuts import render,HttpResponseRedirect
from user_handle.forms import loginForm,signupForm
from django.contrib.auth import authenticate,login,logout
from django.urls import reverse_lazy,reverse
from user_handle.models import UserProfile
# Create your views here.
def homepage(request):
  return render(request,'base.html',context={})

def login_user(request):
  form=loginForm()
  if request.method=="POST":
    form=loginForm(data=request.POST)
    if form.is_valid():
      username=form.cleaned_data.get('username')
      password=form.cleaned_data.get('password')
      user=authenticate(username=username,password=password)
      if user is not None:
        login(request,user)
        print(f'login Successful!')
        pass
        
        # return HttpResponseRedirect(reverse('app_post:home'))
        
  else:   
     return render(request,'user_handle/login.html',context={'form':form})
   
def create_user(request):
  form=signupForm()
  if request.method=="POST":
    form=signupForm(data=request.POST)
    if form.is_valid():
        user=form.save()
        user_profile=UserProfile(user=user)
        user_profile.save()
        print("User Created Successfully!")
    else:
      return render(request,'user_handle/user_registration.html',context={
      'form':form})
  else:    
    return render(request,'user_handle/user_registration.html',context={
      'form':form
    })