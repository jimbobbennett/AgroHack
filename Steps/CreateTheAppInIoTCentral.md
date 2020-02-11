# Creating the application using Azure IoT Central

[Azure IoT Central](https://azure.microsoft.com/services/iot-central/?WT.mc_id=agrohack-github-jabenn) is an IoT Software-as-a-service (SaaS) platform. This allows you to define an service that can interact with IoT devices, sending data both ways from device to cloud, and cloud to device. You can define the capabilities of each device, and create dashboards to show data.

## Creating your first IoT Central app

1. Head to [apps.azureiotcentral.com](https://apps.azureiotcentral.com/?WT.mc_id=agrohack-github-jabenn)
1. From the menu on the side, select **Build**
1. Select **Custom Apps**
1. Sign in with your Microsoft account if needed
1. Fill in your application details:
    1. Give your application a name that makes sense to you, such as `Agro Hack`
    1. Provide a unique URL for your app. This needs to be globally unique, so include things such as the data or your name. For example `agro-hack-jim-2020`.
    1. Leave the Application Template as `Custom Template`
    1. Select a pricing plan. This hack only uses 2 devices, so is free for all tiers, so select the one that makes sense for you. The Free tier is ideal as long as you don't want your code to run longer than 7 days.

       For the free tier you will need to provide a name and phone number, that will be verified. For the other tiers you will need an Azure subscription. You can find details on different free subscriptions [here](https://github.com/jimbobbennett/AgroHack/blob/master/README.md#azure-account).
    1. Select **Create**

Your application will be provisioned, and you will see the dashboard once it is ready.

## Defining the device templates

IoT Central can work with multiple types of device, and multiple devices per device type. Device types are defined using templates - these specify the capabilities of the device including the telemetry that can be received from the device, and commands that can be sent to it.

For the 

## Defining the devices

## Building the dashboards