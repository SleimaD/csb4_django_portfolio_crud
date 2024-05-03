from django.shortcuts import render, redirect
from about.models import About
from skills.models import Skill
from portfolio.models import Project
from services.models import Service
from testimonials.models import Testimonial
from contact.models import ContactInfo

def home(request):
    about = About.objects.first()
    skills = Skill.objects.all()
    projects = Project.objects.all()
    services = Service.objects.all()
    testimonials = Testimonial.objects.all()
    contact = ContactInfo.objects.first()
    seen = set()
    uniquefilterlist = []
    for obj in projects:
        if obj.category not in seen:
            seen.add(obj.category)
            uniquefilterlist.append(obj.category)
    context = locals()
    return render(request, "index.html",context)


def backoffice(request):
    about = About.objects.first()
    skills = Skill.objects.all()
    projects = Project.objects.all()
    services = Service.objects.all()
    testimonials = Testimonial.objects.all()
    contact = ContactInfo.objects.first()
    seen = set()
    uniquefilterlist = []
    for obj in projects:
        if obj.category not in seen:
            seen.add(obj.category)
            uniquefilterlist.append(obj.category)
    context = locals()
    return render(request, "backoffice.html", context)


    

