from django_seed import Seed
from .models import Project



entries = [
    {"title": "App 1", "category": "App", "image_description": "Description for App 1", "image": "images/portfolio-1.jpg"},
    {"title": "Web 3", "category": "Web", "image_description": "Description for Web3", "image": "images/portfolio-2.jpg"},
    {"title": "App 2", "category": "App", "image_description": "Description for App 2", "image": "images/portfolio-3.jpg"},
    {"title": "Card 2", "category": "Card", "image_description": "Description Card 2", "image": "images/portfolio-4.jpg"},
    {"title": "Web 2", "category": "Web", "image_description": "Description for Project 5", "image": "images/portfolio-5.jpg"},
    {"title": "App 3", "category": "App", "image_description": "Description App 3", "image": "images/portfolio-6.jpg"},
    {"title": "Card 1", "category": "Card", "image_description": "Description for Card 1", "image": "images/portfolio-7.jpg"},
    {"title": "Card 3", "category": "Card", "image_description": "Description for Card 3", "image": "images/portfolio-8.jpg"},
    {"title": "Web 3", "category": "Web", "image_description": "Description for Web3", "image": "images/portfolio-9.jpg"}
]


def runProject():
    seeder = Seed.seeder()
    for i in entries:
        seeder.add_entity(Project, 1, {
            'title': i['title'],
            'category': i['category'],
            'image_description': i['image_description'],
            'image': i['image'],
        })
    pks = seeder.execute()
    print(pks)


