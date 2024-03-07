from django.shortcuts import render
from rest_framework.decorators import api_view,permission_classes,authentication_classes
from rest_framework.permissions import IsAuthenticated ,IsAdminUser
from rest_framework.authentication import BasicAuthentication

from .models import *
from .serializers import ReservationSerializer
from rest_framework.response import Response
from rest_framework.views import APIView
from django.http import Http404
from rest_framework import status
from django.shortcuts import get_object_or_404
# Create your views here.


class reservationList(APIView):
    
    permission_classes = [IsAuthenticated]  # Require authenticated user
    def get(self, request, format=None):
        reservations =Reservation.objects.all()
        serializer =  ReservationSerializer(reservations, many=True)
        return Response(serializer.data)
    def post(self, request, format=None):
        serializer =  ReservationSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
class reservationsDetail(APIView):
    @permission_classes([IsAuthenticated])

    def get_object(self, pk):
        try:
            return Reservation.objects.get(pk=pk)
        except Reservation.DoesNotExist:
            raise Http404

    def get(self, request, pk, format=None):
        reservation = self.get_object(pk)
        serializer = ReservationSerializer(reservation)
        return Response(serializer.data)

    def put(self, request, pk, format=None):
        reservation = self.get_object(pk)
        serializer = ReservationSerializer(reservation, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    def delete(self, request, pk, format=None):
        reservation = self.get_object(pk)
        reservation.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)