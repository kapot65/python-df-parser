#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Fri Jan 13 13:00:27 2017

@author: chernov
"""

header_types = {
    "DEFAULT": 0x00014000
  }

meta_types = {
    "UNDEFINED_METATYPE": 0x00000000,
    "JSON_METATYPE": 0x00010000,
    "QDATASTREAM_METATYPE": 0x00010007 
  }

binary_types = {
    "UNDEFINED_BINARY": 0x00000000,
    "POINT_DIRECT_BINARY": 0x00000100,
    "POINT_QDATASTREAM_BINARY": 0x00000107,
    "HV_BINARY": 0x00000200,
    "HV_TEXT_BINARY": 0x00000201 
  }

# http://www.rudshel.ru/soft/SDK2/Doc/CPP_USER_RU/html/struct_rsh_channel.html
channel_control = {    
    "NotUsed" : 0x0, 
    "NoSynchro" : 0x0, 
    "Resist1MOhm" : 0x0, 
    "DC": 0x0,
    "ICPPowerOff" : 0x0, 
    "Used" : 0x1, 
    "Synchro" : 0x2, 
    "AC" : 0x4,
    "Resist50Ohm" : 0x8,
    "ICPPowerOn" : 0x10,
    "FirstChannel" : 0x10000
}

# http://www.rudshel.ru/soft/SDK2/Doc/CPP_USER_RU/html/struct_rsh_synchro_channel.html
synchro_channel_control = {
    "FilterOff" : 0x0, 
    "Resist1MOhm" : 0x0, 
    "DC" : 0x0, 
    "FilterLow" : 0x1,
    "FilterHigh" : 0x2, 
    "AC" : 0x4, 
    "Resist50Ohm" : 0x8   
}

# http://www.rudshel.ru/soft/SDK2/Doc/CPP_USER_RU/html/struct_rsh_init_a_d_c.html
synchro_control = {
    "FrequencySwitchOff" : 0x0, 
    "SlopeFront" : 0x0, 
    "SlopeDecline" : 0x2, 
    "FrequencySwitchToMinimum" : 0x4,
    "FrequencySwitchToMaximum" : 0x8 
}