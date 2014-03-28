from django.shortcuts import render, get_object_or_404
from django.contrib.auth.decorators import login_required
from django.contrib.auth.models import User
from django.core.mail import send_mail

from forms import JoinForm
import settings

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

    valid = False

    if request.method == 'POST':

        form = JoinForm(request.POST)

        if form.is_valid():

            email = form.cleaned_data['email']
            first_name = form.cleaned_data['first_name']
            last_name = form.cleaned_data['last_name']
            university = form.cleaned_data['university']
            degree_subject = form.cleaned_data['degree_subject']
            graduation_year = form.cleaned_data['graduation_year'] 

            subject = "%s %s has requested to join Founder School"
            subject = subject % (first_name, last_name)
            message = """%s %s has requested to join Founder School\n
\n
Email: %s\n
University: %s\n
Degree subject: %s\n
Graduation year: %s
"""
            message = message % (first_name, last_name, email, university, degree_subject, graduation_year)

            from_email = "noreply@effounderschool.com"
            recipient_list = settings.REQUEST_TO_JOIN_EMAILS
            
            send_mail(subject, message, from_email, recipient_list, fail_silently=False)

            valid = True

    else:
        form = JoinForm() # An unbound form

    return render(request, 'join.html', {
        'form': form,
        'valid': valid
    })

@login_required
def manage_account(request):

    return render(request, 'in_progress.html')

@login_required
def feedback(request):

    return render(request, 'feedback.html')