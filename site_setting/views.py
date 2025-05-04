
from django.shortcuts import render, redirect, get_object_or_404
from .models import *
import os
from django.http import HttpResponseRedirect, HttpResponse
from django.contrib import messages
from datetime import datetime


# Create your views here.

def add_site_setting(request):
    
    site_setting = Site_setting.objects.last()
    
    if site_setting:
    
        return render(request, 'admin_templates/add_site_setting.html', {'site_setting':site_setting})
    else:
        
        return render(request, 'admin_templates/add_site_setting.html')


def add_site_setting_info(request):
    
    if request.method == "POST":
        
        site_setting_info = request.POST

        title = site_setting_info.get('title')
        name = site_setting_info.get('name')
        short_description = site_setting_info.get('short_description')
        tagline = site_setting_info.get('tagline')
        description = site_setting_info.get('description')
        email = site_setting_info.get('email')
        phone = site_setting_info.get('phone')
        whatsapp = site_setting_info.get('whatsapp')
        facebook = site_setting_info.get('facebook')
        linkedin = site_setting_info.get('linkedin')
        instagram = site_setting_info.get('instagram')
        youtube = site_setting_info.get('youtube')
        twitter = site_setting_info.get('twitter')
        github = site_setting_info.get('github')
        address = site_setting_info.get('address')

        last_site_setting = Site_setting.objects.last()
        
        if last_site_setting:
        
            site_setting, created = Site_setting.objects.update_or_create(
            
                id=last_site_setting.id,
                
                defaults={
                    'title': title,
                    'name': name,
                    'short_description': short_description,
                    'tagline': tagline,
                    'description': description,
                    'email': email,
                    'phone': phone,
                    'whatsapp': whatsapp,
                    'facebook': facebook,
                    'linkedin': linkedin,
                    'instagram': instagram,
                    'youtube': youtube,
                    'twitter': twitter,
                    'github': github,
                    'address': address
                }
                
            )
            
        else:
        
            site_setting = Site_setting.objects.create(
                
                title=title,
                name=name,
                short_description=short_description,
                tagline=tagline,
                description=description,
                email=email,
                phone=phone,
                whatsapp=whatsapp,
                facebook=facebook,
                linkedin=linkedin,
                instagram=instagram,
                youtube=youtube,
                twitter=twitter,
                github=github,
                address=address
                
            )

        
            
        # site_setting = Site_setting()
        
        # site_setting.title = title
        # site_setting.name = name
        # site_setting.short_description = short_description
        # site_setting.tagline = tagline
        # site_setting.description = description
        # site_setting.email = email
        # site_setting.phone = phone
        # site_setting.whatsapp = whatsapp
        # site_setting.facebook = facebook
        # site_setting.linkedin = linkedin
        # site_setting.instagram = instagram
        # site_setting.youtube = youtube
        # site_setting.twitter = twitter
        # site_setting.github = github
        # site_setting.address = address
        

        if request.FILES.get('favicon') is not None:
            uploaded_favicon = request.FILES['favicon']
            ext = uploaded_favicon.name.split('.')[-1]
            timestamp = datetime.now().strftime('%Y%m%d%H%M%S')
            new_name_favicon = f"{title}{timestamp}.{ext}"
            site_setting.favicon.save(new_name_favicon, uploaded_favicon)
            
        # else:

        #     last_site_setting = Site_setting.objects.last()
            
        #     if last_site_setting.favicon.url:
        #         site_setting.favicon.url = last_site_setting.favicon.url
                
        #     else:
        #         site_setting.favicon.url = None
        
        
        
        if request.FILES.get('logo') is not None:
            uploaded_logo = request.FILES['logo']
            ext = uploaded_logo.name.split('.')[-1]
            timestamp = datetime.now().strftime('%Y%m%d%H%M%S')
            new_name_logo = f"{title}{timestamp}.{ext}"
            site_setting.logo.save(new_name_logo, uploaded_logo)
            
        # else:

        #     last_site_setting = Site_setting.objects.last()
            
        #     if last_site_setting.logo.url:
        #         site_setting.logo.url = last_site_setting.logo.url
                
        #     else:
        #         site_setting.logo.url = None
        

        if request.FILES.get('image') is not None:
            uploaded_image = request.FILES['image']
            ext = uploaded_image.name.split('.')[-1]
            timestamp = datetime.now().strftime('%Y%m%d%H%M%S')
            new_name_image = f"{title}{timestamp}.{ext}"
            site_setting.image.save(new_name_image, uploaded_image)
            
        # else:

        #     last_site_setting = Site_setting.objects.last()
            
        #     if last_site_setting.image.url:
        #         site_setting.image.url = last_site_setting.image.url
                
        #     else:
        #         site_setting.image.url = None
        

        if request.FILES.get('video') is not None:
            uploaded_file = request.FILES['video']
            ext = uploaded_file.name.split('.')[-1]
            timestamp = datetime.now().strftime('%Y%m%d%H%M%S')
            new_name_video = f"{title}{timestamp}.{ext}"
            site_setting.video.save(new_name_video, uploaded_file)
            
        # else:

        #     last_site_setting = Site_setting.objects.last()
            
        #     if last_site_setting.video.url:
        #         site_setting.video.url = last_site_setting.video.url
                
        #     else:
        #         site_setting.video.url = None
        

        if request.FILES.get('resume') is not None:
            uploaded_file = request.FILES['resume']
            ext = uploaded_file.name.split('.')[-1]
            timestamp = datetime.now().strftime('%Y%m%d%H%M%S')
            new_name_resume = f"{title}{timestamp}.{ext}"
            site_setting.resume.save(new_name_resume, uploaded_file)
            
        # else:

        #     last_site_setting = Site_setting.objects.last()
            
        #     if last_site_setting.resume.url:
        #         site_setting.resume.url = last_site_setting.resume.url
                
        #     else:
        #         site_setting.resume.url = None
        

        site_setting.save()

        messages.success(request, "Site setting added successfully.")

        return HttpResponseRedirect(request.META.get('HTTP_REFERER', '/'))

