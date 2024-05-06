from django.shortcuts import render, redirect, get_object_or_404
from about.models import About
from skills.models import Skill
from portfolio.models import Project
from services.models import Service
from testimonials.models import Testimonial
from contact.models import ContactInfo
from contact.models import ContactMessage

from about.forms import AboutForm
from skills.forms import SkillForm
from portfolio.forms import ProjectForm
from services.forms import ServiceForm
from testimonials.forms import TestimonialForm
from contact.forms import ContactInfoForm
from contact.forms import ContactForm




# Renders the home page with fetched data from various models.
# Creates a unique category filter list for projects.
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



# Renders the backoffice page with fetched data from various models.
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




# Renders the services page with fetched data from the Service model.
def services(request):
    services = Service.objects.all()
    context = locals()
    return render(request, "les-services.html",context)




#* edit about
def edit_about(request): 
    about = get_object_or_404(About, id=1)
    if request.method == 'POST':
        form = AboutForm(request.POST or None, request.FILES, instance=about)
        if form.is_valid():
            form.save()
            return redirect('backoffice') 
    else:
        form = AboutForm(instance=about)
    return render(request, 'aboutback.html', {'form': form, 'about': about})


#* edit skills

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


# * delete skills
def delete_skill(request, id):
    skill = Skill.objects.get(id=id)
    skill.delete()
    return redirect('backoffice')



#* portfolio details
def portfolio_details(request):
    return render(request, "portfolio-details.html")


#* add a project to portfolio 
def add_project(request):
    if request.method == 'POST':
        form = ProjectForm(request.POST, request.FILES)
        if form.is_valid():
            form.save()
            return redirect('backoffice') 
    else:
        form = ProjectForm()
    return render(request, 'portfolioback.html', {'form': form})

#* delete a projet from portfolio 
def delete_project(request, id):
    project = Project.objects.get(id=id)
    project.delete()
    return redirect('backoffice')



#* add services
def add_service(request):
    if request.method == 'POST':
        form = ServiceForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('backoffice')  
    else:
        form = ServiceForm()
    return render(request, 'serviceback.html', {'form': form})


#* delete a service
def delete_service(request, id):
    service = Service.objects.get(id=id)
    service.delete()
    return redirect('backoffice')





#* add testimonials
def add_testimonial(request):
    if request.method == 'POST':
        form = TestimonialForm(request.POST, request.FILES)
        if form.is_valid():
            form.save()
            return redirect('backoffice')  
    else:
        form = TestimonialForm()
    return render(request, 'testimonialback.html', {'form': form})


#* delete testimonial
def delete_testimonial(request, id):
    testimonial = Testimonial.objects.get(id=id)
    testimonial.delete()
    return redirect('backoffice')



#* edit contact
def edit_contact(request):
    contact_info = get_object_or_404(ContactInfo, id=1)
    if request.method == 'POST':
        form = ContactInfoForm(request.POST, instance=contact_info)
        if form.is_valid():
            form.save()
            return redirect('backoffice') 
    else:
        form = ContactInfoForm(instance=contact_info)
    return render(request, 'contactback.html', {'form': form})


#* form to add to Mailbox
def contact(request):
    if request.method == 'POST':
        form = ContactForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('contact')  
    else:
        form = ContactForm()
    return render(request, 'index.html', {'form': form}) 


#* render mailbox page and fetch all data
def mailbox(request):
    messages = ContactMessage.objects.all()
    return render(request, 'mailbox.html', {'messages': messages})


#* delete a mail
def delete_mailbox(request, id):
    mailbox = ContactMessage.objects.get(id=id)
    mailbox.delete()
    return redirect('mailbox')

