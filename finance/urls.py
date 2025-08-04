from django.urls import path,include
from .views  import RegisterView,Home




urlpatterns = [
    path('',Home.as_view(),name='home'),
    path('accounts/register/',RegisterView.as_view(),name='register'),
    # built in for login
    path('accounts/',include('django.contrib.auth.urls'),name='login'),
]
