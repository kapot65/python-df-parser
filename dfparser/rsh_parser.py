#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Mon Jan 16 14:06:51 2017

Parser for Troitsk Rsh data files

data file description: 
    https://drive.google.com/open?id=0B0Ux_fvsLMdAOXUwSVRKanNORnc

@author: chernov
"""

import os
import sys
import struct
from datetime import datetime

import numpy as np

cur_dir = os.path.dirname(os.path.realpath(__file__))
if not cur_dir in sys.path: sys.path.append(cur_dir)
del cur_dir

from type_codes import channel_control, synchro_channel_control
from type_codes import synchro_control, synchro_channel_types

def serialise_to_rsh(params: dict) -> str:
    """
      Преобразование конфигурационного файла в формате JSON в текстовый хедер 
      .rsh. Хедер можно использовать как конфигурационный файл для lan10-12base
      
      @params -- параметры в формате JSON
      @return -- текстовый хедер
      
    """
    
    out = "// Generated at %s\n\n"%(datetime.now())
    
    def add_val(field, value):
        if type(value) is bytes: value = value.decode()
        val = ''.join('%s, '%(v) for v in value) if type(value) is list else value
        if type(val) is str and val.endswith(', '): val = val[:-2]
        return '%s -- %s\n'%(val, field)  
    
    for param in params:
        if param == "channel":
            for i, channel in enumerate(params[param]):
                for ch_par in channel:
                    val = "%s_%s[%s]"%(param, ch_par, i) 
                    if ch_par == "params":
                        val = "%ss_%s[%s]"%(param, ch_par, i) 
                        
                    out += add_val(val, channel[ch_par])
        elif param == "synchro_channel":
            for sync_ch_par in params[param]:
                if sync_ch_par == "type":
                    out += add_val(param, params[param][sync_ch_par])
                else:
                    out += add_val("%s_%s"%(param, sync_ch_par), 
                                   params[param][sync_ch_par])
        else:
            out += add_val(param, params[param])

    return out 


def parse_from_rsb(header: bytearray) -> dict:
    """
      Парсинг бинарного хедера rsb в JSON
      
      @header -- бинарный хедер (2048 bytes)
      @return -- параметры в формате JSON
      
    """
    
    params = {}
    
    params["text_header_size"] = struct.unpack('I', header[0:4])[0] #check

    params["events_num"] = struct.unpack('i', header[8:12])[0]
    
    start_time = struct.unpack('Q', header[16:24])[0]
    params["start_time"] = datetime.fromtimestamp(start_time).isoformat()
    end_time = struct.unpack('Q', header[24:32])[0]
    params["end_time"] = datetime.fromtimestamp(end_time).isoformat()
    
    params["filepath"] = header[32: 32 + 255].rstrip(b'\0').decode()
    
    params["num_blocks"] = struct.unpack('i', header[288:292])[0] #check
    
    params["aquisition_time"] = struct.unpack('i', header[292:296])[0]
    
    params["blocks_in_file"] = struct.unpack('i', header[296:300])[0]
    
    params["waitTime"] = struct.unpack('i', header[300:304])[0]
    
    params["threshold"] = struct.unpack('d', header[312:320])[0]
    

    sync_params_num = struct.unpack('I', header[336:340])[0]
    sync_params = np.unique(np.frombuffer(header[320:336], np.uint32)
                            [:sync_params_num])
    params["synchro_control"] = []
    for param in sync_params:
        if param == 0:
            params["synchro_control"].append("Default")
        else:
            params["synchro_control"].append(list(synchro_control.keys())\
            [list(synchro_control.values()).index(param)])
    
    
    params["sample_freq"] = struct.unpack('d', header[344:352])[0]
    params["pre_history"] = struct.unpack('I', header[352:356])[0]
    
    params["packet_number"] = struct.unpack('i', header[356:360])[0]
    
    params["b_size"] = struct.unpack('I', header[360:364])[0]
    
    params["hysteresis"] = struct.unpack('I', header[364:368])[0]
    
    params["channel_number"] = struct.unpack('I', header[368:372])[0]
    
    ch_params = []
    
    for i in range(params["channel_number"]):
        ch_data = header[372 + 56*i: 372 + 56*(i+1)]
        ch_param = {}
        
        param_num = struct.unpack('I', ch_data[36:40])[0]
        ch_params_raw = np.unique(np.frombuffer(ch_data[4:36], 
                                                np.uint32)[:param_num])
        ch_param["params"] = []
        for param in ch_params_raw:
            if param == 0:
                ch_param["params"].append("Default")
            else:
                ch_param["params"].append(list(channel_control.keys())\
                [list(channel_control.values()).index(param)])
        
        ch_param["adjustment"] = struct.unpack('d', ch_data[44:52])[0]
        ch_param["gain"] = struct.unpack('I', ch_data[52:56])[0]
        ch_params.append(ch_param)
        
    params["channel"] = ch_params
        
        
    synchro_channel = {}
    sync_ch_par_num = struct.unpack('I', header[632:636])[0]
    sync_ch_params_raw = np.unique(np.frombuffer(header[600:632], 
                                                 np.uint32)[:sync_ch_par_num])
    
    synchro_channel["params"] = []
    for param in sync_ch_params_raw:
        if param == 0:
            synchro_channel["params"].append("Default")
        else:
            synchro_channel["params"]\
            .append(list(synchro_channel_control.keys())\
            [list(synchro_channel_control.values()).index(param)])
       
    synchro_channel_type = struct.unpack('I', header[304:308])[0]
    synchro_channel["type"] = list(synchro_channel_types.keys())\
            [list(synchro_channel_types.values()).index(synchro_channel_type)]
    
    
    synchro_channel["gain"] = struct.unpack('I', header[636:640])[0]
    
    params["synchro_channel"] = synchro_channel
    
    params["err_lang"] = struct.unpack('I', header[640:644])[0]
    params["board_name"] = header[644: 644 + 255].rstrip(b'\0').decode()
    
    params["board_id"] = struct.unpack('I', header[900: 904])[0]
    
    return params


class RshPackage():
    
    def __init__(self, file, fp=None):
        """
          @file -- filename or opened file
        """
        if type(file) == str:
            self.file = open(file, "rb+")
        else:
            self.file = file
        
        self.file.seek(0)
        
        self.text_header = self.file.read(5120).decode("cp1251").rstrip('\0')

        header = self.file.read(2048)
        self.params = parse_from_rsb(header)
        
    def get_event(self, num):
        if num < 0 or num >= self.params["events_num"]:
            raise IndexError("Index out of range [0:%s]"%
                             (self.params["events_num"]))
            
        ch_num = self.params['channel_number']
        ev_size = self.params['b_size']
        
        event = {}
            
        self.file.seek(7168 + num*(96 + 2*ch_num*ev_size))
        
        event["text_hdr"] = self.file.read(64)
        event["ev_num"] = struct.unpack('I', self.file.read(4))[0]
        self.file.read(4)
        
        start_time = struct.unpack('Q', self.file.read(8))[0]
        event["start_time"] = datetime.fromtimestamp(start_time)
        ns_since_epoch = struct.unpack('Q', self.file.read(8))[0]
        if ns_since_epoch:
            event['ns_since_epoch'] = ns_since_epoch
        self.file.read(8)
        
        event_data = self.file.read(2*ev_size*ch_num)
        
        event["data"] = np.fromstring(event_data, np.short)
                    
        return event

    def update_event_data(self, num, data):
        if num < 0 or num >= self.params["events_num"]:
            raise IndexError("Index out of range [0:%s]"%
                             (self.params["events_num"]))
            
        if type(data) != np.ndarray:
            raise TypeError("data should be np.ndarray")
            
        if data.dtype != np.short:
            raise TypeError("data array dtype should be dtype('int16')")
            
        ch_num = self.params['channel_number']
        ev_size = self.params['b_size']
            
        if data.shape != (ch_num*ev_size,):
            raise Exception("data should contain same number of elements "\
                            "(%s)"%(ch_num*ev_size))
        
        self.file.seek(7168 + num*(96 + 2*ch_num*ev_size) + 96)
        self.file.write(data.tostring())
        self.file.flush()
