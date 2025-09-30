from django.shortcuts import render, redirect
from django.contrib import messages
from .models import Project, Skill
from .forms import ContactForm

def home(request):
    projects = Project.objects.all()[:5]  # Featured projects
    skills = Skill.objects.all()
    return render(request, 'home.html', {'projects': projects, 'skills': skills})

def projects_view(request):
    projects = Project.objects.all()
    return render(request, 'projects.html', {'projects': projects})

def about_view(request):
    return render(request, 'about.html')

def contact_view(request):
    if request.method == "POST":
        form = ContactForm(request.POST)
        if form.is_valid():
            form.save()
            messages.success(request, "Your message has been sent successfully!")
            return redirect('contact')
    else:
        form = ContactForm()
    return render(request, 'contact.html', {'form': form})
