from django.db import models

# Create your models here.

class Experience(models.Model):
    user = models.ForeignKey(
        'users.CustomUser',
        on_delete=models.CASCADE,
        related_name= 'experience'
    )
    company = models.CharField(max_length=100)
    role = models.CharField(max_length=100)
    start_date = models.DateField()
    end_date = models.DateField(null=True, blank=True)
    location = models.CharField(max_length=200, null=True, blank=True)
    description = models.TextField(default='')

    def calculate_experience(self):
        if self.start_date and self.end_date:
            years = self.end_date.year - self.start_date.year
            months = self.end_date.month - self.start_date.month
            if months < 0:
                years -= 1
                months += 12
            return f"{years} years, {months} months"
        return f"Current from date {self.start_date}"

    def __str__(self):
        return f"{self.user.username} - {self.company} @ {self.role} - with exp of {self.calculate_experience()}"

class Education(models.Model):
    user = models.ForeignKey(
        'users.CustomUser',
        on_delete=models.CASCADE,
        related_name='education'
    )
    institution = models.CharField(max_length=200)
    degree = models.CharField(max_length=100)
    field_of_study = models.CharField(max_length=100)
    start_year = models.IntegerField()
    end_year = models.IntegerField(null=True, blank=True)
    grade = models.CharField(max_length=50, null=True, blank=True)

    def __str__(self):
        return f"{self.user.username} - {self.institution} @ {self.degree}"