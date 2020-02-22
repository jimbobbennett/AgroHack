import logging
import os
import requests
import azure.functions as func

iot_central_api_token = os.environ['IOT_CENTRAL_API_TOKEN']

def needs_watering(soil_moisture):
    return soil_moisture < 500

def main(req: func.HttpRequest) -> func.HttpResponse:
    # Log the function was called
    logging.info('Python HTTP trigger function processed a request.')

    # Get the JSON from the request
    req_body = req.get_json()

    # Log the JSON
    logging.info(req_body)

    # The JSON can contain a single telemetry record or a list
    # If it's a list, get the last item
    if isinstance(req_body, list):
        req_body = req_body[-1]

    # Get the telemetry values
    temperature = req_body['temperature']
    pressure = req_body['pressure']
    humidity = req_body['humidity']
    soil_moisture = req_body['soil_moisture']

    # Log the values
    logging.info("temperature: %.1f, pressure: %.1f, pressure: %.1f, soil_moisture: %.1f",
                    temperature, pressure, humidity, soil_moisture)

    # Check if the plant needs watering
    request = { 'request' : needs_watering(soil_moisture) }

    # Call the REST API
    url = 'https://agro-hack-jim-2020.azureiotcentral.com/api/preview/devices/r5s4h6nner/components/EnvironmentSensor_7jx/commands/needs_watering'
    headers = {'Authorization': iot_central_api_token}

    requests.post(url, headers=headers, json = request)

    # Return a 200 status
    return func.HttpResponse(f"OK")



# iot_central_app = os.environ['IOT_CENTRAL_APP']
# maps_key = os.environ['MAPS_KEY']

# def get_location(device):
#     url = 'https://' + iot_central_app + '.azureiotcentral.com/api/preview/devices/' + device + '/cloudProperties'
#     headers = {'Authorization': iot_central_key}

#     r = requests.get(url, headers=headers)
#     location = json.loads(r.text)

#     return location['device_location']

# def get_weather(lat, lon):
#     url = 'https://atlas.microsoft.com/weather/forecast/daily/json?api-version=1.0&query=' + \
#           str(lat) + ',' + str(lon) + \
#           '&subscription-key=' + maps_key
    
#     r = requests.get(url)
#     weather = json.loads(r.text)
#     forecast = weather['forecasts'][0]
#     day_rain = forecast['day']['rain']['value']
#     night_rain = forecast['night']['rain']['value']

#     return day_rain + night_rain