from django.urls import path
from watchlist import views


urlpatterns = [
    path('', views.view_or_add_to_watchlist),
    path('<int:movieId>', views.remove_from_watchlist)
]