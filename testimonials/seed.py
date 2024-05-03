from django_seed import Seed
from .models import Testimonial


entries = [
    {
        "text": "Proin iaculis purus consequat sem cure digni ssim donec porttitora entum suscipit rhoncus. Accusantium quam, ultricies eget id, aliquam eget nibh et. Maecen aliquam, risus at semper.",
        "first_name": "Saul",
        "last_name": "Goodman",
        "position": "Ceo & Founder",
        "image": "images/testimonials-1.jpg"
    },
    {
        "text": "Export tempor illum tamen malis malis eram quae irure esse labore quem cillum quid cillum eram malis quorum velit fore eram velit sunt aliqua noster fugiat irure amet legam anim culpa.",
        "first_name": "Sara",
        "last_name": "Wilsson",
        "position": "Designer",
        "image": "images/testimonials-2.jpg"
    },
    {
        "text": "Enim nisi quem export duis labore cillum quae magna enim sint quorum nulla quem veniam duis minim tempor labore quem eram duis noster aute amet eram fore quis sint minim.",
        "first_name": "Jena",
        "last_name": "Karlis",
        "position": "Store Owner",
        "image": "images/testimonials-3.jpg"
    },
    {
        "text": "Fugiat enim eram quae cillum dolore dolor amet nulla culpa multos export minim fugiat minim velit minim dolor enim duis veniam ipsum anim magna sunt elit fore quem dolore labore illum veniam.",
        "first_name": "Matt",
        "last_name": "Brandon",
        "position": "Freelancer",
        "image": "images/testimonials-4.jpg"
    },
    {
        "text": "Quis quorum aliqua sint quem legam fore sunt eram irure aliqua veniam tempor noster veniam enim culpa labore duis sunt culpa nulla illum cillum fugiat legam esse veniam culpa fore nisi cillum quid.",
        "first_name": "John",
        "last_name": "Larson",
        "position": "Entrepreneur",
        "image": "images/testimonials-5.jpg"
    }
]


def runTestimonials():
    seeder = Seed.seeder()
    for i in entries:
        seeder.add_entity(Testimonial, 1, {
            'text': i['text'],
            'first_name': i['first_name'],
            'last_name': i['last_name'],
            'position': i['position'],
            'image': i['image'],
        })
    pks = seeder.execute()
    print(pks)
