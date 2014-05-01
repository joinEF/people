from django.shortcuts import render, get_object_or_404, redirect
from django.contrib.auth.decorators import login_required
from django.contrib.auth.models import User
from django.core.mail import send_mail
from django.http import HttpResponseRedirect, HttpResponseForbidden
from django.core.urlresolvers import reverse

from forms import JoinForm, UserForm, UserProfileForm, ProjectForm
import settings
from models import Project

def index(request):

    if request.user.is_authenticated():

        users = User.objects.all()
        return render(request, 'people.html', {'users': users})

    else:

        return render(request, 'marketing.html')

@login_required
def projects(request):

    projects = Project.objects.all()
    return render(request, 'projects.html', {'projects': projects})

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
        form = JoinForm()

    return render(request, 'join.html', {
        'form': form,
        'valid': valid
    })

@login_required
def manage_account(request):
    # http://stackoverflow.com/questions/569468/django-multiple-models-in-one-template-using-forms
    # http://collingrady.wordpress.com/2008/02/18/editing-multiple-objects-in-django-with-newforms/

    if request.method == 'POST':    

        user_form = UserForm(request.POST, instance=request.user)
        user_profile_form = UserProfileForm(request.POST, instance=request.user.profile)

        if user_form.is_valid() and user_profile_form.is_valid():

            user_form.save()
            user_profile_form.save()

            return HttpResponseRedirect(reverse(manage_account))

    else:

        user_form = UserForm(instance=request.user)
        user_profile_form = UserProfileForm(instance=request.user.profile)

    return render(request, 'manage_account.html', {
        'user_form': user_form,
        'user_profile_form': user_profile_form
    })

@login_required
def feedback(request):

    return render(request, 'feedback.html')

@login_required
def view_project(request, project_id):

    project = get_object_or_404(Project, pk=project_id)
    return render(request, 'view_project.html', {'project': project})


@login_required
def edit_project(request, project_id=None):
    # http://wiki.ddenis.com/index.php?title=Django,_add_and_edit_object_together_in_the_same_form

    if project_id:
        print "exists"
        project = get_object_or_404(Project, pk=project_id)
        if request.user not in project.users.all():
            return HttpResponseForbidden()
    else:
        print "doesn't exist"
        project = Project()

    if request.method == 'POST':

        form = ProjectForm(request.POST, instance=project)

        if form.is_valid():

            form.save()

            return HttpResponseRedirect(project.get_absolute_url())

    else:

        form = ProjectForm(instance=project)

    if project_id:
        template_name = 'edit_project.html'
    else:
        template_name = 'new_project.html'

    return render(request, template_name, {
        'form': form,
        'project': project
    })


@login_required
def delete_project(request, project_id):

    project = get_object_or_404(Project, pk=project_id)
    if request.user not in project.users.all():
        return HttpResponseForbidden()
    project.delete()
    return redirect(request.user)