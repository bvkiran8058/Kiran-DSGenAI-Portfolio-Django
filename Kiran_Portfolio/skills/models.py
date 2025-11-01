from django.db import models

# Create your models here.

class Skill(models.Model):
    user = models.ForeignKey(
        'users.CustomUser',
        on_delete=models.CASCADE,
        related_name= 'skills'
    )
    name = models.CharField(max_length=100)
    category = models.CharField(max_length=100, help_text='e.g. ML, Web, Cloud')
    proficiency = models.IntegerField(help_text='0 - 100%')
    description = models.TextField(default='')