import imp
from rest_framework import serializers
from .models import Booking, Flight

class ListSerializer (serializers.ModelSerializer):
    class Meta:
        model = Flight
        fields = ["id","destination","time","price"]

        model = Booking
        fields = ["flight","date","id"]