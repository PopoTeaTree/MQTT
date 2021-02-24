Read Me
--------------------------------------------------------------------------------------------------------------------------------
What is this?
This a simple command-line MQTT (MQ Telemetry Transport) with the above functionality.
Use Python to implement and compile MQTT.
There are 3 roles and files Publisher.py, Broker.py and Subscriber.py.
Publisher publishes data to a given topic to Broker by using command line to type command.
Broker prints out a message received from a Publisher and sends it to all Subscribers
that subscribe topic.
Subscriber subscribes topic to get data from Broker by using command line to type command.
--------------------------------------------------------------------------------------------------------------------------------
How to compile and run program.
1. Open Publisher, Subscriber and Broker files.
 
2. Send data from publisher to broker by typing command below to command
line:
“publish broker_ip_address topic data”
Example publish 202.44.12.85 /room1/light value=on
 
**Note** If Publisher is opened first and send command success, the command line will show waiting message until broker is opened.

3. Subscriber subscribes topic to get data from Broker by typing command below to command line:
“subscribe broker_ip_address topic”
Example subscribe 202.44.12.85 /room1/light

**Note** If Subscriber is opened first and send command success, the command line will show waiting message until broker is opened. If Subscriber subscribes topic that isn’t created, the command line will show nothing until the topic is created.
4. Broker shows data and topic that send and receive.