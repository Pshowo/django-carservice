from django.urls import path
from . import views

urlpatterns = [
    path('', views.WelcomeView.as_view()),
    path('menu/', views.menu, name='menu'),
]