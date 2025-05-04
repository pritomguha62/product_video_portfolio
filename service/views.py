from django.shortcuts import render, redirect, get_object_or_404
from .models import *
import os
from django.http import HttpResponseRedirect
from django.contrib import messages
from datetime import datetime
from site_setting.models import Site_setting

# Create your views here.

def add_service(request):
    
    site_setting = Site_setting.objects.last()
    return render(request, 'admin_templates/add_service.html', {'site_setting':site_setting})

def add_service_info(request):
    
    if request.method == "POST":
        
        service_info = request.POST
        
        title = service_info.get('title')
        short_description = service_info.get('short_description')
        description = service_info.get('description')
        image = request.FILES.get('image')

        service = Service()
        service.title = title
        service.short_description = short_description
        service.description = description

        if request.FILES.get('image') is not None:
            uploaded_image = request.FILES['image']
            ext = uploaded_image.name.split('.')[-1]
            timestamp = datetime.now().strftime('%Y%m%d%H%M%S')
            new_name_image = f"{title}{timestamp}.{ext}"
            service.image.save(new_name_image, uploaded_image)
            
        service.save()

        messages.success(request, "Service added successfully.")

        return HttpResponseRedirect(request.META.get('HTTP_REFERER', '/'))

def all_services(request):
    
    site_setting = Site_setting.objects.last()
    services = Service.objects.all()
    return render(request, 'admin_templates/services.html', {'services':services, 'site_setting':site_setting})


def delete_service(request, id):
    service = get_object_or_404(Service, id=id)
    if service.image and os.path.isfile(service.image.path):
        os.remove(service.image.path)
    service.delete()
    messages.success(request, "Service deleted successfully.")
    # return redirect('blog_post_detail', id=service.id)
    return HttpResponseRedirect(request.META.get('HTTP_REFERER', '/'))


def update_service(request, id):
    
    site_setting = Site_setting.objects.last()
    update_service = get_object_or_404(Service, id=id)
    return render(request, 'admin_templates/update_service.html', {'update_service':update_service, 'site_setting':site_setting})


def update_service_info(request):
    service = get_object_or_404(Service, id=request.POST.get('id'))
    if request.method == "POST":
        service_info = request.POST

        title = service_info.get('title')
        short_description = service_info.get('short_description')
        description = service_info.get('description')
        image = request.FILES.get('image')

        service.title = title
        service.short_description = short_description
        service.description = description

        if image is not None:
            if service.image and os.path.isfile(service.image.path):
                os.remove(service.image.path)
            uploaded_image = request.FILES['image']
            ext = uploaded_image.name.split('.')[-1]
            timestamp = datetime.now().strftime('%Y%m%d%H%M%S')
            new_name = f"{title}{timestamp}.{ext}"
            service.image.save(new_name, uploaded_image)

        service.save()

        messages.success(request, "Service Updated successfully.")

        return HttpResponseRedirect(request.META.get('HTTP_REFERER', '/'))

