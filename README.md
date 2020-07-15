# Mosquito-Breeding-Sites-Prediction-System

We propose a mosquito breeding sites prediction system that leverages IoT technologies, Machine Learning algorithms, and other Information Technology systems, to predict those geographical locations in the area of deployment, that have a high probability to turn into a dangerous mosquito breeding site, owing to a large number of environmental parameters that are most conducive to mosquito breeding. We use a variety of sensors, microcontroller modules, low-cost and low-powered IoT messaging protocols like MQTT, and AWS Cloud services to solve this issue, along with a user-friendly Web Interface providing all the necessary information generated using this system.

# Brief Chronology of System Modeling

1) Generate the contour plot of the region (campus).

2) Find out the end-points (sinks) of the flow vectors.

3) At the sink locations, install a camera, the sensors, and connect them to an ESP8266 chip. This chip connects to a Wifi network and transmits data to a Raspberry Pi. Using the MQTT protocol, the Raspberry Pi publishes all collected data to the MQTT Server. Data is stored in AWS DynamoDB, with triggers programmed for insertion, updation, and deletion.

4) Apply feature extraction (dimensionality reduction) algorithm on images. Then feed the data to a trained classifier that would declare the location, as having water stagnation or not. If yes, then step 5 or else stop.

5) Check environmental parameters for thresholds, ranges, and probabilistic results. AWS Lambda functions are implemented. When appropriate conditions are satisfied, it means mosquito-breeding prone areas. The appropriate notification is sent to the UI, through Amazon API Gateway.

# Technologies Used

The UI is a basic one, with the updated features being a live updation of the summary and reports that are generated in the AWS Backend. 
The major technologies used include:
1) Google Earth and Surfer Software
2) Environmental Sensors (Details in the report)
3) ESP8266 and Raspberry Pi micro-controllers
4) MQTT Protocol
5) Amazon Web Services - AWS IoT Core, AWS lambda, AWS DynamoDB, AWS streams and triggers, Amazon API Gateway
6) Python Scripts
7) Web Application - HTML, CSS - Bootstrap, flex, and grid, JavaScript - jQuery
8) To be inmplemented in future: Histogram of Oriented Gradients (HOG) and Support Vector Machine - Machine Learning
