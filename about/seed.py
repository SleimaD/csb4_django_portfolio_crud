
from django_seed import Seed
from .models import About



entries = [
    { 
        'title':'UI/UX Designer & Web Developer.',
        'subtitle':'Lorem ipsum dolor sit amet, consectetur adipiscing elit, sed do eiusmod tempor incididunt ut labore et dolore magna aliqua.',
        'profile_image': 'images/profile_img.jpg',
        'general_description':'Magnam dolores commodi suscipit. Necessitatibus eius consequatur ex aliquid fuga eum quidem. Sit sint consectetur velit. Quisquam quos quisquam cupiditate. Et nemo qui impedit suscipit alias ea. Quia fugiat sit in iste officiis commodi quidem hic quas.',
        'birthday': '1995-05-01',
        'website': 'www.example.com',
        'phone': '+123 456 7890',
        'city': 'New York, USA',
        'age': 30,
        'degree': 'Master',
        'email': 'email@example.com',
        'freelance': 'Available',
        'detailed_description': 'Officiis eligendi itaque labore et dolorum mollitia officiis optio vero. Quisquam sunt adipisci omnis et ut. Nulla accusantium dolor incidunt officia tempore. Et eius omnis. Cupiditate ut dicta maxime officiis quidem quia. Sed et consectetur qui quia repellendus itaque neque. Aliquid amet quidem ut quaerat cupiditate. Ab et eum qui repellendus omnis culpa magni laudantium dolores.'
    }
]

def runAbout():
    seeder = Seed.seeder()
    for i in entries:
        seeder.add_entity(About, 1, {
            'title': i['title'],
            'subtitle': i['subtitle'],
            'profile_image': i['profile_image'],
            'general_description': i['general_description'],
            'birthday': i['birthday'],
            'website': i['website'],
            'phone': i['phone'],
            'city': i['city'],
            'age': i['age'],
            'degree': i['degree'],
            'email': i['email'],
            'freelance': i['freelance'],
            'detailed_description': i['detailed_description'],
        })
    pks = seeder.execute()
    print(pks)