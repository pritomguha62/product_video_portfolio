
# Create your views here.
from django.shortcuts import render, redirect, get_object_or_404
from .models import *
import os
from django.http import HttpResponseRedirect, HttpResponse
from django.contrib import messages
from datetime import datetime
from service.models import Service
from site_setting.models import Site_setting


# Create your views here.

def add_portfolio(request):
    
    site_setting = Site_setting.objects.last()
    services = Service.objects.all()
    return render(request, 'admin_templates/add_portfolio.html', {'services': services, 'site_setting':site_setting})


def add_portfolio_info(request):
    if request.method == "POST":
        portfolio_info = request.POST

        title = portfolio_info.get('title')
        short_description = portfolio_info.get('short_description')
        description = portfolio_info.get('description')
        # service_id = request.POST.get("service")
        # service = Service.objects.get(id=service_id)
        link = portfolio_info.get('link')
        if portfolio_info.get('is_short') == '1':
            is_short = 'yes'
        else:
            is_short = 'no'

        # Portfolio.objects.create(
        #     title=title,
        #     short_description=short_description,
        #     description=description,
        #     image=image,
        #     video=video,
        #     service=service,
        #     link=link,
        # )

        portfolio = Portfolio()
        portfolio.title = title
        portfolio.short_description = short_description
        portfolio.description = description
        # portfolio.service = service
        portfolio.link = link
        portfolio.is_short = is_short

        if request.FILES.get('image') is not None:
            uploaded_image = request.FILES['image']
            ext = uploaded_image.name.split('.')[-1]
            timestamp = datetime.now().strftime('%Y%m%d%H%M%S')
            new_name_image = f"{title}{timestamp}.{ext}"
            portfolio.image.save(new_name_image, uploaded_image)

        if request.FILES.get('video') is not None:
            uploaded_file = request.FILES['video']
            ext = uploaded_file.name.split('.')[-1]
            timestamp = datetime.now().strftime('%Y%m%d%H%M%S')
            new_name_video = f"{title}{timestamp}.{ext}"
            portfolio.video.save(new_name_video, uploaded_file)

        portfolio.save()

        messages.success(request, "Portfolio added successfully.")

        return HttpResponseRedirect(request.META.get('HTTP_REFERER', '/'))


def all_portfolios(request):
    
    site_setting = Site_setting.objects.last()
    portfolios = Portfolio.objects.all()
    return render(request, 'admin_templates/portfolios.html', {'portfolios': portfolios, 'site_setting':site_setting})


def delete_portfolio(request, id):
    portfolio = get_object_or_404(Portfolio, id=id)
    if portfolio.image and os.path.isfile(portfolio.image.path):
        os.remove(portfolio.image.path)
    if portfolio.video and os.path.isfile(portfolio.video.path):
        os.remove(portfolio.video.path)
    portfolio.delete()
    messages.success(request, "Portfolio deleted successfully.")
    # return redirect('blog_post_detail', id=service.id)
    return HttpResponseRedirect(request.META.get('HTTP_REFERER', '/'))


def update_portfolio(request, id):
    
    site_setting = Site_setting.objects.last()
    update_portfolio = get_object_or_404(Portfolio, id=id)
    return render(request, 'admin_templates/update_portfolio.html', {'update_portfolio':update_portfolio, 'site_setting':site_setting})


def update_portfolio_info(request):
    portfolio = get_object_or_404(Portfolio, id=request.POST.get('id'))
    if request.method == "POST":
        portfolio_info = request.POST

        title = portfolio_info.get('title')
        short_description = portfolio_info.get('short_description')
        description = portfolio_info.get('description')
        link = portfolio_info.get('link')
        # service_id = portfolio_info.get('service')
        # service = Service.objects.get(id=service_id)
        image = request.FILES.get('image')
        video = request.FILES.get('video')

        portfolio.title = title
        portfolio.short_description = short_description
        portfolio.description = description
        portfolio.link = link
        # portfolio.service = service

        if image is not None:
            if portfolio.image and os.path.isfile(portfolio.image.path):
                os.remove(portfolio.image.path)
            uploaded_image = request.FILES['image']
            ext = uploaded_image.name.split('.')[-1]
            timestamp = datetime.now().strftime('%Y%m%d%H%M%S')
            new_name = f"{title}{timestamp}.{ext}"
            portfolio.image.save(new_name, uploaded_image)

        if video is not None:
            if portfolio.video and os.path.isfile(portfolio.video.path):
                os.remove(portfolio.video.path)
            uploaded_file = request.FILES['video']
            ext = uploaded_file.name.split('.')[-1]
            timestamp = datetime.now().strftime('%Y%m%d%H%M%S')
            new_name_video = f"{title}{timestamp}.{ext}"
            portfolio.video.save(new_name_video, uploaded_file)

        portfolio.save()

        messages.success(request, "Portfolio Updated successfully.")

        return HttpResponseRedirect(request.META.get('HTTP_REFERER', '/'))


