from django.db import models

class About(models.Model):
    name = models.CharField(max_length=100, default='Aynekulu Molla Miniwab')
    degree = models.CharField(max_length=100, default='BSc in Software Engineering')
    bio = models.TextField(default='Software Engineering graduate from Adama Science and Technology University with a passion for full-stack development, data science, and AI.')
    profile_image = models.ImageField(upload_to='profiles/', blank=True, null=True)
    certificate_image = models.ImageField(upload_to='certificates/', blank=True, null=True)

    def __str__(self):
        return self.name

class Skill(models.Model):
    name = models.CharField(max_length=50)
    level = models.PositiveIntegerField(help_text="Percentage 0-100")

    def __str__(self):
        return self.name

class Project(models.Model):
    title = models.CharField(max_length=100)
    description = models.TextField()
    image = models.ImageField(upload_to='projects/', default='projects/placeholder.jpg')
    github_url = models.URLField(blank=True, null=True)
    demo_url = models.URLField(blank=True, null=True)

    def __str__(self):
        return self.title

class Contact(models.Model):
    name = models.CharField(max_length=100)
    email = models.EmailField()
    message = models.TextField()
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"{self.name} - {self.email}"

class BlogPost(models.Model):
    title = models.CharField(max_length=200)
    content = models.TextField()
    image = models.ImageField(upload_to='blog/', blank=True, null=True)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)  # Changed from auto_next to auto_now

    def __str__(self):
        return self.title