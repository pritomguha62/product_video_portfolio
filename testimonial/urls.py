
from django.urls import path
from testimonial import views
from middlewares.admin_auth import admin_middleware

urlpatterns = [
    path('add_testimonial/', admin_middleware(views.add_testimonial), name='admin_panel.add_testimonial'),
    path('add_testimonial_info/', admin_middleware(views.add_testimonial_info), name='admin_panel.add_testimonial_info'),
    path('all_testimonials/', admin_middleware(views.all_testimonials), name='admin_panel.all_testimonials'),
    path('delete_testimonial/<str:id>', admin_middleware(views.delete_testimonial), name='admin_panel.delete_testimonial'),
    path('update_testimonial/<str:id>', admin_middleware(views.update_testimonial), name='admin_panel.update_testimonial'),
    path('update_testimonial_info/', admin_middleware(views.update_testimonial_info), name='admin_panel.update_testimonial_info'),
]
