from django.shortcuts import render, redirect, get_object_or_404
from .models import *
import os
from django.http import HttpResponseRedirect, HttpResponse
from django.contrib import messages
from datetime import datetime
from site_setting.models import Site_setting
from django.core.mail import EmailMessage
from django.template.loader import render_to_string

# Create your views here.

def add_subscription(request):
    
    site_setting = Site_setting.objects.last()
    return render(request, 'admin_templates/add_subscription.html', {'site_setting':site_setting})

def add_subscription_info(request):
    
    if request.method == "POST":
        
        subscription_info = request.POST
        
        title = subscription_info.get('title')
        email = subscription_info.get('email')
        

        subscription = Subscription()
        subscription.title = title
        subscription.email = email

        subscription.save()

        messages.success(request, "Subscription added successfully.")

        return HttpResponseRedirect(request.META.get('HTTP_REFERER', '/'))

def all_subscriptions(request):
    
    site_setting = Site_setting.objects.last()
    subscriptions = Subscription.objects.all()
    return render(request, 'admin_templates/subscriptions.html', {'subscriptions':subscriptions, 'site_setting':site_setting})


def delete_subscription(request, id):
    subscription = get_object_or_404(Subscription, id=id)
    # if subscription.image and os.path.isfile(subscription.image.path):
    #     os.remove(subscription.image.path)
    subscription.delete()
    messages.success(request, "Subscription deleted successfully.")
    # return redirect('blog_post_detail', id=subscription.id)
    return HttpResponseRedirect(request.META.get('HTTP_REFERER', '/'))


def update_subscription(request, id):
    
    site_setting = Site_setting.objects.last()
    update_subscription = get_object_or_404(Subscription, id=id)
    return render(request, 'admin_templates/update_subscription.html', {'update_subscription':update_subscription, 'site_setting':site_setting})


def update_subscription_info(request):
    subscription = get_object_or_404(Subscription, id=request.POST.get('id'))
    if request.method == "POST":
        subscription_info = request.POST

        title = subscription_info.get('title')
        email = subscription_info.get('email')

        subscription.title = title
        subscription.email = email
        subscription.save()

        messages.success(request, "Subscription Updated successfully.")

        return HttpResponseRedirect(request.META.get('HTTP_REFERER', '/'))
    
def send_mail(request):

    site_setting = Site_setting.objects.last()
    return render(request, 'admin_templates/send_mail.html', {'site_setting':site_setting})

def send_mail_info(request):

    if request.method == "POST":
        
        site_setting = Site_setting.objects.last()
        seubscriptions = Subscription.objects.all()
        
        for subscription in seubscriptions:
    
            name = request.POST.get("name", site_setting.name)
            email = request.POST.get("email", site_setting.email)
            service = request.POST.get("service", "")
            subject = request.POST.get("Subject", site_setting.name+" Contact")
            message = request.POST.get("message", "")
            # recipient = request.POST.get("email", "recipient@example.com")
            html_content = render_to_string("pub_templates/send_mail.html", {
                "name": name,
                "email": email,
                # "service": service,
                "subject": subject,
                "message": message,
            })
            from_email = "contact@techpartit.net"
            recipient_list = ["recipient@example.com"]


            email = EmailMessage(subject, html_content, from_email, [subscription.email])
            email.content_subtype = "html"  # Set the email content type to HTML
            email.send()
            
        return HttpResponse("Email sent successfully!")
    return HttpResponse("Submit the form to send an email.")

