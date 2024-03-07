from django.urls import path
from .views import reservationList,reservationsDetail

urlpatterns = [
    path('reservations/', reservationList.as_view(), name='reservation-list-create'),
    path('reservations/<int:pk>/', reservationsDetail.as_view(), name='reservation-detail'),
]