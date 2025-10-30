from django.db import models
from django.contrib.auth.models import AbstractUser
from django.core.validators import RegexValidator, MinLengthValidator
import string
# Create your models here.

class CustomUser(AbstractUser):
    
    phone_number_validator = RegexValidator(
        regex=r'^[6-9]\d{9}$',
        message='Enter a valid 10-digit Indian phone number starting with 6-9.'
    )
    password_validator = RegexValidator(
        regex=r'^(?=.*[a-z])(?=.*[A-Z])(?=.*\d)(?=.*[@$!%*?&])[A-Za-z\d@$!%*?&]{8,}$',
        message='Password must contain at least 8 characters, including uppercase, lowercase, number, and special character.'
    )
    email = models.EmailField(unique=True, help_text='enter your email')
    phone_number = models.CharField(max_length=10, validators= phone_number_validator, blank=True, null=True)
    password = models.CharField(max_length=128, validators=[password_validator])
    date_of_birth = models.DateField(blank=True, null=True)
    LANGUAGE_CHOICES = [
        ('TE', 'Telugu'),
        ('HI', 'Hindi'),
        ('EN', 'English')
        ('TA', 'Tamil'),
    ]
    preferred_language = models.CharField(
        max_length=2,
        choices=LANGUAGE_CHOICES,
        default='EN'
    )
    is_email_verified = models.BooleanField(default=False)
    is_email_verification_token = models.CharField(max_length=100, blank=True, null=True)

    USERNAME_FIELD = "email"
    REQUIRED_FIELDS = ['username', 'first_name', 'last_name']

    def __str__(self):
        return self.first_name +" "+ self.last_name
    
    class Meta:
        db_table = 'Custom Users'
        verbose_name = 'User'
        verbose_name_plural = 'Users'
        indexes = [
            models.Index(fields=['email']),
            models.Index(fields=['date_joined']),
            models.Index(fields=['is_active', 'is_email_verified'])
        ]
class BaseProfile(models.Model):
    user = models.OneToOneField(CustomUser, on_delete=models.CASCADE)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

class LibrarianProfile(BaseProfile):
    employee_id = models.BigIntegerField(primary_key=True)
    DEPARTMENT_CHOICES = [
        ('CIRC', 'Circulation'),
        ('REF', 'Reference Services'),
        ('TECH', 'Technical Services'),
        ('CAT', 'Cataloging'),
        ('ACQ', 'Acquisitions'),
        ('CHILD', 'Children’s Services'),
        ('YA', 'Young Adult Services'),
        ('DIGI', 'Digital Resources'),
        ('ADMIN', 'Administration'),
        ('ARCH', 'Archives and Special Collections'),
        ('OUTR', 'Outreach and Community Engagement'),
        ('IT', 'IT and Systems Support'),
    ]
    department = models.CharField(max_length=20, choices=DEPARTMENT_CHOICES)
    hire_date = models.DateField(auto_now_add=True)
    ACCESS_LEVELS = [
        ('BASIC', 'Basic Access'),
        ('STAFF', 'Staff Access'),
        ('SUPERVISOR', 'Supervisor Access'),
        ('MANAGER', 'Manager Access'),
        ('ADMIN', 'Administrator Access'),
        ('TECH', 'Technical Access'),
        ('ARCHIVE', 'Archive Access'),
    ]
    access_levels = models.CharField(max_length=20, choices=ACCESS_LEVELS)
    supervisor = models.ForeignKey(
        'self',
        on_delete=models.SET_NULL,
        null=True,
        blank=True,
        related_name='subordinates'
    )

class MemberProfile(BaseProfile):
    membership_number=
    MEMBERSHIP_TYPES=[
        ()
    ]
    membership_types =
    registration_date =
    membership_expiry = 

    # address information

    # emergency contact

    # preferences