#!/usr/bin/env python3

import sys
import getopt
import os
import subprocess

def usage():
	print ("\n-:Usage:-")
	print ("python",os.path.realpath(__file__),"[APP_NAME] [PLATFORM] [COUNTRY] [ENVIRONMENT] [TRACK]\n")
	print ("-:Options:-")
	print ("APP_NAME    : TMRW | MTY")
	print ("PLATFORM    : ANDROID | IOS")
	print ("COUNTRY     : SG | MY | TH | ID | VN")
	print ("ENVIRONMENT : ID | ID_1 | ID_2 | ID_3 | IDPT | TH | TH_1 | TH_2 | TH_3 | THPT | SG | VN | MY")
	print ("TRACK       : internal | alpha | beta | production")
	print ("\n")

def is_tool(name):
    from shutil import which
    return which(name) is not None

if len(sys.argv) != 6:
	usage()
	sys.exit()

print ("\nInitialization")
APP_NAME = sys.argv[1]
PLATFORM = sys.argv[2]
COUNTRY = sys.argv[3]
ENVIRONMENT = sys.argv[4]
TRACK = sys.argv[5]
BASEDIR = os.getcwd()

JSON_KEY_PATH = '/Users/'
if APP_NAME == 'MTY':
	if PLATFORM == 'ANDROID':
		def PACKAGE_NAME(i):
			switcher={
				'SG': 'com.uob.mighty.app',
				'TH': 'com.uob.mightyth2',
				'VN': 'com.uob.mightyvn',
				'MY': 'com.uob.mightymy'
			}
			return switcher.get(i,"aa!! Invalid country!")
		APP_FILES_LOCATION = ''
	elif PLATFORM == 'IOS':
		APP_FILES_LOCATION = ''
	else:
		sys.exit ("aa!! Error in Application Name & Platform!")
elif APP_NAME == 'TMRW':
	if PLATFORM == 'ANDROID':
		def PACKAGE_NAME(i):
			switcher={
				'ID': 'com.uob.id.digitalbank',
				'TH': 'com.uob.th.digitalbank'
			}
			return switcher.get(i,"aa!! Invalid country!")
		APP_FILES_LOCATION = ''
	elif PLATFORM == 'IOS':
		APP_FILES_LOCATION = ''
	else:
		sys.exit ("aa!! Error in Application Name & Platform!")

print ("Application Name  =", APP_NAME)
print ("Platform          =", PLATFORM)
print ("Country           =", COUNTRY)
print ("Environment       =", ENVIRONMENT)
print ("Track             =", TRACK)
print ("Base Directory    =", BASEDIR)
print ("App file Location =", APP_FILES_LOCATION)
print ("Json Key path     =", JSON_KEY_PATH)
print ("Package Name      =", PACKAGE_NAME(COUNTRY))
print ("Fastlane status   =",is_tool(fastlane))
print ("\n")





