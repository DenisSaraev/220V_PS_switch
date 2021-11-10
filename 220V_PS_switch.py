#!/usr/bin/python3.7
'''
This script controls the 220V Power Socket Unit using a relay (normally open, hight level trigger)
'''

import troykahat
import logging
import argparse,sys

#Logger configuration
logger=logging.getLogger()
logger.setLevel(logging.INFO)
formatter=logging.Formatter('%(asctime)s %(name)s %(levelname)s: %(message)s')
#Logger to file
fh=logging.FileHandler('/home/pi/projects/results/logs/220V_PS_switch.log')
fh.setLevel(logging.INFO)
fh.setFormatter(formatter)
logger.addHandler(fh)
#Logger to console
ch=logging.StreamHandler()
ch.setLevel(logging.INFO)
ch.setFormatter(formatter)
logger.addHandler(ch)

#format for --help
class CustomFormatter(argparse.RawDescriptionHelpFormatter, argparse.ArgumentDefaultsHelpFormatter):
    pass

#Parsing in user input positional arguments
parser=argparse.ArgumentParser(description=sys.modules[__name__].__doc__, formatter_class=CustomFormatter)
parser.add_argument(dest='statement', type=int, choices=[0,1], help='0 for disable, 1 for enable 220V PS switch.')

try:
    args=parser.parse_args()
except AttributeError:
    logger.critical(f'Not enought attributes for work. Read --help')
    sys.exit(1)

statement=args.statement
logger.info(f'User input: statement = {statement}')

#PIN with RELE module
PIN_WP_REL = 11
#Enable troykahat digital pins
wp = troykahat.wiringpi_io()
wp.pinMode(PIN_WP_REL, wp.OUTPUT)

#Command to RELE
if statement==0:
    wp.digitalWrite(PIN_WP_REL, False) #set True for enable
    logger.info('RELE DISABLED. PS disactivated')
if statement==1:
    wp.digitalWrite(PIN_WP_REL, True)
    logger.info('RELE ENABLED. PS activated')
