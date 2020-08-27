# -*- coding:utf-8 -*-

# *****************************
# COPYRIGHT 2019 Smiths Medical.
# Created Date: 2019-11
# Author: Li.Wang
# Description: This library is used for test automation on pump, including C9 Syringe and C9 LVP pump.
# *****************************

from Keywords import *
from SerialDevice.pump_connect import *
from ParserProtocol.protocol_invoker import *


class PumpLibrary(
    Info,
    Infusion,
    InfusionParameter,
    DeviceReport,
    HistoryLog,
    InfusionSetting,
    Maintenance,
    SafetySetting,
    SystemSetting,
    Alarm,
    Bolus,
    Priming,
    Motor,
):
    """
    Use double inheritance to load methods from all keywords here
    """

    def __init__(self):
        for base in PumpLibrary.__bases__:
            base.__init__(self)
        self.port = None
        # self.connectObj = None
        # self.parser_invoker = None
        self.sequence_id = 0
        self.product_id = PRODUCT_ID
        self.connectObj = PumpConnect("C9LVP", "COM").connect()
        self.parser_invoker = ProtocolParserInvoker(lvp_project_dll_path)

    @classmethod
    def main(cls):
        lvp = PumpLibrary()
        return lvp
