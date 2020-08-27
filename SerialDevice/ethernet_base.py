# -*-coding:utf-8 -*-
import sys, os

sys.path.append(os.path.pardir)
from SerialDevice.device_base import DeviceBase


class EthernetBase(DeviceBase):
    def __init__(self):
        print("This is Ethernet")
        DeviceBase.__init__(
            self,
            b"\x0B\x1C\x01\x00\xFF\xAC\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\xD6\xE3\xCB\x00",
            22,
            115200,
            8,
            1,
        )
        self.serial_com_list = []
        self.serialobject = None
        self.keep = True
        self.flag = False

    def detect_port(self):
        print("Ethernet adress")


if __name__ == "__main__":
    c9 = EthernetBase()
    c9.detect_port()
