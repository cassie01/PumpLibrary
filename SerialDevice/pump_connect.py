# -*-coding:utf-8 -*-

from SerialDevice.connect_object import *

"""
This class is used to connect with Pump.
Including:
- connect
- connect_close
"""


class PumpConnect():

    # Define here to connect the extra pump in some way.
    def __init__(self, func, connect_way):
        self.connectObj = dic_Pump[func](connect_way)

    # Detect and open the serial port, because the current communication protocol of LVP is undecided, skip it first.
    # At the same time, for COM, IO, and Ethernet, you must define different connections in the future.
    def connect(self):
        # 1.Detect all serial ports.
        self.connectObj.detect_port()
        return self.connectObj

    # Close the serial object.
    def connect_close(self):
        self.connectObj.close()
