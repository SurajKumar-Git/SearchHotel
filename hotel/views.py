from rest_framework import views
from rest_framework.response import Response
from rest_framework import status

from django.db.models import Count, F

from .models import Hotel
from .serializers import HotelSerializer
from .utils import distance_expression
# Create your views here.


class GetHotelsApiView(views.APIView):

    def get(self, request, *args, **kwargs):
        
        user_latitude = float(request.query_params.get("lat"))
        user_longitude = float(request.query_params.get("long"))

        if user_latitude and user_longitude:

            hotels = Hotel.objects.annotate(
                        distance = distance_expression(
                            user_latitude, 
                            user_longitude)
                            ).filter(distance__lte=100)
        else:
            hotels = Hotel.objects.all()

        ser_obj = HotelSerializer(hotels, many=True)
        return Response(ser_obj.data, status=status.HTTP_200_OK)

                    
                        
