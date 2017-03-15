# Python test of all the functionality needed for the pi day event

import time
import RPi.GPIO as GPIO
from tsl2561 import TSL2561

GPIO.setmode(GPIO.BCM)
GPIO.setwarnings(False)

count = 0
bouncetime = int(round(time.time()*1000))
pin_LED = 17
pin_button = 4

pin_top_bar = 22
pin_upper_left_vertical = 27
pin_upper_right_vertical = 16
pin_left_mid_bar = 21
pin_right_mid_bar = 12
pin_lower_left_vertical = 26
pin_lower_right_vertical = 13
pin_bottom_bar = 19

GPIO.setup(pin_top_bar, GPIO.OUT, initial=GPIO.LOW)
GPIO.setup(pin_upper_left_vertical, GPIO.OUT, initial=GPIO.LOW)
GPIO.setup(pin_upper_right_vertical, GPIO.OUT, initial=GPIO.LOW)
GPIO.setup(pin_left_mid_bar, GPIO.OUT, initial=GPIO.LOW)
GPIO.setup(pin_right_mid_bar, GPIO.OUT, initial=GPIO.LOW)
GPIO.setup(pin_lower_left_vertical, GPIO.OUT, initial=GPIO.LOW)
GPIO.setup(pin_lower_right_vertical, GPIO.OUT, initial=GPIO.LOW)
GPIO.setup(pin_bottom_bar, GPIO.OUT, initial=GPIO.LOW)
GPIO.setup(pin_LED, GPIO.OUT, initial=GPIO.LOW)
GPIO.setup(pin_button, GPIO.IN, pull_up_down=GPIO.PUD_UP)

def button_interupt(channel):
	global count
	global bouncetime
	nbt = int(round(time.time()*1000))
	if nbt - bouncetime > 200:
		i = dict[count % 10]
		GPIO.output(i, GPIO.LOW)
		count = count+1
		i = dict[count % 10]
		GPIO.output(i,GPIO.HIGH)
	bouncetime = nbt
 
GPIO.add_event_detect(pin_button,GPIO.RISING,callback=button_interupt)

print("don't Blink")
blink_val = False
print("map of your head")
hex_0 = [pin_top_bar,pin_upper_left_vertical,pin_upper_right_vertical,pin_lower_right_vertical,pin_lower_left_vertical,pin_bottom_bar]
hex_1 = [pin_upper_right_vertical,pin_lower_right_vertical]
hex_2 = [pin_top_bar, pin_upper_right_vertical,pin_left_mid_bar,pin_right_mid_bar,pin_lower_left_vertical,pin_bottom_bar]
hex_3 = [pin_top_bar,pin_upper_right_vertical,pin_lower_right_vertical,pin_left_mid_bar,pin_right_mid_bar,pin_bottom_bar]
hex_4 = [pin_upper_left_vertical,pin_right_mid_bar,pin_left_mid_bar,pin_upper_right_vertical,pin_lower_right_vertical]
hex_5 = [pin_top_bar,pin_upper_left_vertical,pin_left_mid_bar,pin_right_mid_bar,pin_lower_right_vertical,pin_bottom_bar]
hex_6 = [pin_upper_left_vertical,pin_lower_left_vertical,pin_bottom_bar,pin_lower_right_vertical,pin_left_mid_bar,pin_right_mid_bar]
hex_7 = [pin_top_bar,pin_upper_right_vertical,pin_lower_right_vertical]
hex_8 = [pin_top_bar,pin_upper_left_vertical,pin_upper_right_vertical,pin_lower_right_vertical,pin_lower_left_vertical,pin_bottom_bar,pin_left_mid_bar,pin_right_mid_bar]
hex_9 = [pin_top_bar,pin_upper_left_vertical,pin_upper_right_vertical,pin_lower_right_vertical,pin_left_mid_bar,pin_right_mid_bar]
print("take a look, its in a book")
dict = {0: hex_0, 1: hex_1, 2: hex_2, 3: hex_3, 4: hex_4, 5: hex_5, 6: hex_6, 7: hex_7, 8: hex_8, 9: hex_9}
i = dict[0]
GPIO.output(i,GPIO.HIGH)
while count < 20:
	blink_val = not blink_val
	if blink_val: 
		GPIO.output(pin_LED, GPIO.HIGH)
	else:
		GPIO.output(pin_LED, GPIO.LOW)
	tsl = TSL2561(debug=1)
	print "Light level:", tsl.lux(), "lux"
	time.sleep(1)

GPIO.cleanup()

