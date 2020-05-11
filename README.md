# Agrotech Hackathon

This workshop is a hands on lab for building an AgroTech solution using [Azure IoT](https://azure.microsoft.com/overview/iot/?WT.mc_id=agrohack-github-jabenn).

> **Learn more, get certified**
>
> If you want to learn more about Azure IoT Services, then check out the following:
> 
> * [IoT learning paths on Microsoft Learn](https://docs.microsoft.com/learn/browse/?term=IOT&WT.mc_id=agrohack-github-jabenn)
> * [The IoT show on Channel9](https://channel9.msdn.com/Shows/Internet-of-Things-Show/?WT.mc_id=agrohack-github-jabenn)
>
> Once you have upskilled as an IoT developer, why not get certified with our upcoming AZ-220 Azure IoT Developer certification. Check out the details on our [certification page](https://docs.microsoft.com/learn/certifications/azure-iot-developer-specialty?WT.mc_id=agrohack-github-jabenn)

The final project that will be created is an internet connected device with environment sensors, that connects to a set of services that will store the telemetry data and predict the weather using [Azure Maps](https://azure.microsoft.com/services/azure-maps/?WT.mc_id=agrohack-github-jabenn). This weather prediction will be combined with soil moisture data, and used to send a signal back to the device to indicate if the plants need watering, and this will be indicated by an LED, lit if the plant needs watering.

Most of this implementation will use a no-code IoT platform called [Azure IoT Central](https://azure.microsoft.com/services/iot-central/?WT.mc_id=agrohack-github-jabenn), an IoT Software-as-a-service (SaaS) platform. There will be some coding required for the connected device, and this will all be in Python.

## Getting started

### Hardware requirements

Like all good IoT labs, you will need hardware to make this work. You will also need a plant to monitor.

#### The environment sensor

* A [Raspberry Pi](https://www.raspberrypi.org/products/raspberry-pi-4-model-b/) with an SD card and power supply, running Raspbian Lite.

  ![A Raspberry Pi](./Images/pi4.jpg),

* A [Grove base hat](https://www.seeedstudio.io/Grove-Base-Hat-for-Raspberry-Pi-p-3186.html)

  ![A grove base hat](./Images/BaseHat.jpg)

* A [Grove BME280 temperature/pressure/humidity sensor](https://www.seeedstudio.io/Grove-Temp%26Humi%26Barometer-Sensor-%28BME280%29-p-2653.html)

  ![A grove BME 280 sensor](./Images/BME280.jpg)

* A [Grove capacitive moisture sensor](http://wiki.seeedstudio.com/Grove-Capacitive_Moisture_Sensor-Corrosion-Resistant/)

  ![A Grove capacitive moisture sensor](./Images/moisture.jpg)

* A [Grove LED socket kit with an LED](http://wiki.seeedstudio.com/Grove-LED_Socket_Kit/)

  ![A grove led socket kit](./Images/Grove-White-LED-p-2016.jpeg)

* [Grove cables](https://www.seeedstudio.com/Grove-Universal-4-Pin-20cm-Unbuckled-Cable-5-PCs-Pack-p-749.html) to connect the components

  ![Grove cables](./Images/Cables.jpg)

### Software

You will need to install some software to be able to program the Raspberry Pi and create the various parts of this app

* [Visual Studio Code](https://code.visualstudio.com/Download/?WT.mc_id=agrohack-github-jabenn)

* [Azure Functions Core Tools](https://docs.microsoft.com/azure/azure-functions/functions-run-local?WT.mc_id=agrohack-github-jabenn)
* Python

  * **Windows:**

    You can install Python from the [Windows Store](https://www.microsoft.com/p/python-38/9mssztt1n39l?activetab=pivot:overviewtab&WT.mc_id=agrohack-github-jabenn). This configures Python correctly on your PATH, and there are no further steps.

    If you don't want to use the store, you can install from the [Python Downloads page](https://www.python.org/downloads/). If you do this, ensure you check the *Add Python to PATH* option.

    ![The python installer dialog highlighting the Add Python 3.8 to PATH option](./Images/PythonInstaller.png)

  * **macOS**
  
    You can install Python from the [Python Downloads page](https://www.python.org/downloads/).

    When Python is installed it will open a Finder window. Run the following scripts from inside that Finder window to set up certificates and add Python to your PATH:

    1. `Update Shell Profile.command`

    1. `Install Certificates.command`

### Azure subscription

To use Azure services you will need an Azure subscription. If you don't have a subscription you can sign up for free.

* If you are a student aged 18 and up and have an email address from an academic institution, you can sign up for the free Azure for Students offer at [azure.microsoft.com/free/students](https://azure.microsoft.com/free/students/?WT.mc_id=agrohack-github-jabenn) without a credit card. At the time of writing this gives you $100 of credit to use over 12 months, as well as free tiers of a number of services for that 2 months. At the end of the 12 months, if you are still a student you can renew and get another $100 in credit and 12 months of free services.

* If you are not a student, you can sign up at [azure.microsoft.com/free](https://azure.microsoft.com/free/?WT.mc_id=agrohack-github-jabenn). You will need a credit card for verification purposes only, you will not be billed unless you decide to upgrade your account to a paid offering. At the time of writing the free account will give you US$200 of free credit to spend on what you like in the first 30 days, 12 months of free services, plus a load of services that have tiers that are always free.

## The workshop

### Steps

1. [Set up the environment monitor](./Steps/SetUpTheEnvironmentMonitor.md)

1. [Create the application in Azure IoT Central](./Steps/CreateTheAppInIoTCentral.md)

1. [Write the code to capture telemetry from the Raspberry Pi](./Steps/WriteThePiCode.md)

1. [Export IoT telemetry to Azure Event Hubs](./Steps/ExportDataToEventHubs.md)

1. [Create a storage account to store telemetry data](./Steps/CreateBlobStorage.md)

1. [Use Azure Stream Analytics to stream data into the storage account](./Steps/ExportDataToBlobStorage.md)

1. [Create an Azure Function triggered by Azure Stream Analytics to check soil moisture](./Steps/CreateFunction.md)

1. [Trigger an Azure IoT Central command if the soil moisture is too low](./Steps/ExecuteIoTCommand.md)

1. [Call Azure Maps to check the weather forecast before sending the needs watering command](./Steps/CheckWeatherWithAzureMaps.md)

1. [Summary](./Steps/Summary.md)

1. [Clean up](./Steps/CleanUp.md)
