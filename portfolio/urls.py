
from django.urls import path
from portfolio import views
from middlewares.admin_auth import admin_middleware

urlpatterns = [
    path('add_portfolio/', admin_middleware(views.add_portfolio), name='admin_panel.add_portfolio'),
    path('add_portfolio_info/', admin_middleware(views.add_portfolio_info), name='admin_panel.add_portfolio_info'),
    path('all_portfolios/', admin_middleware(views.all_portfolios), name='admin_panel.all_portfolios'),
    path('delete_portfolio/<str:id>', admin_middleware(views.delete_portfolio), name='admin_panel.delete_portfolio'),
    path('update_portfolio/<str:id>', admin_middleware(views.update_portfolio), name='admin_panel.update_portfolio'),
    path('update_portfolio_info/', admin_middleware(views.update_portfolio_info), name='admin_panel.update_portfolio_info'),
]
