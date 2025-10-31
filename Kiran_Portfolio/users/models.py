from django.db import models
from django.contrib.auth.models import AbstractUser
from django.core.exceptions import ValidationError
import datetime as dt
import re


def validate_password(raw_password):
    if len(raw_password) < 8:
        raise ValidationError("Password should be atleast 8 characters")
    elif not re.search(r'[a-z]', raw_password):
        raise ValidationError("Password should contains atleast one lowercase letter")
    elif not re.search(r'[A-Z]', raw_password):
        raise ValidationError("Password should contains atleast one uppercase letter")
    elif not re.search(r'[\d]', raw_password):
        raise ValidationError("Password should contains atleast one digit")
    elif not re.search(r'[@#$%&*?/]', raw_password):
        raise ValidationError("Password should contains atleast one special character")
    

class CustomUser(AbstractUser):
    email = models.EmailField(
        verbose_name='email',
        unique=True,
        help_text='Enter your valid email',
        error_messages={
            "unique": "A user with that email already exists.",
        },
    )
    role = models.CharField(
        max_length=15,
        help_text='Select one: Admin, Visitor, Recruiter, or Contributor',
        choices=[
            ('admin', 'Admin'),
            ('visitor', 'Visitor'),
            ('recruiter', 'Recruiter'),
            ('contributor', 'Contributor'),
        ],
    )
    email_verified = models.BooleanField(default=False)
    profile_completed = models.BooleanField(default=False)

    USERNAME_FIELD = 'email'
    REQUIRED_FIELDS = ['first_name', 'last_name']

    def clean(self):
        if self.password:
            validate_password(self.password)
        return super().clean()

    def __str__(self):
        return f"{self.username} - role -  ({self.role})"
    
def validate_age(date_of_birth):
    today = dt.date.today()
    age = today.year - date_of_birth.year - (
        (today.month, today.day) < (date_of_birth.month, date_of_birth.day)
    )
    if age < 13:
        raise ValidationError("User must be at least 13 years old.")

class Profile(models.Model):
    user = models.OneToOneField(
        CustomUser,
        on_delete=models.CASCADE,
        related_name='profile'
    )
    headline = models.CharField(max_length=100, help_text="Short tagline (e.g. “Data Scientist | GenAI Developer”)")
    bio = models.TextField(help_text='Short professional summary')
    profile_picture = models.ImageField(
        upload_to='profile_photos/',
        null=True,
        blank=True
    )
    location = models.CharField(
        max_length=100,
        help_text="City, Country"
    )
    date_of_birth = models.DateField(null=True, blank=True, validators=[validate_age])
    phone_number = models.CharField(max_length=15, blank=True, null=True)
    

    def __str__(self):
        return f"Profile of {self.user.username}"


class ProfessionalInfo(models.Model):
    user = models.OneToOneField(
        CustomUser,
        on_delete=models.CASCADE,
        related_name='professional_info'
    )
    designation = models.CharField(max_length=100, help_text="Current title (e.g. Data Scientist)")
    company = models.CharField(max_length=150, blank=True, help_text="Current company name")
    skills = models.JSONField(default=dict, help_text="List of skills (e.g. 'languages': ['Python', 'c'], 'frameworks':['django', 'langchain'])")
    years_of_experience = models.PositiveIntegerField(default=0)
    education = models.JSONField(default=list, help_text="List of dicts: [{'degree': 'B.Tech', 'university': 'IIT', 'year': 2020}]")
    certifications = models.JSONField(default=list, blank=True, null= True, help_text="List of certifications with issuer/date")
    achievements = models.TextField(blank=True, null=True)
    projects_count = models.PositiveIntegerField(default=0)
    resume = models.FileField(
        upload_to='resumes/',
        null=True,
        blank=True,
        help_text='Upload resume (PDF)'
    )

    def __str__(self):
        return f"Professional Info of {self.user.username}"


class SocialLinks(models.Model):
    user = models.OneToOneField(
        CustomUser,
        on_delete=models.CASCADE,
        related_name='social_links'
    )
    github_url = models.URLField(blank=True, null=True)
    linkedin_url = models.URLField(blank=True, null=True)
    kaggle_url = models.URLField(blank=True, null=True)
    portfolio_website = models.URLField(blank=True, null=True)
    medium_url = models.URLField(blank=True, null=True)
    twitter_url = models.URLField(blank=True, null=True)
    youtube_url = models.URLField(blank=True, null=True)

    def __str__(self):
        return f"Social Links of {self.user.username}"
