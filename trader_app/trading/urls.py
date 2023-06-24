from django.urls import path
from .views import user_dashboard, trader_sign_up, trader_sign_in, trader_logout, admin_dashboard


app_name = 'trading'

urlpatterns = [
    path('', trader_sign_up, name='trader_sign_up'),
    path('trader_sign_in/', trader_sign_in, name='trader_sign_in'),
    path('trader_logout/', trader_logout, name='trader_logout'),
    path('user_dashboard/<slug:slug>/', user_dashboard, name='user_dashboard'),
    path('admin_dashboard/', admin_dashboard, name='admin_dashboard'),
]
