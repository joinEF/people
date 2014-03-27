from django.shortcuts import render, get_object_or_404

from django.contrib.auth.models import User

def index(request):

    users = User.objects.all()
    return render(request, 'index.html', {'users': users})

def profile(request, username):

    user = get_object_or_404(User, username=username)
    return render(request, 'profile.html', {'profile_user': user})

def about(request):

    return render(request, 'about.html')