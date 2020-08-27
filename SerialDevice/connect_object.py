# -*-coding:utf-8 -*-

from SerialDevice import *
from enum import Enum, unique


# 重定义C9的通讯
class C9(COMBase):
    def __init__(self, connect_way):
        self.connect_way = connect_way
        COMBase.__init__(
            self,
            b"\x0B\x1C\x01\x00\xFF\xAC\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\xD6\xE3\xCB\x00",
        )


# 重定义C9LVP的通讯
class C9LVP(COMBase, IOBase, EthernetBase):
    def __init__(self, connect_way):
        self.connect_way = connect_way
        self.serial_com_list = []
        if self.connect_way == "COM":
            super(
                C9LVP,
                COMBase.__init__(
                    self,
                    b"\x0B\x1C\x01\x00\xFF\xAC\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\xD6\xE3\xCB\x00",
                    # b'\x0B\x1C\x01\x00\xFF\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\xCF\x34\x65\x89',
                ),
            )
        elif self.connect_way == "IO":
            super(C9LVP, IOBase.__init__(self))
        elif self.connect_way == "Ethernet":
            super(C9LVP, EthernetBase.__init__(self))

    def detect_port(self):
        try:
            dic_Connect[self.connect_way]["detect_port"](self)
        except Exception as reason:
            print("Error : %s" % reason)


@unique
class ConnectObject(Enum):
    COM = "COM"
    IO = "IO"
    Ethernet = "Ethernet"
    C9LVP = "C9LVP"
    C9 = "C9"


# 对应连接对象及功能
dic_COM = {"detect_port": COMBase.detect_port}

dic_IO = {"detect_port": IOBase.detect_port}

dic_Ethernet = {"detect_port": EthernetBase.detect_port}

dic_Connect = {
    ConnectObject.COM.value: dic_COM,
    ConnectObject.IO.value: dic_IO,
    ConnectObject.Ethernet.value: dic_Ethernet,
}

dic_Pump = {ConnectObject.C9.value: C9, ConnectObject.C9LVP.value: C9LVP}
