from django.shortcuts import render, redirect
from django.core.mail import send_mail
from django.conf import settings
from .models import Project, ContactMessage
from .forms import ContactForm
from .models import About, Skill

def home(request):
    projects = Project.objects.all().order_by('-id')[:6]
    skills = Skill.objects.all()
    return render(request, 'home.html', {'projects': projects, 'skills': skills})

def about(request):
    about_info = About.objects.first()
    skills = Skill.objects.all()
    return render(request, 'about.html', {'about': about_info, 'skills': skills})

def projects(request):
    projects = Project.objects.all().order_by('-id')
    tech = request.GET.get('tech')
    if tech:
        projects = projects.filter(tech_stack__icontains=tech)
    return render(request, 'projects.html', {'projects': projects})

def contact(request):
    if request.method == "POST":
        form = ContactForm(request.POST)
        if form.is_valid():
            name = form.cleaned_data['name']
            email = form.cleaned_data['email']
            message = form.cleaned_data['message']

            ContactMessage.objects.create(name=name, email=email, message=message)

            # send email
            subject = f"Portfolio Contact from {name}"
            full_message = f"Message from {name} ({email}):\n\n{message}"
            try:
                send_mail(subject, full_message, settings.DEFAULT_FROM_EMAIL, [settings.DEFAULT_FROM_EMAIL])
            except Exception:
                # Fail quietly in dev; consider logging
                pass

            return redirect('contact')
    else:
        form = ContactForm()
    return render(request, 'contact.html', {'form': form})
