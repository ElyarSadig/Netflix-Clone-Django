from django.urls import path
from . import views

urlpatterns = [
    path('', views.home, name="home"),
    path('profile-list/', views.profileList, name="profile-list"),
    path('profile/create/', views.createProfile, name="create-profile"),
    path('watch/<str:pk>/', views.watch, name='watch'),
    path('movie/detail/<str:pk>', views.movieDetail, name='movie-detail'),
    path('movie/play/<str:pk>', views.showMovie, name='show-movie'),
]
