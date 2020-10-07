from django.urls import  path
from users.views import  create
from rest_framework.authtoken import views



urlpatterns = [
    path('signup/', create),
    path('login/', views.obtain_auth_token)
]