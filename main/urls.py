from django.urls import path
from . import views

urlpatterns = [
    path('', views.home, name='home'),
    path('about/', views.about_view, name='about'),
    path('projects/', views.projects_view, name='projects'),
    path('contact/', views.contact_view, name='contact'),
    path('blog/', views.blog_view, name='blog'),
    path('blog/<int:pk>/', views.blog_detail, name='blog_detail'),
    path('reset-admin/', views.reset_admin_password, name='reset_admin'),
]