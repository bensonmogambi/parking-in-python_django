from django.urls import path
from . import views

urlpatterns = [
    path('available_parking/', views.available_parking, name='available_parking'),
    path('book_parking/<int:space_id>/', views.book_parking, name='book_parking'),
    path('booking_confirmation/<int:booking_id>/', views.booking_confirmation, name='booking_confirmation'),
]
