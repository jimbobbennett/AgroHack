# Create the application using Azure IoT Central

[Azure IoT Central](https://azure.microsoft.com/services/iot-central/?WT.mc_id=agrohack-github-jabenn) is an IoT Software-as-a-service (SaaS) platform. This allows you to define an service that can interact with IoT devices, sending data both ways from device to cloud, and cloud to device. You can define the capabilities of each device, and create dashboards to show data.

## Create your first IoT Central app

To create your app, you can either create it manually from scratch to learn about how to build IoT Central apps, or create it from a pre-defined template if you want to save time and already know how to use IoT Central.

### Create the app from a template

1. Follow this link to create a new IoT Central app pre-configured for this workshop:

   [apps.azureiotcentral.com/build/new/59a05afb-9cd6-4d41-8554-7389f5277ec8](https://apps.azureiotcentral.com/build/new/59a05afb-9cd6-4d41-8554-7389f5277ec8)

1. Sign in with your Microsoft account if needed
1. Give your application a name that makes sense to you, such as `Agro Hack`
1. Provide a unique URL for your app. This needs to be globally unique, so include things such as the data or your name. For example `agro-hack-jim-2020`.
1. Select a pricing plan. This hack only uses 2 devices, so is free for all tiers, so select the one that makes sense for you. The Free tier is ideal as long as you don't want your code to run longer than 7 days.

    For the free tier you will need to provide a name and phone number, that will be verified. For the other tiers you will need an Azure subscription. You can find details on different free subscriptions [here](https://github.com/jimbobbennett/AgroHack/blob/master/README.md#azure-account).

1. Select **Create**

Your application will be provisioned, and you will see the dashboard once it is ready.

Head to [Create a device](#CreateADevice) to configure a device inside the IoT Central app.

### Creating the app manually

#### Provision the app

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

#### Define the device template

IoT Central can work with multiple types of device, and multiple devices per device type. Device types are defined using templates - these specify the capabilities of the device including the telemetry that can be received from the device, and commands that can be sent to it.

The environment sensor captures temperature, humidity, air pressure and soil moisture. You will need to define a template that has these values on it, so they can be received from the Pi.

1. From the left-hand menu, select **Device Templates**

   ![The device templates menu item](../Images/DeviceTemplatesMenu.png)

1. Select the **+ New** button from the top menu

   ![The new device template button](../Images/NewDeviceTemplateButton.png)

1. Select the **IoT Device** template

   ![The template type selector](../Images/SelectIoTDeviceType.png)

1. Select the **Next: Customize** button
1. Select the **Next: Review** button
1. Select the **Create** button
1. Name the template `Environment Sensor`

Once the template is created, you need to add capabilities to it. These are defined using **capability models**, which define the capabilities of all devices that will use this template. Capability models are made up of three parts:

* **Interfaces** - these are reusable collections of capabilities, and are grouped into three categories:

   1. **Telemetry** - actual values detected and sent but the device, for example in a thermostat it could be the current detected temperature
   1. **Properties** - settings on the device, for example in a thermostat it could be the desired temperature
   1. **Commands** - calls that can be made on the device from IoT Central, optionally passing data. For example in a thermostat it could be called by a mobile app to send a request to change the desired temperature.

* **Cloud properties** - these are properties set in IoT central against a device, but not synced to the device. For example a device could have a cloud property for the account name of the owner, or the date it was last services

* **Views** - these are dashboards for a device that can contain charts, data values and other information allowing you to visualize telemetry or send commands.

The environment sensor needs a capability model created, with an interface defined for the telemetry values being sent, and a view to visualize these values.

1. Select the **Custom** capability model

   ![The capability model selector](../Images/SelectCapabilityModel.png)

##### Add an interface

1. Add a new interface to the capability model by selecting the top level *Environment sensor* item in the menu and selecting **+Add interface**

   ![The add interface option](../Images/AddInterface.png)

1. Select **Custom**

   ![The custom interface option](../Images/CustomInterface.png)

This interface needs 4 telemetry values added to it for the temperature, pressure, humidity and soil moisture. Telemetry values have the following properties:

* **Display name** - this defines what is shown on a view to display the value
* **Name** - this maps to the values being sent from the device
* **Capability type** - this defines what type of value this is, and includes some standard types such as temperature or pressure.
* **Schema** - this defines the data type for the value being received, such as an integer or a floating point number
* **Unit** - this defines the unit for know telemetry types, for example °C for temperatures.

1. Select the **+ Add capability** button to add new capabilities, and add the following:

   |  Display Name | Name          | Capability Type | Schema | Unit |
   | ------------- | ------------- | --------------- | ------ | ---- |
   | Temperature   | temperature   | Temperature     | Double | °C   |
   | Pressure      | pressure      | Pressure        | Double | kPa  |
   | Humidity      | humidity      | Humidity        | Double | %    |
   | Soil Moisture | soil_moisture | None            | Double | None |

1. Select the **Save** button from the top menu

   ![The save interface button](../Images/SaveInterface.png)

##### Add a view

A view is used to visualize this telemetry, and this needs to be added to the capability model.

1. Select **Views** from the menu

   ![The views option](../Images/views.png)

1. Select **Visualizing the device**

   ![Selecting the view type](../Images/SelectViewType.png)

1. Set the view name to `Environment Monitoring`

   ![Setting the view name](../Images/NameView.png)

1. Drag *Temperature* from the *Telemetry* section onto the dashboard. This will add a graph showing the temperature recorded over the past 30 minutes to the dashboard. You can configure this in multiple ways using the control buttons on the top of the panel:

   ![The chart type selection icon](../Images/ChartType.png) Change the visualization to be a number of different chart types, or the last known value

   ![The chart size selection icon](../Images/ChartSize.png) Change the size of the panel on the dashboard

   ![The chart settings selection icon](../Images/ChartSettings.png) Configure the chart including legend, axis labels and the time range

   Configure the chart or last know value to your liking.

1. Repeat this for the other telemetry values. If you want to plot multiple telemetry values on the same chart use the check boxes to select multiple values and drag them together. You can add telemetry values multiple times to get multiple views over the data.

1. You can also customize the view with labels, markdown or images if desired.

1. Select the **Save** button from the top menu

   ![The save view button](../Images/SaveView.png)

When done you will have a view that will look something like this, depending on how you designed it:

![An example dashboard](../Images/View.png)

#### Publish the device template

Before the device template can be assigned to a device, it needs to be published. Once published, any interfaces defined on it cannot be changed, instead a new version of the device template needs to be created.

1. Select the **Publish** button from the top-most menu

   ![The publish button](../Images/PublishButton.png)

1. Select **Publish**

   ![The publish template dialog](../Images/PublishTemplateDialog.png)

## Create a device

Device templates can be assigned to one or more devices - a device being an actual physical device or a software simulator