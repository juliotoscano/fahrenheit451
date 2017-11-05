import time
import Adafruit_ADS1x15
import sys
import time
import paho.mqtt.client as mqtt

mqttc = mqtt.Client("fogo")
mqttc.connect("test.mosquitto.org", 1883)

adc = Adafruit_ADS1x15.ADS1115()
GAIN = 1

adc.start_adc(0, gain=GAIN)
print('Reading ADS1x15 channel 0 for 25 seconds...')
while True:
    # Read the last ADC conversion value and print it out.
    value = adc.get_last_result()
    # WARNING! If you try to read any other ADC channel during this continuous
    # conversion (like by calling read_adc again) it will disable the
    # continuous conversion!
    print('Channel 0: {0}'.format(value))
    # Sleep for half a second.
    mqttc.publish("smoke", value)
    time.sleep(0.5)



