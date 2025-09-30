from django.shortcuts import render, redirect
from django.contrib import messages
from django.core.mail import send_mail
from .models import Project, Skill, About, BlogPost, Contact  # Updated to include Contact
from .forms import ContactForm  # If you have a separate forms.py, ensure it’s updated too
from django import forms
from captcha.fields import CaptchaField

def home(request):
    projects = Project.objects.all()[:5]
    skills = Skill.objects.all()
    return render(request, 'home.html', {'projects': projects, 'skills': skills})

def projects_view(request):
    filter_param = request.GET.get('filter', 'all')
    projects = Project.objects.all()
    if filter_param != 'all':
        projects = projects.filter(title__icontains=filter_param)  # Basic filtering; enhance with category field
    return render(request, 'projects.html', {'projects': projects})

def about_view(request):
    about = About.objects.first()
    skills = Skill.objects.all()
    return render(request, 'about.html', {'about': about, 'skills': skills})

def contact_view(request):
    if request.method == 'POST':
        form = ContactForm(request.POST)
        if form.is_valid():
            form.save()
            messages.success(request, 'Your message has been sent successfully!')
            return redirect('contact')
        else:
            messages.error(request, 'There was an error with your submission.')
    else:
        form = ContactForm()
    return render(request, 'contact.html', {'form': form})

def blog_view(request):
    posts = BlogPost.objects.all().order_by('-created_at')
    return render(request, 'blog.html', {'posts': posts})

class ContactForm(forms.ModelForm):
    class Meta:
        model = Contact  # Changed from ContactMessage to Contact
        fields = ['name', 'email', 'message']
        widgets = {
            'name': forms.TextInput(attrs={'placeholder': 'Enter your full name'}),
            'email': forms.EmailInput(attrs={'placeholder': 'Enter your email address'}),
            'message': forms.Textarea(attrs={'placeholder': 'Type your message here'}),
        }

    captcha = CaptchaField()