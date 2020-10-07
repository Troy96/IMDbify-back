from django.urls import path
from watchedlist import views

urlpatterns = [
    path('', views.view_or_add_to_watchedlist),
    path('<int:movieId>', views.remove_from_watchedlist)
]