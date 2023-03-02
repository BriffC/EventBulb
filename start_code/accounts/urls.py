from . import views
from django.urls import path
from django.contrib.auth.views import LoginView, LogoutView

urlpatterns = [
    path('Login/', LoginView.as_view(), name ='accounts_login'),
    path('Logout/', LogoutView.as_view(next_page = "/"), name = 'accounts_logout'),
    path('register/',views.register, name = 'accounts_register')
]
