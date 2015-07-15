#!/usr/bin/python

import smbus
import argparse
from subprocess import call
import picamera
import datetime

def options():
	parser = argparse.ArgumentParser(description="Turn on/off Pi Bright LED lights.", formatter_class=argparse.ArgumentDefaultsHelpFormatter)
	parser.add_argument("--on", help="Turn all the lights on", default=False, action="store_true")
	parser.add_argument("--white", help="Turn on the white lights only", default=False, action="store_true")
	parser.add_argument("--ir", help="Turn on the IR lights only", default=False, action="store_true")
	parser.add_argument("--off", help="Turn all the lights off", default=False, action="store_true")
	parser.add_argument("--outdir", help="Output directory path", default='.')
	args = parser.parse_args()
	
	return(args)

def main():
	args = options()

	bus = smbus.SMBus(1)

	DEVICE_ADDRESS = 0x70

	if args.on:
		# All LEDs on
		bus.write_byte_data(DEVICE_ADDRESS, 0x00, 0xff)

		# Turn up the gain
		bus.write_byte_data(DEVICE_ADDRESS, 0x09, 0x0f)

		# Turn up the brightness
		bus.write_byte_data(DEVICE_ADDRESS, 0x02, 0x32)
		bus.write_byte_data(DEVICE_ADDRESS, 0x04, 0x32)
		bus.write_byte_data(DEVICE_ADDRESS, 0x05, 0x32)
		bus.write_byte_data(DEVICE_ADDRESS, 0x07, 0x32)
		
		# Turn up the brightness
		bus.write_byte_data(DEVICE_ADDRESS, 0x01, 0x32)
		bus.write_byte_data(DEVICE_ADDRESS, 0x03, 0x32)
		bus.write_byte_data(DEVICE_ADDRESS, 0x06, 0x32)
		bus.write_byte_data(DEVICE_ADDRESS, 0x08, 0x32)

		# Take a picture
		take_a_picture(args, 'all')

	if args.white:
		# White light LEDs on
		bus.write_byte_data(DEVICE_ADDRESS, 0x00, 0x5a)

		# Turn up the gain
		bus.write_byte_data(DEVICE_ADDRESS, 0x09, 0x0f)

		# Turn up the brightness
		bus.write_byte_data(DEVICE_ADDRESS, 0x02, 0x32)
		bus.write_byte_data(DEVICE_ADDRESS, 0x04, 0x32)
		bus.write_byte_data(DEVICE_ADDRESS, 0x05, 0x32)
		bus.write_byte_data(DEVICE_ADDRESS, 0x07, 0x32)
	
		# Take a picture
		take_a_picture(args, 'white')
	
	if args.ir:
		# All IR LEDs on
		bus.write_byte_data(DEVICE_ADDRESS, 0x00, 0xa5)
		
		# Turn up the gain
		bus.write_byte_data(DEVICE_ADDRESS, 0x09, 0x0f)

		# Turn up the brightness
		bus.write_byte_data(DEVICE_ADDRESS, 0x01, 0x32)
		bus.write_byte_data(DEVICE_ADDRESS, 0x03, 0x32)
		bus.write_byte_data(DEVICE_ADDRESS, 0x06, 0x32)
		bus.write_byte_data(DEVICE_ADDRESS, 0x08, 0x32)
		
		# Take a picture
		take_a_picture(args, 'ir')

	if args.off:
		# All lights off
		bus.write_byte_data(DEVICE_ADDRESS, 0x00, 0x00)

def take_a_picture(args, which_lights):
	# Initialize camera
	camera = picamera.PiCamera()
	
	# Get the current date and time
	dtime = datetime.datetime.now().strftime('%Y-%m-%d_%H:%M:%S')
	
	# Hard code some camera settings, but we could make these setable with a bit more work
	# Camera exposure setting
	camera.exposure_mode = 'verylong'
	# Image vertical flip
	#camera.vflip = True
	# Image horizontal flip
	#camera.hflip = True
	
	# Take a picture with the settings above
	# Name the file with the date, time and light settings (which set of lights was turned on)
	camera.capture(args.outdir + '/' + dtime + '_' + which_lights + '.jpg')

if __name__ == '__main__':
	main()
