from django.shortcuts import render, HttpResponseRedirect, get_object_or_404
from user_handle.forms import loginForm, signupForm
from django.contrib.auth import authenticate, login, logout
from django.urls import reverse_lazy, reverse
from user_handle.models import UserProfile
from django.contrib.auth.decorators import login_required
from .forms import UserProfileForm

# Messages
from django.contrib import messages


# Create your views here.
def login_user(request):
    form = loginForm()
    # print(form)
    if request.method == "POST":
        print(f"Post Accessed")
        form = loginForm(data=request.POST)
        if form.is_valid():
            username = form.cleaned_data.get("username")
            password = form.cleaned_data.get("password")
            user = authenticate(username=username, password=password)
            if user is not None:
                login(request, user)
                print(f"login Accessed")
                messages.success(request, "Login Successfull!")
                return HttpResponseRedirect(reverse("app_video:homepage"))
    else:
        return render(request, "user_handle/login.html", context={"form": form})


def create_user(request):
    form = signupForm()
    if request.method == "POST":
        form = signupForm(data=request.POST)
        if form.is_valid():
            user = form.save()
            user_profile = UserProfile(user=user)
            user_profile.save()
            print("Account Created Successfully!")
            messages.success(request, "Account Created Successfully!")
            return HttpResponseRedirect(reverse("app_video:homepage"))
        else:
            print("UnSuccessfull!")
            return render(
                request, "user_handle/user_registration.html", context={"form": form}
            )
    method = str(request.method)
    print(f"Post Not  Accessed & Method:{method}")
    return render(request, "user_handle/user_registration.html", context={"form": form})


def userProfile(request):
    user = request.user
    profile = get_object_or_404(UserProfile, user=user)
    print(profile)
    return render(
        request,
        "user_handle/user_profile.html",
        context={
            "profile": profile,
        },
    )


def editprofile(request):
    # Load the user's profile if it exists, or create a new one
    user_profile = UserProfile.objects.get(user=request.user)
    form = UserProfileForm(instance=user_profile)  # Pass the user's profile instance to pre-fill the form

    if request.method == "POST":
        form = UserProfileForm(data=request.POST, files=request.FILES, instance=user_profile)  # Include files for image upload
        if form.is_valid():
            profile = form.save(commit=False)
            profile.user = request.user
            profile.save()
            messages.success(request, "Profile Updated Successfully!")
            return HttpResponseRedirect(reverse("user_handle:profile"))
        else:
            messages.error(request, "Failed to update profile. Please check the form for errors.")
    
    return render(request, "user_handle/edit_profile.html", context={"form": form})


@login_required
def logout_user(request):
    logout(request)
    messages.success(request, "You have successfully logged out.")
    return HttpResponseRedirect(reverse("app_video:homepage"))
