from django.shortcuts import render, get_object_or_404

from django.contrib.auth.models import User

def index(request):

    if request.user.is_authenticated():

        users = User.objects.all()
        return render(request, 'people.html', {'users': users})

    else:

        return render(request, 'marketing.html')

def profile(request, username):

    user = get_object_or_404(User, username=username)
    return render(request, 'profile.html', {'profile_user': user})