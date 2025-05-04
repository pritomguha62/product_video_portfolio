from django.db import models

# Create your models here.

class Site_setting(models.Model):
    
    # STATUS_CHOICES = [
    #     ('draft', 'Draft'),
    #     ('published', 'Published'),
    #     ('archived', 'Archived')
    # ]

    title = models.CharField(max_length=200, null=True, blank=True)
    name = models.CharField(max_length=200, null=True, blank=True)
    short_description = models.CharField(max_length=300, null=True, blank=True)
    tagline = models.TextField(null=True, blank=True)
    description = models.TextField(null=True, blank=True)
    email = models.CharField(max_length=300, null=True, blank=True)
    phone = models.CharField(max_length=300, null=True, blank=True)
    whatsapp = models.CharField(max_length=300, null=True, blank=True)
    facebook = models.TextField(null=True, blank=True)
    linkedin = models.TextField(null=True, blank=True)
    instagram = models.TextField(null=True, blank=True)
    youtube = models.TextField(null=True, blank=True)
    twitter = models.TextField(null=True, blank=True)
    github = models.TextField(null=True, blank=True)
    address = models.TextField(null=True, blank=True)
    # view_count = models.IntegerField(default=1)
    favicon = models.ImageField(null=True, blank=True, upload_to='site_setting_favicon/')
    logo = models.ImageField(null=True, blank=True, upload_to='site_setting_logo/')
    image = models.ImageField(null=True, blank=True, upload_to='site_setting_images/')
    video = models.FileField(null=True, blank=True, upload_to='site_setting_videos/')
    resume = models.FileField(null=True, blank=True, upload_to='site_setting_resumes/')
    # link = models.TextField(null=True, blank=True)
    # status = models.CharField(max_length=10, choices=STATUS_CHOICES, default='publish')
    # is_deleted = models.BooleanField(default=False)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

