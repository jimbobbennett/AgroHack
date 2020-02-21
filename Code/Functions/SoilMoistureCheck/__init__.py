import logging, json, os
import requests
import azure.functions as func

# iot_central_key = os.environ['IOT_CENTRAL_KEY']
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

def main(req: func.HttpRequest) -> func.HttpResponse:
    logging.info('Python HTTP trigger function processed a request.')

    req_body = req.get_json()

    logging.info(req_body)

    if isinstance(req_body, list):
        req_body = req_body[-1]

    temperature = req_body['temperature']
    pressure = req_body['pressure']
    humidity = req_body['humidity']
    soil_moisture = req_body['soil_moisture']

    print("temperature:", temperature, "pressure:", pressure, "humidity:", humidity, "soil_moisture:", soil_moisture)

    # device = req_body['device']['id']

    # device_location = get_location(device)
    # rain = get_weather(device_location['lat'], device_location['lon'])


    # telemetry = req_body['data']
    # moisture = [t['value'] for t in telemetry if t['name'] == 'soil_moisture'][0]

    # print('device', device, 'moisture = ', moisture)

    return func.HttpResponse(f"OK")
