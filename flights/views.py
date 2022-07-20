from .models import Booking, Flight
from rest_framework.generics import ListAPIView 
from .serializer import ListSerializer
import datetime



class flightApiView(ListAPIView):
    queryset = Flight.objects.all()
    serializer_class = ListSerializer 


 
class BookingApiView(ListAPIView):
    queryset = Booking.objects.all().filter(date__gte =datetime.date.today())
    serializer_class = ListSerializer    