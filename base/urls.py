from django.urls import path
from .views import LoginViewPage, RegisterViewPage, ProfileViewPage
from django.contrib.auth.views import LogoutView

# app_name = "base"


urlpatterns = [
    path('', LoginViewPage.as_view(), name='login'),
    path('register/', RegisterViewPage.as_view(), name='register'),
    path('accounts/profile/', ProfileViewPage.as_view(), name='profile'),
    path('logout/', LogoutView.as_view(next_page='login'), name='logout'),
]
