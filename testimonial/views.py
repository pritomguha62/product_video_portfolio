from django.shortcuts import render, redirect, get_object_or_404
from .models import *
import os
from django.http import HttpResponseRedirect, HttpResponse
from django.contrib import messages
from datetime import datetime
from site_setting.models import Site_setting

# Create your views here.

def add_testimonial(request):
    
    site_setting = Site_setting.objects.last()
    return render(request, 'admin_templates/add_testimonial.html', {'site_setting':site_setting})

def add_testimonial_info(request):
    
    if request.method == "POST":
        
        testimonial_info = request.POST
        
        title = testimonial_info.get('title')
        short_description = testimonial_info.get('short_description')
        description = testimonial_info.get('description')
        image = request.FILES.get('image')
        

        testimonial = Testimonial()
        testimonial.title = title
        testimonial.short_description = short_description
        testimonial.description = description

        if request.FILES.get('image') is not None:
            uploaded_image = request.FILES['image']
            ext = uploaded_image.name.split('.')[-1]
            timestamp = datetime.now().strftime('%Y%m%d%H%M%S')
            new_name_image = f"{title}{timestamp}.{ext}"
            testimonial.image.save(new_name_image, uploaded_image)
            
        testimonial.save()

        messages.success(request, "Testimonial added successfully.")

        return HttpResponseRedirect(request.META.get('HTTP_REFERER', '/'))

def all_testimonials(request):
    
    site_setting = Site_setting.objects.last()
    testimonials = Testimonial.objects.all()
    return render(request, 'admin_templates/testimonials.html', {'testimonials':testimonials, 'site_setting':site_setting})


def delete_testimonial(request, id):
    testimonial = get_object_or_404(Testimonial, id=id)
    if testimonial.image and os.path.isfile(testimonial.image.path):
        os.remove(testimonial.image.path)
    testimonial.delete()
    messages.success(request, "Testimonial deleted successfully.")
    # return redirect('blog_post_detail', id=testimonial.id)
    return HttpResponseRedirect(request.META.get('HTTP_REFERER', '/'))


def update_testimonial(request, id):
    
    site_setting = Site_setting.objects.last()
    update_testimonial = get_object_or_404(Testimonial, id=id)
    return render(request, 'admin_templates/update_testimonial.html', {'update_testimonial':update_testimonial, 'site_setting':site_setting})


def update_testimonial_info(request):
    testimonial = get_object_or_404(Testimonial, id=request.POST.get('id'))
    if request.method == "POST":
        testimonial_info = request.POST

        title = testimonial_info.get('title')
        short_description = testimonial_info.get('short_description')
        description = testimonial_info.get('description')
        image = request.FILES.get('image')

        testimonial.title = title
        testimonial.short_description = short_description
        testimonial.description = description

        if image is not None:
            if testimonial.image and os.path.isfile(testimonial.image.path):
                os.remove(testimonial.image.path)
            uploaded_image = request.FILES['image']
            ext = uploaded_image.name.split('.')[-1]
            timestamp = datetime.now().strftime('%Y%m%d%H%M%S')
            new_name = f"{title}{timestamp}.{ext}"
            testimonial.image.save(new_name, uploaded_image)

        testimonial.save()

        messages.success(request, "Testimonial Updated successfully.")

        return HttpResponseRedirect(request.META.get('HTTP_REFERER', '/'))

