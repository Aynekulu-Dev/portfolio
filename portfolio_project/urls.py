from django.contrib import admin
from django.urls import path, include
from main import views

urlpatterns = [
    path('', views.home, name='home'),
    path('about/', views.about_view, name='about'),
    path('projects/', views.projects_view, name='projects'),
    path('contact/', views.contact_view, name='contact'),
    path('blog/', views.blog_view, name='blog'),
    path('admin/', admin.site.urls),  # Single inclusion of admin URLs
    path('captcha/', include('captcha.urls')),
]