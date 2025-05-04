from django.http import HttpResponse
from site_setting.models import Site_setting
from service.models import Service
from portfolio.models import Portfolio
from testimonial.models import Testimonial
from django.core.mail import EmailMessage
from django.template.loader import render_to_string
from datetime import datetime


from django.shortcuts import render

def home(request):
    
    site_setting = Site_setting.objects.last()
    # return HttpResponse(site_setting.title)

    services = Service.objects.all()

    portfolios = Portfolio.objects.all()
    
    testimonials = Testimonial.objects.order_by('-id')[:3]

    experience = datetime.now().year - 2018

    return render(request, 'pub_templates/index.html', {'site_setting':site_setting, 'services':services, 'portfolios':portfolios, 'testimonials':testimonials, 'experience':experience})


def contact_us_email(request):

    if request.method == "POST":
        name = request.POST.get("name", "")
        email = request.POST.get("email", "")
        service = request.POST.get("service", "")
        subject = "Contact with us."
        message = request.POST.get("message", "")
        site_setting = Site_setting.objects.last()
        # recipient = request.POST.get("email", "recipient@example.com")
        html_content = render_to_string("pub_templates/send_mail.html", {
            "name": name,
            "email": email,
            "service": service,
            "subject": subject,
            "message": message,
        })
        from_email = "contact@techpartit.net"
        recipient_list = ["recipient@example.com"]


        email = EmailMessage(subject, html_content, from_email, [site_setting.email])
        email.content_subtype = "html"  # Set the email content type to HTML
        email.send()
        return HttpResponse("Email sent successfully!")
    return HttpResponse("Submit the form to send an email.")


