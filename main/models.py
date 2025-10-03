from django.db import models
from django.core.validators import MinValueValidator, MaxValueValidator, FileExtensionValidator

class About(models.Model):
    name = models.CharField(max_length=100, default='Aynekulu Molla Miniwab')
    degree = models.CharField(max_length=100, default='BSc in Software Engineering')
    bio = models.TextField(default='Software Engineering graduate from Adama Science and Technology University with a passion for full-stack development, data science, and AI.')
    profile_image = models.ImageField(upload_to='profiles/', blank=True, null=True, validators=[FileExtensionValidator(['jpg', 'png', 'jpeg'])])
    certificate_image = models.ImageField(upload_to='certificates/', blank=True, null=True, validators=[FileExtensionValidator(['jpg', 'png', 'jpeg'])])

    def __str__(self):
        return self.name

class Skill(models.Model):
    name = models.CharField(max_length=50)
    level = models.PositiveIntegerField(validators=[MinValueValidator(0), MaxValueValidator(100)])

    def __str__(self):
        return self.name

class Project(models.Model):
    CATEGORY_CHOICES = [
        ('web', 'Web Development'),
        ('data', 'Data Science'),
        ('ml', 'Machine Learning'),
        ('all', 'All'),
    ]
    title = models.CharField(max_length=100)
    description = models.TextField()
    image = models.ImageField(upload_to='projects/', default='projects/placeholder.jpg', validators=[FileExtensionValidator(['jpg', 'png', 'jpeg'])])
    github_url = models.URLField(blank=True, null=True)
    demo_url = models.URLField(blank=True, null=True)
    category = models.CharField(max_length=50, choices=CATEGORY_CHOICES, default='all')

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
    image = models.ImageField(upload_to='blog/', blank=True, null=True, validators=[FileExtensionValidator(['jpg', 'png', 'jpeg'])])
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.title
