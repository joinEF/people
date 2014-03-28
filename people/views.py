from django.shortcuts import render, get_object_or_404
from django.contrib.auth.decorators import login_required
from django.contrib.auth.models import User

def index(request):

    if request.user.is_authenticated():

        users = User.objects.all()
        return render(request, 'people.html', {'users': users})

    else:

        return render(request, 'marketing.html')

@login_required
def profile(request, username):

    user = get_object_or_404(User, username=username)
    return render(request, 'profile.html', {'profile_user': user})


def join(request):

    return render(request, 'in_progress.html')

@login_required
def manage_account(request):

    return render(request, 'in_progress.html')

@login_required
def feedback(request):

    return render(request, 'in_progress.html')