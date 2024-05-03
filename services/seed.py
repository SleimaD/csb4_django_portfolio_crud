from django_seed import Seed
from .models import Service


entries = [
    {"title": "Lorem Ipsum", "icon": "bi-briefcase", "description": "Voluptatum deleniti atque corrupti quos dolores et quas molestias excepturi sint occaecati cupiditate non provident"},

    {"title": "Dolor Sitema", "icon": "bi-card-checklist", "description": "Minim veniam, quis nostrud exercitation ullamco laboris nisi ut aliquip ex ea commodo consequat tarad limino ata"},

    {"title": "Sed ut perspiciatis", "icon": "bi-bar-chart", "description": "Duis aute irure dolor in reprehenderit in voluptate velit esse cillum dolore eu fugiat nulla pariatur"},

    {"title": "Magni Dolores", "icon": "bi-binoculars", 
    "description": "Excepteur sint occaecat cupidatat non proident, sunt in culpa qui officia deserunt mollit anim id est laborum"},

    {"title": "Nemo Enim", "icon": "bi-brightness-high", "description": "At vero eos et accusamus et iusto odio dignissimos ducimus qui blanditiis praesentium voluptatum deleniti atque"},

    {"title": "Eiusmod Tempor", "icon": "bi-calendar4-week", "description": "Et harum quidem rerum facilis est et expedita distinctio. Nam libero tempore, cum soluta nobis est eligendi"}
]


def runService():
    seeder = Seed.seeder()
    for i in entries:
        seeder.add_entity(Service, 1, {
            'title': i['title'],
            'icon': i['icon'],
            'description': i['description'],
        })
    pks = seeder.execute()
    print(pks)