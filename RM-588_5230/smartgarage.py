# project : SmartGarage
# device : NOKIA 5230, RM-588
# os : Symbian 9.4, S60 v5
# operator : Free in France
# author : caesarhao
# email : caesarhao@gmail.com
# version history : 
# 0.1 : the project is started, 2020.03.24


# import block
import e32				# symbian os related services
import sysinfo			# system information
import appuifw			# user interface and graphics
import telephone		# telephone services
import messaging		# sms and mms
import camera			# take photo and record video
from sensor	import *	# sensors
import btsocket			# bluetooth service
# ------------

# global parameters
G_TestMode = True
G_destNum = '+33698009759'
# ------------

# global functions
def setup():
	"set up the system, scheduled once at the beginning"
	pass

def loop():
	"working routine"
	pass

def monitor():
	"monitor the system and react if necessary, scheduled every 10 seconds"
	pass

def test_setup():
	"system initialization during the development"
	print "OS version is : ", sysinfo.os_version(), "%"
	print "IMEI is : ", sysinfo.imei(), "%"
	print "battery level is : ", sysinfo.battery(), "%"
	#print "Device has ", camera.cameras_available(), " cameras"
	# Device has 1 camera
	#print "Camera Image Modes: ", camera.image_modes(), ""
	# Camera Image modes : ['RGB12', 'RGB', 'JPEG_Exif', 'RGB16']
	#print "Camera Image Sizes: ", camera.image_sizes(), ""
	# Camera Image Sizes: [(1024, 768), (640, 480)]
	#print "Camera Flash modes: ", camera.flash_modes(), ""
	# Camera Flash modes: ['none']
	#print "Camera Max zoom: ", camera.max_zoom(), ""
	# Camera Max zoom: 60
	#print "Camera Exposure modes: ", camera.exposure_modes(), ""
	#Camera Exposure modes: ['auto', 'center', 'backlight', 'night']
	
	pass

def test_loop():
	"test routine during the development"
	pass

# local functions
def IsCarInGarage():
	"detect if the car is in the garage now"
	# TODO:
	return True

def IsDoorOpen():
	"detect if the door is open now"
	# TODO:
	return False

def IsCarNear():
	"detect if the car is nearby"
	# TODO: scan the bluetooth of the car?
	return True

# work flow
if __name__ == '__main__' :
	if G_TestMode :
		test_setup()
		test_loop()
	else:
		setup()
		loop()

# ------------

