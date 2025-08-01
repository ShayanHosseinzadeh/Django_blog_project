from django.contrib.auth.views import LoginView
from django.urls import path
from . import views
from .forms import MyAuthenticationForm

urlpatterns = [
    path('signup/', views.SignUpView.as_view(), name='signup'),
    path('login/', LoginView.as_view(template_name='registration/login.html', authentication_form=MyAuthenticationForm),
         name='login'),

]