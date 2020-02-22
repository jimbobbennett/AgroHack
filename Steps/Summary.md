# Summary

In the [previous step](./CheckWeatherWithAzureMaps.md) you called Azure Maps to check the weather forecast before sending the needs watering command. This step gives a summary of the completed solution.

## What you have built

In this workshop, you built an IoT device to capture environment data from sensors, set up an IoT Central app as a dashboard for all the data, sent telemetry to storage, and queried based on average telemetry and weather data to see if the plant needed watering.

### The IoT Device

The IoT Device is a Raspberry Pi running Raspbian Lite. It is connected to a soil sensor, and a temperature, humidity and pressure sensor. It is also connected to a LED to indicate if the plant needs water.

The Raspberry Pi runs a Python app that connects to Azure IoT Central to send telemetry data, and receive a command to turn the LED on and off.

### The Azure IoT Central app

The Azure IoT Central app is the central point for ingesting telemetry data from the Raspberry Pi, and sending commands. The telemetry is shown on a dashboard, showing the current and historical values.

<hr>

This step gave a summary of the completed solution. In the [next step](./CleanUp.md) you will clean up your resources.
