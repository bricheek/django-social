from django.contrib.auth import login
from django.urls import reverse
from django.shortcuts import render, redirect
from .models import Dweet,Profile
from .forms import DweetForm, CustomUserCreationForm

def dashboard(request):
    form = DweetForm(request.POST or None)
    if request.method == "POST":
        if form.is_valid():
            dweet = form.save(commit=False)
            dweet.user = request.user
            dweet.save()
            return redirect("dwitter:dashboard")
    followed_dweets = Dweet.objects.filter(
    user__profile__in=request.user.profile.follows.all()
    ).order_by("-created_at")
    return render(request, "dwitter/dashboard.html", 
    {"form": form, "dweets": followed_dweets},
    )

def register(request):
    if request.method == "GET":
        return render (
            request, "register.html",
            { "form": CustomUserCreationForm }
        )
    elif request.method == "POST":
        form = CustomUserCreationForm(request.POST)
        if form.is_valid():
            user = form.save()
            login(request, user)
            return redirect(reverse("/"))


def profile_list(request):
    profiles = Profile.objects.exclude(user=request.user)
    return render(request, "dwitter/profile_list.html", {"profiles":profiles})

def profile(request, pk):
    # check if there is a user profile, if not add it.
    if not hasattr(request.user, 'profile'):
        missing_profile = Profile(user=request.user)
        missing_profile.save()
    # respond to action of clicking follow or unfollow
    profile = Profile.objects.get(pk=pk)
    if request.method == "POST":
        current_user_profile = request.user.profile
        data = request.POST
        action = data.get("follow")
        if action == "follow":
            current_user_profile.follows.add(profile)
        elif action == "unfollow":
            current_user_profile.follows.remove(profile)
        current_user_profile.save()
    return render(request, "dwitter/profile.html",{"profile":profile})