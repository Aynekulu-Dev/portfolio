from django.shortcuts import render
from .models import Project

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

            subject = f"Portfolio Contact from {name}"
            full_message = f"Message from {name} ({email}):\n\n{message}"

            send_mail(
                subject,
                full_message,
                settings.DEFAULT_FROM_EMAIL,  # sender
                [settings.DEFAULT_FROM_EMAIL],  # recipient (your email)
            )
            return redirect('contact')  # reload page after submit
    else:
        form = ContactForm()

    return render(request, 'contact.html', {'form': form})