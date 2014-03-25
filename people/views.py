from django.shortcuts import render

def index(request):

    people = [
        {
            'name': 'Calum J. Eadie',
            'email': 'calum@calumjeadie.com',
            'university': 'Cambridge',
            'graduation_year': 2013,
            'location': 'London',
            'twitter': 'CalumJEadie',
            'github': 'CalumJEadie',
            'linkedin': 'calumjeadie',
            'url': 'http://calumjeadie.com'
        }
    ]

    print people

    return render(request, 'index.html', {'people': people})