from django.db import models
from django.contrib.auth.models import AbstractUser
import string

special_characters = list(string.punctuation)
string.
# Create your models here.

class User(AbstractUser):
    email = models.EmailField(
        verbose_name='email',
        unique=True,
        blank=False,
        help_text= 'enter your valid email',
        error_messages={
            "unique": ("A user with that email already exists."),
        },
    )
    password = models.CharField(
        'password',
        help_text='Enter your password which has min length of 8 and special char and number and caps and small letter'
    )
    role = models.CharField(
        max_length=15,
        help_text= 'select anyone of these (`Admin`, `Visitor`, `Recruiter`, `Contributor`)',
        choices=[
            ('admin', 'admin'),
            ('visitor', 'visitor'),
            ('recruiter', 'recruiter'),
            ('contributor', 'contributor')
        ]
    )
    email_verified = models.BooleanField(default=False)
    profile_completed = models.BooleanField(default=False)

    def save(self, *args, **kwargs):
        if self.password is not None:
            if all()
        super().save(*args, **kwargs)