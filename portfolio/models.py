from django.db import models
from service.models import Service

# Create your models here.

class Portfolio(models.Model):
    STATUS_CHOICES = [
        ('draft', 'Draft'),
        ('published', 'Published'),
        ('archived', 'Archived')
    ]

    title = models.CharField(max_length=200, null=True, blank=True)
    short_description = models.CharField(max_length=300, null=True, blank=True)
    description = models.TextField(null=True, blank=True)
    slug = models.SlugField(unique=True, null=True)
    view_count = models.IntegerField(default=1)
    image = models.ImageField(null=True, blank=True, upload_to='portfolio_images/')
    video = models.FileField(null=True, blank=True, upload_to='videos/')
    link = models.TextField(null=True, blank=True)
    service = models.ForeignKey(Service, on_delete=models.CASCADE, related_name="portfolios", null=True, blank=True)
    is_short = models.CharField(max_length=10, choices=[('yes', 'Yes'), ('no', 'No')], default='yes')
    status = models.CharField(max_length=10, choices=STATUS_CHOICES, default='published')
    is_deleted = models.BooleanField(default=False)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

