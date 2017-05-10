#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Mon Dec 26 14:24:42 2016

@author: chernov
"""

import os
import sys

cur_dir = os.path.dirname(os.path.realpath(__file__))
if not cur_dir in sys.path: sys.path.append(cur_dir)
del cur_dir

from envelope_parser import create_message, parse_from_file, parse_message
from envelope_parser import read_machine_header, get_messages_from_stream
from rsh_parser import RshPackage, serialise_to_rsh, parse_from_rsb
from rsh_parser import serialize_to_rsb, dump_to_rsb
from rsb_event_pb2 import Point