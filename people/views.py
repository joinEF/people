from django.shortcuts import render, get_object_or_404

from django.contrib.auth.models import User

def index(request):

    users = User.objects.all()

    people = [
        {
            'university': 'Cambridge',
            'graduation_year': 2013,
            'location': 'London',
            'twitter': 'CalumJEadie',
            'github': 'CalumJEadie',
            'linkedin': 'calumjeadie',
            'url': 'http://calumjeadie.com',
            'user': users[0],
            'get_absolute_url': '/CalumJEadie',
            'degree_subject': 'CS'
        },
        {
            'university': 'Cambridge',
            'graduation_year': 2013,
            'location': 'London',
            'twitter': 'jordnb',
            'github': 'jordn',
            'linkedin': 'jordanburgess',
            'url': 'http://jordanburgess.com/',
            'user': users[1],
            'get_absolute_url': '/jordnb',
            'degree_subject': 'Engineering'
        },
        {
            'university': 'Cambridge',
            'graduation_year': 2013,
            'location': 'London',
            'twitter': 'FraserAtkins',
            'linkedin': 'fraseratkins',
            'url': 'http://www.fraseratkins.com/',
            'user': users[2],
            'get_absolute_url': '/FraserAtkins',
            'degree_subject': 'Engineering'
        },
        {
            'university': 'Imperial & Oxford',
            'graduation_year': 2012,
            'location': 'London',
            'twitter': 'joeroot',
            'linkedin': 'josephsroot',
            'url': 'http://joeroot.com/',
            'user': users[3],
            'get_absolute_url': '/joeroot',
            'degree_subject': 'CS'
        }
    ]

    return render(request, 'index.html', {'people': people})

def profile(request, username):

    user = get_object_or_404(User, username=username)

    people = {
        'CalumJEadie' : {
            'university': 'Cambridge',
            'graduation_year': 2013,
            'location': 'London',
            'twitter': 'CalumJEadie',
            'github': 'CalumJEadie',
            'linkedin': 'calumjeadie',
            'url': 'http://calumjeadie.com',
            'user': user,
            'get_absolute_url': '/CalumJEadie',
            'degree_subject': 'CS'
        },
        'jordnb': {
            'university': 'Cambridge',
            'graduation_year': 2013,
            'location': 'London',
            'twitter': 'jordnb',
            'github': 'jordn',
            'linkedin': 'jordanburgess',
            'url': 'http://jordanburgess.com/',
            'user': user,
            'get_absolute_url': '/jordnb',
            'degree_subject': 'CS'
        },
        'FraserAtkins': {
            'university': 'Cambridge',
            'graduation_year': 2013,
            'location': 'London',
            'twitter': 'FraserAtkins',
            'linkedin': 'fraseratkins',
            'url': 'http://www.fraseratkins.com/',
            'user': user,
            'get_absolute_url': '/FraserAtkins',
            'degree_subject': 'CS'
        },
        'joeroot': {
            'university': 'Imperial & Oxford',
            'graduation_year': 2012,
            'location': 'London',
            'twitter': 'joeroot',
            'linkedin': 'josephsroot',
            'url': 'http://joeroot.com/',
            'user': user,
            'get_absolute_url': '/joeroot',
            'degree_subject': 'CS'
        }
    }
    person = people[user.username]

    return render(request, 'profile.html', {'person': person})

def about(request):

    return render(request, 'about.html')