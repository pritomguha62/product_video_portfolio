
from django.urls import path
from subscription import views
from middlewares.admin_auth import admin_middleware

urlpatterns = [
    # path('add_subscription/', admin_middleware(views.add_subscription), name='admin_panel.add_subscription'),
    # path('add_subscription_info/', admin_middleware(views.add_subscription_info), name='admin_panel.add_subscription_info'),
    path('send_mail/', admin_middleware(views.send_mail), name='admin_panel.send_mail'),
    path('send_mail_info/', admin_middleware(views.send_mail_info), name='admin_panel.send_mail_info'),
    path('add_subscription/', admin_middleware(views.add_subscription), name='admin_panel.add_subscription'),
    # path('add_subscription_info/', admin_middleware(views.add_subscription_info), name='admin_panel.add_subscription_info'),
    path('add_subscription_info/', views.add_subscription_info, name='add_subscription_info'),
    path('all_subscriptions/', admin_middleware(views.all_subscriptions), name='admin_panel.all_subscriptions'),
    path('delete_subscription/<str:id>', admin_middleware(views.delete_subscription), name='admin_panel.delete_subscription'),
    path('update_subscription/<str:id>', admin_middleware(views.update_subscription), name='admin_panel.update_subscription'),
    path('update_subscription_info/', admin_middleware(views.update_subscription_info), name='admin_panel.update_subscription_info'),
]
