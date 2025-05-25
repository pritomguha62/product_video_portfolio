import base64

from django.shortcuts import render, redirect, HttpResponseRedirect
from django.http import HttpResponse, JsonResponse
from django.core.files.base import ContentFile
# import face_recognition
from .forms import UserRegistrationForm
from django.contrib.auth import login, authenticate, logout
from django.contrib import messages
from .models import *
from site_setting.models import Site_setting
from django.contrib.auth import get_user_model
from django.views.decorators.csrf import csrf_exempt

# User = get_user_model()

# Create your views here.

def dashboard(request):
    
    site_setting = Site_setting.objects.last()
    
    return render(request, 'admin_templates/dashboard.html', {'site_setting':site_setting})

def signin(request):
    
    site_setting = Site_setting.objects.last()
    return render(request, 'admin_templates/admin_signin.html', {'site_setting':site_setting})

def face_login(request):
    return render(request, 'admin_templates/face_login.html')

def signup(request):
    
    site_setting = Site_setting.objects.last()
    return render(request, 'admin_templates/admin_signup.html', {'site_setting':site_setting})

def signin_info(request):

    if request.method == "POST":

        email = request.POST.get('email')

        password = request.POST.get('password')

        rememberme = request.POST.get('remeberme')

        user = authenticate(email=email, password=password)
        

        if user is not None and user.is_staff == 1:
            if rememberme:  # If "Remember Me" is checked
                request.session.set_expiry(1209600)  # 2 weeks
            else:  # Default session expiry (browser close)
                request.session.set_expiry(0)

            login(request, user)

            # Set custom session data
            request.session['email'] = user.email
            request.session['is_admin'] = user.is_staff

            # return HttpResponse(user.is_staff)
            return redirect('dashboard')
        else:
            messages.error(request, "Login Invalid.")
            return HttpResponseRedirect(request.META.get('HTTP_REFERER', '/'))

@csrf_exempt
def face_login_info(request):
    email = request.POST.get('email')

    face_image_data = request.POST['face_image']

    try:
        admin = CustomAdmin.objects.get(email = email)

        email_username = email.split("@")[1]

    except admin.DoesNotExist:
        return JsonResponse({
            'status' : 'error', 'message' : 'Invalid Username!'
    })

    face_image_data = face_image_data.split(",")[1]

    uploaded_image = ContentFile(base64.b64decode({face_image_data},name=f'{email_username}_.jpg'))

    upload_face_image = face_recognition.load_image_file(uploaded_image)

    upload_face_encoding = face_recognition.face_encodings(upload_face_image)

    if upload_face_encoding:
        upload_face_encoding = upload_face_encoding[0]
        user_iamge = CustomAdmin.objects.filter(user = user).last()
        stored_face_image = face_recognition.load_image_file(user_iamge.face_image.path)
        stored_face_encoding = face_recognition.face_encodings(stored_face_image)

        match = face_recognition.compare_faces([stored_face_encoding], upload_face_encoding)

    email = request.POST.get('email')

    face_image = request.POST['face_image']




    # user = authenticate(email=email, password=password)
    #
    # if user is not None:
    #     login(request, user)
    #
    #     # Set custom session data
    #     request.session['email'] = user.email
    #     request.session['is_admin'] = user.is_staff
    #
    #     # return HttpResponse(user.is_staff)
    #     return redirect('dashboard')
    # else:
    #     messages.error(request, "Invalid username or password.")
    #     return HttpResponseRedirect(request.META.get('HTTP_REFERER', '/'))


def signup_info(request):

    if request.method == 'POST':
        form = UserRegistrationForm(request.POST)
        if form.is_valid():
            user = form.save()
            user.set_password(form.cleaned_data['password'])
            user.save()
            login(request, user)  # Log the user in after registration
            return redirect('home')  # Replace 'home' with your desired redirect URL
    else:
        form = UserRegistrationForm()
    return render(request, 'admin_templates/admin_signup.html', {'form': form})

def sign_out(request):
    # Log out the user
    logout(request)
    # Destroy the session completely
    request.session.flush()
    # Redirect to a specific page
    return redirect('home')

