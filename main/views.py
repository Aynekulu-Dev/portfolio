from django.shortcuts import render, redirect
from django.contrib import messages
from django.core.mail import send_mail
from django.conf import settings
from .models import Project, Skill, About, BlogPost, Contact
from .forms import ContactForm

def home(request):
    projects = Project.objects.all()[:5]
    skills = Skill.objects.all()
    return render(request, 'home.html', {'projects': projects, 'skills': skills})

def projects_view(request):
    filter_param = request.GET.get('filter', 'all')
    projects = Project.objects.all()
    if filter_param != 'all':
        projects = projects.filter(category=filter_param)
    return render(request, 'projects.html', {'projects': projects})

def about_view(request):
    about = About.objects.first()
    skills = Skill.objects.all()
    if not about:
        messages.warning(request, 'No About information found. Please add details in the admin panel.')
    return render(request, 'about.html', {'about': about, 'skills': skills})

def contact_view(request):
    if request.method == 'POST':
        form = ContactForm(request.POST)
        if form.is_valid():
            contact = form.save()
            send_mail(
                subject=f"New Contact Message from {contact.name}",
                message=f"Message: {contact.message}\nFrom: {contact.email}",
                from_email=contact.email,
                recipient_list=[settings.DEFAULT_FROM_EMAIL],
                fail_silently=False,
            )
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

def blog_detail(request, pk):
    post = BlogPost.objects.get(pk=pk)
    return render(request, 'blog_detail.html', {'post': post})
