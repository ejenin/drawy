from django.urls import path

from . import views

urlpatterns = [
    path('', views.HomePageView.as_view(), name='index'),
    path('getRandom', views.getRandomClass, name='random'),
    path('guessImage', views.guessImage, name='guess')
]