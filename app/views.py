from django.shortcuts import render, redirect, get_object_or_404
from about.models import About
from skills.models import Skill
from portfolio.models import Project
from services.models import Service
from testimonials.models import Testimonial
from contact.models import ContactInfo

from about.forms import AboutForm
from skills.forms import SkillForm
from portfolio.forms import ProjectForm
from services.forms import ServiceForm
from testimonials.forms import TestimonialForm


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
        category = obj.category.strip().lower()
        if category not in uniquefilterlist:
            uniquefilterlist.append(category)
    context = locals()
    return render(request, "backoffice.html", context)



def edit_about(request): 
    # about = About.objects.first()
    about = get_object_or_404(About, id=1)
    if request.method == 'POST':
        form = AboutForm(request.POST or None, request.FILES, instance=about)
        if form.is_valid():
            form.save()
            return redirect('backoffice') 
    else:
        form = AboutForm(instance=about)
    return render(request, 'aboutback.html', {'form': form, 'about': about})


#* skills

def skill_add(request):
    if request.method == 'POST':
        form = SkillForm(request.POST, request.FILES)
        if form.is_valid():
            form.save()
            return redirect('backoffice')
    else:
        form = SkillForm()
    skills = Skill.objects.all()
    return render(request, 'skillsback.html', {'form': form, 'skills':skills})



def delete_skill(request, id):
    skill = Skill.objects.get(id=id)
    skill.delete()
    return redirect('backoffice')



#* portfolio

def portfolio_details(request):
    return render(request, "portfolio-details.html")


def add_project(request):
    if request.method == 'POST':
        form = ProjectForm(request.POST, request.FILES)
        if form.is_valid():
            form.save()
            return redirect('backoffice') 
    else:
        form = ProjectForm()
    return render(request, 'portfolioback.html', {'form': form})


def delete_project(request, id):
    project = Project.objects.get(id=id)
    project.delete()
    return redirect('backoffice')



#* services

def add_service(request):
    if request.method == 'POST':
        form = ServiceForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('backoffice')  
    else:
        form = ServiceForm()
    return render(request, 'serviceback.html', {'form': form})



def delete_service(request, id):
    service = Service.objects.get(id=id)
    service.delete()
    return redirect('backoffice')

#* testimonials

def add_testimonial(request):
    if request.method == 'POST':
        form = TestimonialForm(request.POST, request.FILES)
        if form.is_valid():
            form.save()
            return redirect('backoffice')  
    else:
        form = TestimonialForm()
    return render(request, 'testimonialback.html', {'form': form})


def delete_testimonial(request, id):
    testimonial = Testimonial.objects.get(id=id)
    testimonial.delete()
    return redirect('backoffice')


