# Loop up the weather for the device using Azure Maps

In the [previous step](./ExecuteIoTCommand.md) you added to the function to trigger the Azure IoT Central command with a value depending on the level of the soil moisture, turning the LED off if the soil is wet, and on if it is dry. In this step you will call Azure Maps to check the weather forecast before sending the needs watering command.

## Azure Maps

[Azure Maps](https://azure.microsoft.com/services/azure-maps/?WT.mc_id=agrohack-github-jabenn) is an Azure service that provides mapping and related data. You can use it for visualizing maps on a web page with added data, or requesting spatial data, such as if a coordinate is inside a shape on a map, and even weather data.

For our soil moisture rule, if the soil is too dry then the plant needs a water. However, there is no need to water the plant if rain is predicted. Azure Maps can get the weather for the plants location, and from this the precipitation levels can be extracted to see if it will rain.

For this workshop, the location will be hard coded, but in a real world app this would be set against each device, either by using GPS on the device, or set by the end user via a Cloud Property. You can read more on Cloud Properties in the [Azure IoT Central docs](https://docs.microsoft.com/azure/iot-central/core/howto-set-up-template?WT.mc_id=agrohack-github-jabenn#add-cloud-properties).

### Create an Azure Maps instance

Azure Maps resources can be created using the Azure Portal or the Azure CLI

#### Create an Azure Maps instance using the Azure Portal


