from django.db import models
from django.contrib.auth.models import AbstractUser
from django.core.exceptions import ValidationError
import string

class User(AbstractUser):
    email = models.EmailField(
        verbose_name='email',
        unique=True,
        blank=False,
        help_text='Enter your valid email',
        error_messages={
            "unique": "A user with that email already exists.",
        },
    )
    password = models.CharField(
        'password',
        help_text='Enter your password (min 8 chars, 1 uppercase, 1 lowercase, 1 digit, 1 special char)'
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

    def save(self, *args, **kwargs):
        if self.password:
            if len(self.password) < 8:
                raise ValidationError("Password must be at least 8 characters long.")
            elif not any(c.isupper() for c in self.password):
                raise ValidationError("Password must contain at least one uppercase letter.")
            elif not any(c.islower() for c in self.password):
                raise ValidationError("Password must contain at least one lowercase letter.")
            elif not any(c.isdigit() for c in self.password):
                raise ValidationError("Password must contain at least one digit.")
            elif not any(c in string.punctuation for c in self.password):
                raise ValidationError("Password must contain at least one special character.")

            # Hash password before saving
            self.set_password(self.password)

        super().save(*args, **kwargs)

    def __str__(self):
        return f"{self.username} - role -  ({self.role})"

class Profile(models.Model):
    user = models.OneToOneField(
        User,
        on_delete=models.CASCADE,
        related_name='profile'
    )
    headline = models.CharField(
        max_length=100,
        help_text="Short tagline (e.g. “Data Scientist | GenAI Developer”)"
    )
    bio = models.TextField(
        help_text='Short professional summary'
    )
    profile_picture = models.ImageField(
        upload_to='profile_photos/',
        null=True,
        blank=True
    )
    location = models.CharField(
        max_length=100,
        help_text="City, Country"
    )
    date_of_birth = models.DateField(null=True, blank=True)
    phone_number = models.CharField(max_length=15, blank=True, null=True)

    def __str__(self):
        return f"Profile of {self.user.username}"


class ProfessionalInfo(models.Model):
    user = models.OneToOneField(
        User,
        on_delete=models.CASCADE,
        related_name='professional_info'
    )
    designation = models.CharField(
        max_length=100,
        help_text="Current title (e.g. Data Scientist)"
    )
    company = models.CharField(
        max_length=150,
        blank=True,
        help_text="Current company name"
    )
    skills = models.JSONField(
        default=list,
        help_text="List of skills (e.g. ['Python', 'Django', 'ML'])"
    )
    years_of_experience = models.PositiveIntegerField(default=0)
    education = models.JSONField(
        default=list,
        help_text="List of dicts: [{'degree': 'B.Tech', 'university': 'IIT', 'year': 2020}]"
    )
    certifications = models.JSONField(
        default=list,
        help_text="List of certifications with issuer/date"
    )
    achievements = models.TextField(blank=True)
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
        User,
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
