from django.shortcuts import render, redirect
from django.core.mail import send_mail
from django.conf import settings
from .models import Project, ContactMessage
from .forms import ContactForm

def home(request):
    return render(request, 'home.html')

def about(request):
    return render(request, 'about.html')

def projects(request):
    projects = Project.objects.all()
    return render(request, 'projects.html', {"projects": projects})

def contact(request):
    if request.method == "POST":
        form = ContactForm(request.POST)
        if form.is_valid():
            name = form.cleaned_data['name']
            email = form.cleaned_data['email']
            message = form.cleaned_data['message']

            ContactMessage.objects.create(name=name, email=email, message=message)

            subject = f"Portfolio Contact from {name}"
            full_message = f"Message from {name} ({email}):\n\n{message}"
            send_mail(subject, full_message, settings.DEFAULT_FROM_EMAIL, [settings.DEFAULT_FROM_EMAIL])

            return redirect('contact')
    else:
        form = ContactForm()
    return render(request, 'contact.html', {'form': form})
