from django.contrib import admin
from .models import Project, ContactMessage
from .models import About
from .models import Skill

@admin.register(Project)
class ProjectAdmin(admin.ModelAdmin):
    list_display = ("title", "tech_stack", "github_link", "live_demo")

@admin.register(ContactMessage)
class ContactMessageAdmin(admin.ModelAdmin):
    list_display = ('name', 'email', 'created_at')
    ordering = ('-created_at',)
@admin.register(About)
class AboutAdmin(admin.ModelAdmin):
    list_display = ('name', 'degree')
@admin.register(Skill)
class SkillAdmin(admin.ModelAdmin):
    list_display = ('name', 'level')
