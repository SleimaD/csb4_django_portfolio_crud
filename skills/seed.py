from django_seed import Seed
from .models import Skill


entries = [
    {"name": "HTML", "percentage": 100},
    {"name": "CSS", "percentage": 90},
    {"name": "JavaScript", "percentage": 75},
    {"name": "PHP", "percentage": 80},
    {"name": "WordPress/CMS", "percentage": 90},
    {"name": "Photoshop", "percentage": 55}
]


def runSkill():
    seeder = Seed.seeder()
    for i in entries:
        seeder.add_entity(Skill, 1, {
            'name': i['name'],
            'percentage': i['percentage'],
        })
    pks = seeder.execute()
    print(pks)