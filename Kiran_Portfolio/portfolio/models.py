from django.db import models

# Create your models here.

class Technology(models.Model):
    name = models.CharField(max_length=128, help_text="eg. python, sql, django")
    category = models.CharField(max_length=128, help_text="eg.programming language, web framework")
    description = models.TextField(blank=True, null= True)

class Project(models.Model):
    user = models.ForeignKey(
        'users.CustomUser',
        on_delete=models.CASCADE,
        related_name= 'projects'
    )
    title = models.CharField(max_length=128, help_text="Enter project title")
    description = models.TextField()
    tech_stack = models.ManyToManyField(Technology)
    github_link = models.URLField()
    image = models.ImageField(upload_to='project_images/', null=True, blank=True)
    created_at = models.DateTimeField(auto_now_add=True)
    featured = models.BooleanField(default=False)
