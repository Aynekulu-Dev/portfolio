from django.db import models

class Project(models.Model):
    title = models.CharField(max_length=200)
    description = models.TextField()
    tech_stack = models.CharField(max_length=200)
    github_link = models.URLField(blank=True, null=True)
    live_demo = models.URLField(blank=True, null=True)
    image = models.ImageField(upload_to="projects/", blank=True, null=True)

    def __str__(self):
        return self.title

class ContactMessage(models.Model):
    name = models.CharField(max_length=100)
    email = models.EmailField()
    message = models.TextField()
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"{self.name} - {self.email}"
class About(models.Model):
    name = models.CharField(max_length=100, default="Aynekulu Molla")
    bio = models.TextField()
    degree = models.CharField(max_length=200, default="Bachelor's Degree")
    profile_image = models.ImageField(upload_to='about/', blank=True, null=True)
    certificate_image = models.ImageField(upload_to='about/', blank=True, null=True)

    def __str__(self):
        return self.name
class Skill(models.Model):
    name = models.CharField(max_length=50)        # Skill name, e.g., Python
    level = models.IntegerField(default=50)       # Skill proficiency 0-100%

    def __str__(self):
        return self.name
