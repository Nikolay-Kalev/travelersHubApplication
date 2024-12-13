from django.urls import path

from common import views

urlpatterns = [
    path('', views.home_view, name='home'),
    path('all-trips/', views.all_trips_view, name='all_trips'),
]
