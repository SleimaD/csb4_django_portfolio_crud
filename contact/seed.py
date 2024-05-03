from django_seed import Seed
from .models import ContactInfo


entries = [
    {
        'description': 'Magnam dolores commodi suscipit. Necessitatibus eius consequatur ex aliquid fuga eum quidem. Sit sint consectetur velit. Quisquam quos quisquam cupiditate. Et nemo qui impedit suscipit alias ea. Quia fugiat sit in iste officiis commodi quidem hic quas.',
        'street': 'Adam Street',
        'street_number': 'A108 ', 
        'location': 'New York, NY',
        'zipcode': '535022',
        'email': 'info@example.com',
        'phone': '+1 5589 55488 55'
    }
]

 
def runContact():
    seeder = Seed.seeder()
    for i in entries:
        seeder.add_entity(ContactInfo, 1, {
            'description': i['description'],
            'street': i['street'],
            'street_number': i['street_number'],
            'location': i['location'],
            'zipcode': i['zipcode'],
            'email': i['email'],
            'phone': i['phone'],
        })
    pks = seeder.execute()
    print(pks) 