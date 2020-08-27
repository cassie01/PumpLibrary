# -*-coding:utf-8 -*-

import serial


class DeviceBase:
    """
    The base class of all serial devices, including the parameter information of the serial port, and some basic serial operation functions.
    """

    def __init__(
            self,
            detectBytes,
            response_length,
            baudRate,
            dataBits,
            stopBits,
            parity=serial.PARITY_NONE,
            portName="",
    ):
        """
        Constructor
        :param detectBytes: Command bytes sent to the device
        :param response_length: Length of bytes the device should respond to, constant
        :param baudRate: The length in bytes that the baud rate device should respond to, constant
        :param dataBits: Data bit
        :param stopBits: Stop bit
        :param parity: Parity
        :param portName: Serial number
        """
        self._portName = portName
        self._baudRate = baudRate
        self._dataBits = dataBits
        self._stopBits = stopBits
        self._parity = parity
        self._detectedPortName = None  # The detected serial port name is stored here.
        self._detectCommandBytes = detectBytes  # Command byte stream used.
        self._responseBytesLength = response_length  # The data length of the pump response. According to the protocol, this length should be fixed.

    def open(self):
        pass

    def close(self):
        pass

    def is_open(self):
        pass
