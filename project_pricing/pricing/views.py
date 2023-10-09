from datetime import datetime
from django.shortcuts import get_object_or_404, render
from .models import Config, TimeTier, Week
from rest_framework.decorators import api_view
from rest_framework.response import Response
from rest_framework import status

# Create your views here.
def index(request):
    data = Config.objects.all()
    print(data[0].name)
    return render(request, "home.html", {'name': data[0].name})

@api_view(['GET'])
def calculate_ride_pricing(request):
    try:
        ride_duration = request.query_params.get('duration')
        ride_date = request.query_params.get('date')
        total_distance = request.query_params.get('total_distance')
        ride_day = datetime.strptime(ride_date, '%Y-%m-%d').strftime('%A')

        #fetch data from databases
        week = get_object_or_404(Week, day=ride_day)
        config = get_object_or_404(Config, is_active=True)

        #time tier pricing
        time_tiers = TimeTier.objects.get(config_key=config)
        while(ride_duration):
            print('in time-tiers, calculate and keep just the total-time for each tier and with the loop try and deduce the total time_pricing')

        #Distance-Base-Tier pricing
        distance_base_price = DistanceBaseTier.objects.get(config_key=config, max_base_tier_distance__gte=total_distance)

        #Distance-Additional-Tier pricing
        additional_distance_price = DistanceAdditionalTier.objects.get(config_key=config, per_km_price__lte=your_price_criteria)

        #Waiting time pricing
        waiting = Waiting.objects.get(config_key=config, free_mins__gte=ride_duration, per_min_charge__lte=your_charge_criteria)

        return 'Return the result of the calculation here'
    except Exception as e:
        return Response({'error': str(e)}, status=status.HTTP_400_BAD_REQUEST)