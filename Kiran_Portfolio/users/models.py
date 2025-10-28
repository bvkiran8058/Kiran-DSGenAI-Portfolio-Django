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

class Profile(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE, related_name='profile')
    user = models.OneToOneField(
        User,
        on_delete=models.CASCADE,
        related_name='profile'
    )
    headline = models.CharField(
        max_length=100,
        help_text="Short tagline (e.g. “Data Scientist  | GenAI Developer”)"
    )
    bio = models.TextField(
        help_text='Short professional summary '
    )
    profile_picture =models.ImageField(
        upload_to='profile photos/'
    )