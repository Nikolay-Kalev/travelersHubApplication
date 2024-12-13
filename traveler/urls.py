from django.urls import path

from traveler import views

urlpatterns = [
    path('create/', views.create_traveler, name='traveler_create'),
    path('details/', views.traveler_details, name='traveler_details'),
    path('edit/', views.edit_traveler, name='traveler_edit'),
    path('delete/', views.delete_traveler, name='traveler_delete'),
]
