from django.shortcuts import render, redirect
from .models import Project, Skill
from .forms import ContactForm
from django.contrib import messages

def home(request):
    projects = Project.objects.all()
    skills = Skill.objects.all()
    form = ContactForm()
    return render(request, 'home.html', {'projects': projects, 'skills': skills, 'form': form})

def contact(request):
    if request.method == 'POST':
        form = ContactForm(request.POST)
        if form.is_valid():
            form.save()
            messages.success(request, "Your message has been sent successfully!")
            return redirect('home')
    return redirect('home')
