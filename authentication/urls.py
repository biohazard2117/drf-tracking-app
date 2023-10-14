from authentication import views
from django.urls import path


urlpatterns = [
    path('register', views.RegisterView.as_view(), name='register'),
    path('login', views.LoginView.as_view(), name='login'),
    path('user', views.AuthUserView.as_view(), name='user'), 
]
