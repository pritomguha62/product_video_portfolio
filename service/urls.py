
from django.urls import path, include
from service import views
from middlewares.admin_auth import admin_middleware

urlpatterns = [
    path('add_service/', admin_middleware(views.add_service), name='admin_panel.add_service'),
    path('add_service_info/', admin_middleware(views.add_service_info), name='admin_panel.add_service_info'),
    path('all_services/', admin_middleware(views.all_services), name='admin_panel.all_services'),
    path('delete_service/<str:id>', admin_middleware(views.delete_service), name='admin_panel.delete_service'),
    path('update_service/<str:id>', admin_middleware(views.update_service), name='admin_panel.update_service'),
    path('update_service_info/', admin_middleware(views.update_service_info), name='admin_panel.update_service_info'),
]
