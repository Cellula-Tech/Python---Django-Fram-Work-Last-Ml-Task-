from django.shortcuts import render
from django.http import JsonResponse
import json
from django.views.decorators.csrf import csrf_exempt
from .model_utils import predict
import pandas as pd

def index_view(request):
    return render(request, 'app/index.html')

@csrf_exempt
def predict_view(request):
    print('Predict_View')
    if request.method == 'POST':
        try:
            data = json.loads(request.body)
            # Ensure the data is in the correct format for the model
            print(data)
            features = {
                'user_id': [data['user_id']],
                'user_name': [data['user_name']],
                'driver_name': [data['driver_name']],
                'car_condition': [data['car_condition']],
                'weather': [data['weather']],
                'traffic_condition': [data['traffic_condition']],
                'key': [data['key']],
                'pickup_datetime': [data['pickup_datetime']],
                'passenger_count': [int(data['passenger_count'])],
                'hour': [int(data['hour'])],
                'day': [int(data['day'])],
                'month': [int(data['month'])],
                'weekday': [int(data['weekday'])],
                'year': [int(data['year'])],
                'jfk_dist': [float(data['jfk_dist'])],
                'ewr_dist': [float(data['ewr_dist'])],
                'lga_dist': [float(data['lga_dist'])],
                'sol_dist': [float(data['sol_dist'])],
                'nyc_dist': [float(data['nyc_dist'])],
                'distance': [float(data['distance'])],
                'bearing': [float(data['bearing'])],
                'pickup_longitude_degrees': [float(data['pickup_longitude_degrees'])],
                'pickup_latitude_degrees': [float(data['pickup_latitude_degrees'])],
                'dropoff_longitude_degrees': [float(data['dropoff_longitude_degrees'])],
                'dropoff_latitude_degrees': [float(data['dropoff_latitude_degrees'])]
            }

            # Convert the features dictionary into a DataFrame
            features_df = pd.DataFrame(features)
            
            # Make the prediction using the DataFrame
            prediction = predict(features_df)
            
            return JsonResponse({'prediction': prediction.tolist()})
        except Exception as e:
            return JsonResponse({'error': str(e)}, status=400)
    else:
        return JsonResponse({'error': 'Only POST method is allowed'}, status=405)
