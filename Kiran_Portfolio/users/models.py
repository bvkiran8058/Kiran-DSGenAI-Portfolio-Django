from django.db import models
from django.contrib.auth.models import AbstractUser
import string

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
            if len(self.password) < 8:
                return "please provide password with atleat 8 chars"
            elif not any(string.ascii_uppercase in self.password):
                return "please give atleast one uppercase letter in password"
            elif not any(string.ascii_lowercase in self.password):
                return "please give atleast one lowercase letter in password"
            elif not any(string.digits in self.password):
                return "please give atleast one digit in password"
            elif not any(string.punctuation in self.password):
                return "please give atleast one special char in password"
        super().save(*args, **kwargs)