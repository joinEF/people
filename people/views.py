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
        },
        {
            'name': 'Jordan Burgess',
            'email': 'jordanburgess@gmail.com',
            'university': 'Cambridge',
            'graduation_year': 2013,
            'location': 'London',
            'twitter': 'jordnb',
            'github': 'jordn',
            'linkedin': 'jordanburgess',
            'url': 'http://jordanburgess.com/'
        },
        {
            'name': 'Fraser Atkins',
            'email': 'jordanburgess@gmail.com',
            'university': 'Cambridge',
            'graduation_year': 2013,
            'location': 'London',
            'twitter': 'FraserAtkins',
            'linkedin': 'fraseratkins',
            'url': 'http://www.fraseratkins.com/'
        },
        {
            'name': 'Joe Root',
            'university': 'Imperial & Oxford',
            'graduation_year': 2012,
            'location': 'London',
            'twitter': 'joeroot',
            'linkedin': 'josephsroot',
            'url': 'http://joeroot.com/'
        }
    ]

    return render(request, 'index.html', {'people': people})