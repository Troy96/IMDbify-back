from django.urls import  path
from movies import views

urlpatterns = [
    path('', views.MovieList.as_view()),
    path('<int:pk>', views.MovieDetail.as_view()),
    path('scrape', views.scrape_data)
]