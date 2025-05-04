
from django.urls import path
from site_setting import views
from middlewares.admin_auth import admin_middleware

urlpatterns = [
    path('add_site_setting/', admin_middleware(views.add_site_setting), name='admin_panel.add_site_setting'),
    path('add_site_setting_info/', admin_middleware(views.add_site_setting_info), name='admin_panel.add_site_setting_info'),
    # path('all_site_settings/', admin_middleware(views.all_site_settings), name='admin_panel.all_site_settings'),
    # path('delete_site_setting/<str:id>', admin_middleware(views.delete_site_setting), name='admin_panel.delete_site_setting'),
    # path('update_site_setting/<str:id>', admin_middleware(views.update_site_setting), name='admin_panel.update_site_setting'),
    # path('update_site_setting_info/', admin_middleware(views.update_site_setting_info), name='admin_panel.update_site_setting_info'),
]
