from django.urls import path, include

from trips import views

urlpatterns = [
    path('create/', views.create_trip_view, name='create_trip'),
    path('<int:trip_pk>/', include([
        path('details/', views.trip_details, name='trip_details'),
        path('edit/', views.edit_trip, name='edit_trip'),
        path('delete/', views.delete_trip, name='delete_trip'),
    ]))
]
