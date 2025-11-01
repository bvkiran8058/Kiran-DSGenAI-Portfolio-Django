from django.db import models

class Certificate(models.Model):
    user = models.ForeignKey(
        'users.CustomUser',
        on_delete=models.CASCADE,
        related_name='certificates'  
    )
    name = models.CharField(max_length=200)
    issuer = models.CharField(max_length=100)
    issue_date = models.DateField()
    credential_id = models.CharField(max_length=100, null=True, blank=True)
    credential_url = models.URLField()
    image = models.ImageField(upload_to='certificates/', null=True, blank=True)
    description = models.TextField(null=True, blank=True)

    def __str__(self):
        return f"{self.name} - {self.issuer} ({self.issue_date.year})"

    class Meta:
        ordering = ['-issue_date']