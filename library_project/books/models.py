from django.db import models

# Create your models here.

class Author(models.Model):
    name = models.CharField(max_length=250)
    biography = models.TextField(null=True)
    photo = models.ImageField(upload_to='author_photos/', null=True, blank=True, help_text='please upload image name as author name (eg. rabindranath_tagore.jpg)')
    author_alias = models.ManyToManyField('self', on_delete = models.SET_NULL, null=True, blank=True, related_name='alias')
    social_media_links = models.JSONField(default=dict, blank=True)
    birth_date = models.DateField(null=True, blank=True)
    death_date = models.DateField(null=True, blank=True)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    