from django.urls import path
from . import views

urlpatterns = [
    path('', views.WelcomeView.as_view()),
    path('menu/', views.menu, name='menu'),
    path('get_ticket/change_oil/', views.Wait.as_view()),
    path('get_ticket/inflate_tires/', views.Wait.as_view()),
    path('get_ticket/diagnostic/', views.Wait.as_view()),
    path('processing', views.Processing.as_view()),
    path('next', views.Next.as_view()),
]