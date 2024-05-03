import os
import django
django.setup()
from about.seed import runAbout
from skills.seed import runSkill
from portfolio.seed import runProject
from services.seed import runService
from testimonials.seed import runTestimonials
from contact.seed import runContact

if __name__ == "__main__":
   # runAbout()
   # runSkill()
   # runProject()
   # runService()
   # runTestimonials()
   runContact()
   

    


