# coding= utf-8

import ctypes
import datetime
from enum import Enum, unique
# from global_attributes import PRODUCT_ID


@unique
class CommandID(Enum):
    """
    Reference c9 communication protocol
    """

    # Normal user authority

    EGetProductID = 0x0000  # 应用:C
    EInvalidCommand = 0x0001  # 应用:
    ESendFileStart = 0x0002  # 应用:GUA
    ESendFilePackage = 0x0003  # 应用:GUA
    ESendFileCompleted = 0x0004  # 应用:GUA
    EGetFirmwareVersion = 0x0005  # 应用:GUA/GPA/ FCT
    EGetCurrentMode = 0x0006  # 应用:GUA/GPA
    EResetPumpMode = 0x0007  # 应用:GUA
    EGetSerialNumber = 0x0008  # 应用:GPA/GBA
    EGetSupportedMaxFileSize = 0x0009  # 应用:GUA

    EGetPumpAlarm = 0x0100  # 应用:GPA/GBA, LVP
    EGetKVO = 0x0101  # 应用:GPA, LVPGPA
    EGetDateTime = 0x0102  # 应用:GPA, LVPGPA
    EGetOcclusionLevel = 0x0103  # 应用:GPA, LVPGPA
    EGetMaintenanceDateTime = 0x0104  # 应用:GPA, LVPGPA
    EGetMaintenancePeriod = 0x0105  # 应用:GPA, LVPGPA
    EGetAlarmVolume = 0x0106  # 应用:GPA, LVPGPA
    EGetBrightness = 0x0107  # 应用:GPA, LVPGPA
    EGetNightModePeriod = 0x0108  # 应用:GPA, LVPGPA
    EGetPumpLanguage = 0x0109  # 应用:GPA, LVPGPA
    EGetLogTotalNum = 0x010A  # 应用:GPA, LVPGPA
    EGetLogItem = 0x010B  # 应用:GPA, LVPGPA
    EGetPowerStatus = 0x010C  # 应用:GPA/GBA, LVPGPA
    EGetSensorStatus = 0x010D  # 应用:GPA, LVPGPA
    EGetInfusionMode = 0x010E  # 应用:GPA, LVPGPA
    EGetBrand = 0x010F  # 应用:GPA, LVPGPA

    EGetDoseUnit = 0x0110  # 应用:GPA, LVPGPA
    EGetCurrentDrug = 0x0111  # 应用:GPA, LVP
    EGetInfusionParameter = 0x0112  # 应用:GPA, LVPGPA
    EGetBatteryAlarmDuration = 0x0113  # 应用:GPA
    EGetLockPassword = 0x0116  # 应用:GPA
    EGetSecuritySwitch = 0x0117  # 应用:GPA, LVPGPA
    EGetCompleteInfusionAlarmTime = 0x0118  # 应用:GPA
    EGetAlarmSoundType = 0x0119  # 应用:GPA, LVPGPA
    EGetCustomBrandCaliPara = 0x011A  # 应用:GPA
    EGetPreselectonBrand = 0x011B  # 应用:GPA
    EGetCaliCustomBrand = 0x011C  # 应用:GPA
    EGetAlarmTypePassword = 0x011D  # 应用:GPA, LVP
    EGetInfusingParasOfMode = 0x011E  # 应用:GPA,LVP
    EGetSystemStatus = 0x011F  # 应用:INFUSYS,LVP

    EGetBrandCount = 0x0120  # 应用:GPA，LVPGPA
    EGetAlarmCount = 0x0122  # 应用:GPA，LVPGPA
    EGetAlarmName = 0x0123  # 应用:GPA，LVPGPA
    EGetTubePrecisionCalibrationStatus = 0x0124  # 应用:LVPGPA
    EGetRegionCount = 0x0125  # 应用:LVPGPA
    EGetRegionName = 0x0126  # 应用:LVPGPA
    EGetLanguageName = 0x0127  # 应用:LVPGPA
    EGetNightModeAlarmVolume = 0x0128  # 应用:LVPGPA
    EGetNightModeBrightness = 0x0129  # 应用:LVPGPA
    EGetSecondaryInfusionCompleteSetting = 0x012A  # 应用:LVPGPA
    EGetTubeSize = 0x012B  # 应用:LVPGPA
    EGetDrugMassUnit = 0x012C  # 应用:LVPGPA
    EGetInfusionNearCompleteCriteria = 0x012D  # 应用:LVPGPA
    EGetAirDetectionOption = 0x012E  # 应用:LVPGPA
    EGetBubbleSensitivity = 0x012F  # 应用:LVPGPA

    EVerifyPasscode = 0x0130  # 应用:LVPGPA
    EGetBasicModeRateUnit = 0x0131  # 应用:LVPGPA

    # Infosys has occupied 0x1000~0x1005

    ESetOcclusionLevel = 0x2000  # 应用:GPA, LVPGPA
    ESetInfusionMode = 0x2001  # 应用:GPA/GBA, LVPGPA
    ESetDateTime = 0x2002  # 应用:GPA, LVPGPA
    ESetAlarmVolume = 0x2003  # 应用:GPA, LVPGPA
    ESetBrightness = 0x2004  # 应用:GPA, LVPGPA
    ESetNightModePeriod = 0x2005  # 应用:GPA, LVPGPA
    ESetBrand = 0x2006  # 应用:GPA, LVPGPA
    ESetDoseUnit = 0x2007  # 应用:GPA, LVPGPA
    ESetKVO = 0x2008  # 应用:GPA, LVPGPA
    ESetCurrentDrug = 0x2009  # 应用:GPA, LVPGPA
    ESetInfusionParameter = 0x200A  # 应用:GPA/GBA, LVPGPA
    ESetLockPassword = 0x200B  # 应用:GPA
    ESetSecuritySwitch = 0x200C  # 应用:GPA, LVPGPA
    ESetCompleteInfusionAlarmTime = 0x200D  # 应用:GPA
    ESetAlarmSoundType = 0x200E  # 应用:GPA, LVPGPA
    ESetCustomBrandCaliPara = 0x200F  # 应用:GPA

    EClearAllCustomBrandCaliPara = 0x2010  # 应用:GPA
    ESetPreselectonBrand = 0x2011  # 应用:GPA
    ESetAlarmTypePassword = 0x2012  # 应用:GPA
    EClearCustomBrandCaliPara = 0x2013  # 应用:GPA
    ESetInfusingParameterOfMode = 0x2014  # 应用:TAA
    ESetTubePrecisionCalibrationBrand = 0x2015  # 应用:LVPGPA
    EStartTubePrecisionCalibrationPriming = 0x2016  # 应用:LVPGPA
    EStopTubePrecisionCalibrationPriming = 0x2017  # 应用:LVPGPA
    ESetTubePrecisionCalibrationParameter = 0x2018  # 应用:LVPGPA
    ESetTubePrecisionCalibrationInfusionValue = 0x2019  # 应用:LVPGPA
    EStopTubePrecisionCalibration = 0x201A  # 应用:LVPGPA
    ESetNightModeAlarmVolume = 0x201B  # 应用:LVPGPA
    ESetNightModeBrightness = 0x201C  # 应用:LVPGPA
    ESetSecondaryInfusionCompleteSetting = 0x201D  # 应用:LVPGPA
    ESetTubeSize = 0x201E  # 应用:LVPGPA
    ESetDrugMassUnit = 0x201F  # 应用:LVPGPA

    ESetInfusionNearCompleteCriteria = 0x2020  # 应用:LVPGPA
    ESetAirDetectionOption = 0x2021  # 应用:LVPGPA
    ESetBubbleSensitivity = 0x2022  # 应用:LVPGPA
    EModifyPasscode = 0x2023  # 应用:LVPGPA
    ESetBasicModeRateUnit = 0x2024  # 应用:LVPGPA

    # Maintenance authority has occupied 0x3000~0x3FFF

    ESetMaintenancePeriod = 0x3000  # 应用:GPA, LVP
    ESetMaintenanceDateTime = 0x3001  # 应用:GPA(FQC) , LVP

    # Factory has occupied 0x4000~0x4FFF

    EGetPressureSensorValue = 0x4000  # 应用:GPA
    EGetPressurePValue = 0x4001  # 应用:GPA
    EGetPressureFactor_ABC = 0x4002  # 应用:GPA
    EGetSizeSensorCalibrationFactor_KP = 0x4003  # 应用:GPA
    EGetSizeSensorValue = 0x4004  # 应用:GPA
    EGetBatteryVoltage = 0x4005  # 应用:GPA/GBA
    EGetUIUserDefineSyringeBrandName = 0x4006  # 应用:GPA
    EGetFactoryFirmwareVersion = 0x4007  # 应用:GPA, LVP
    EGetTubePrecisionCalibrationFactor = 0x4008  # 应用:LVP
    EGetBrandPressureCalibrationFactorKB = 0x4009  # 应用:LVP
    EGetEachPressureSensorValue = 0x400A  # 应用:LVP
    EGetBrandEachPressurePValue = 0x400B  # 应用:LVP
    EGetDripSensorSpeed = 0x400C  # 应用:LVPGPA
    EGetBrandOcclusionLevelThreshold = 0x400D  # 应用:LVP

    ESetPumpLanguage = 0x5000  # 应用:GPA, LVPGPA
    EClearHistoryLog = 0x5001  # 应用:GPA ,LVP
    ESetSerialNumber = 0x5002  # 应用:GPA ,LVP
    ESetUIUserDefineSyringeBrandName = 0x5003  # 应用:GPA, LVP
    ERestoreFactorySetting = 0x5004  # 应用:GPA ,LVP
    ESetTubePrecisionCalibrationFactor = 0x5005  # 应用:LVPGPA
    ESetBrandPressureCalibrationFactorKB = 0x5006  # 应用:LVPGPA
    ESetBrandOcclusionLevelThreshold = 0x5007  # 应用:LVP
    ERestoreFactorySetting_FactoryMode = 0x5008  # 应用:LVP （Factory Mode）

    # Drug library has occupied 0x6000~0x6FFF

    EGetDrugItem = 0x6000  # 应用:GPA
    EUpdateDrugItem = 0x6001  # 应用:GPA
    EGetCategoryItem = 0x6002  # 应用:GPA
    EUpdateCategoryItem = 0x6003  # 应用:GPA
    EGetDrugLibCount = 0x6004  # 应用:GPA
    EGetCategoryCount = 0x6005  # 应用:GPA
    EClearDrugLib = 0x6006  # 应用:GPA
    EGetLanguageCount = 0x6007  # 应用:GPA
    EUpdateCategoryDrugIndex = 0x6008  # 应用:GPA
    EGetCategoryDrugIndex = 0x6009  # 应用:GPA
    EENABLEDRUGLIBFEATURES = 0x600A  # 应用:GPA
    EGetREGIONLANGUAGELIST = 0x600B  # 应用:LVP
    EGetREGIONCATEGORYCOUNT = 0x600C  # 应用:LVP
    EGetREGIONCATEGORYITEM = 0x600D  # 应用:LVP
    ESTARTUPDATEREGIONCATEGORYDRUGINDEX = 0x600E  # 应用:LVP
    EUPDATEREGIONCATEGORYDRUGINDEX = 0x600F  # 应用:LVP

    EGetREGIONCATEGORYDRUGINDEX = 0x6010  # 应用:LVP
    ESTARTIMPORTDRUGLIB = 0x6011  # 应用:LVP
    EENDIMPORTDRUGLIB = 0x6012  # 应用:LVP
    EGetDRUGITEMWITHTYPE = 0x6013  # 应用:LVP
    EUPDATEDRUGITEMWITHTYPE = 0x6014  # 应用:LVP
    ESTARTGetREGIONCATEGORYDRUGINDEX = 0x6015  # 应用:LVP

    # Development has occupied 0x7000~0x7FFF

    EGetOcculsionPressureThreshold = 0x7000  # 应用:GPA
    EGetSyringeData = 0x7001  # 应用:GPA
    EGetInputsAtMain = 0x7002  # 应用:GPA
    EGetBatteryThreshold = 0x7003  # 应用:GPA
    EGetFlashAddressData = 0x7004  # 应用:GPA
    EGetFCTFlag = 0x7005  # 应用:GPA
    EGetADCRedress = 0x7006  # 应用:GPA, LVP
    EGetSyringePressureSelfCaliValue = 0x7007  # 应用:GPA
    EGetSyringeCaliFlag = 0x7008  # 应用:GPA
    EGetAppImgValidFlag = 0x7009  # 应用:GPA
    EGetUIDeliverySecureConfig = 0x700A  # 应用:GPA
    EGetSyringeSizeCaliRange = 0x700B  # 应用:GPA
    EETLOG = 0x700C  # 应用:GPA (未保护的历史纪录)
    EEXPORTFILEFROMPUMPSTART = 0x700D  # 应用:GPA
    EEXPORTFILEFROMPUMPPACKAGE = 0x700E  # 应用:GPA
    EEXPORTFILEFROMPUMPRESULT = 0x700F  # 应用:GPA

    EEXPORTPRESSURECALIBRATIONDATA = 0x7010  # 应用:LVP
    EGetTUBEUNINSTALLTHRESHOLD = 0x7011  # 应用:LVP
    EGetOCCLUSIONROLLBACKVOLUME = 0x7012  # 应用:LVP

    EResetSPIFlashData = 0x8000  # 应用:GPA ,LVP
    ESetOcculsionPressureThreshold = 0x8001  # 应用:GPA
    ESetSyringeData = 0x8002  # 应用:GPA
    ESetBatteryThreshold = 0x8003  # 应用:GPA
    ESetFlashAddressData = 0x8004  # 应用:GPA
    EWriteLog = 0x8005  # 应用:GPA
    ESetFCTFlag = 0x8006  # 应用:GPA
    ESetADCRedress = 0x8007  # 应用:GPA ,LVP
    ESetPressurePValue = 0x8008  # 应用:GPA
    ESetSyringePressureSelfCaliValue = 0x8009  # 应用:GPA
    ESetSyringeCaliFlag = 0x800A  # 应用:GPA
    ESetAppImgValidFlag = 0x800B  # 应用:GPA
    ESetUIDeliverySecureConfig = 0x800C  # 应用:GPA
    ESetPressureFactor_ABC = 0x800D  # 应用:GPA
    ESetSizeSensorCalibrationFactor_KP = 0x800E  # 应用:GPA
    ESetSyringeSizeCaliRange = 0x800F  # 应用:GPA

    ERemoteStartStopInfusion = 0x8010  # 应用:Remote
    EIMPORTFILETOPUMPSTART = 0x8011  # 应用:GPA
    EIMPORTFILETOPUMPPACKAGE = 0x8012  # 应用:GPA
    EIMPORTFILETOPUMPRESULT = 0x8013  # 应用:GPA
    ESetTOTALVOLUME = 0x8014  # 应用:GPA, LVP
    ESetBRANDEACHPRESSUREPVALUE = 0x8015  # 应用:LVP
    ESetTUBEUNINSTALLTHRESHOLD = 0x8016  # 应用:LVP
    ESetOCCLUSIONROLLBACKVOLUME = 0x8017  # 应用:LVP
    ERemoteStartPrime = 0x8018  # 应用:LVP_TAA
    ERemoteStartBolus = 0x8019  # 应用:LVP_TAA
    ERemoteSetBolusParameter = 0x801A  # 应用:LVP_TAA

    # TAA has occupied 0x9000~0x9FFF
    ERollbackVolume = 0x9000  # 应用:TAA
    EGetScreenValue = 0x9001  # 应用:TAA
    EGetTitleHint = 0x9002  # 应用:TAA
    EForwardVolume = 0x9003  # 应用:TAA
    EStopMotor = 0x9004  # 应用:TAA
    EGetRightAreaScreenValue = 0x9005  # 应用:TAA
    EGetCursorPosinScreen = 0x9006  # 应用:TAA

    # FCT has occupied 0xA000~0xA00F

    EIsFCTMode = 0xA000  # 应用:FCT
    EGetTestCaseCount = 0xA001  # 应用:FCT
    EGetTestCaseItem = 0xA002  # 应用:FCT
    EGetTestCaseHint = 0xA003  # 应用:FCT
    ETriggerTestCaseItem = 0xA004  # 应用:FCT

    @classmethod
    def convert_int_to_command_id(cls, value):
        for name, member in CommandID.__members__.items():
            if member.value == value:
                print(member)
                return member
            else:
                continue
        return None

    @classmethod
    def convert_command_id_to_int(cls, value):
        for name, member in CommandID.__members__.items():
            if member == value:
                return member.value
            else:
                continue
        return None


# Define various command structures, transfer them to ProtocolParser_x64.dll and get the return value.

class BaseCommand(ctypes.Structure):
    _fields_ = [("sequence_id", ctypes.c_byte),
                ("direction", ctypes.c_byte),
                ("product_id", ctypes.c_byte),
                ("command_id", ctypes.c_ushort),
                ("timestamp", ctypes.c_byte * 9)
                ]

    command_send_time = datetime.datetime.now().timestamp()

    # command_send_time = time.time()

    def __init__(self):
        self.timeout_count = 0

    def set_timeout_count(self, count):
        """
        Set timeout count
        :param count: count of request command timeout
        :return:
        """
        # The timeout count is less than 3
        if self.timeout_count >= 3:
            return
        else:
            self.timeout_count = self.timeout_count + count

    @property
    def get_timeout_count(self):
        return self.timeout_count

    def copy(self, cmd):
        pass


class GetGeneralInfoForTAA(BaseCommand):
    """
    GetGeneralInfoForTAA
    """
    _fields_ = [("command_string_id", ctypes.c_byte), ("return_id", ctypes.c_ushort)]

    def copy(self, cmd):
        self.return_id = cmd.return_id


class GetVTBI(BaseCommand):
    """
    GetVTBI
    """
    _fields_ = [("unit", ctypes.c_byte), ("VTBI", ctypes.c_float)]

    def copy(self, cmd):
        self.unit = cmd.unit
        self.rate = cmd.VTBI


class GetTotal(BaseCommand):
    """
    GetTotal
    """
    _fields_ = [("unit", ctypes.c_byte), ("total_volume", ctypes.c_float)]

    def copy(self, cmd):
        self.unit = cmd.unit
        self.total_volume = cmd.total_volume


class GetDateTime(BaseCommand):
    """
    GetDateTime
    """
    _fields_ = [("year", ctypes.c_ushort),
                ("month", ctypes.c_byte),
                ("day", ctypes.c_byte),
                ("hour", ctypes.c_byte),
                ("minute", ctypes.c_byte),
                ("second", ctypes.c_byte)
                ]

    def copy(self, cmd):
        self.year = cmd.year
        self.month = cmd.month
        self.day = cmd.day
        self.hour = cmd.hour
        self.minute = cmd.minute
        self.second = cmd.second


class GetDrugSolutionWeightMode(BaseCommand):
    """
    GetDrugSolutionWeightMode
    """
    _fields_ = [("drugSolution", ctypes.c_float), ("drugSolutionUnit", ctypes.c_byte)]

    def copy(self, cmd):
        self.drugSolution = cmd.drugSolution
        self.drugSolutionUnit = cmd.drugSolutionUnit


class GetVolumeWeightMode(BaseCommand):
    """
    GetVolumeWeightMode
    """
    _fields_ = [("drugVolume", ctypes.c_float), ("volUnit", ctypes.c_byte)]

    def copy(self, cmd):
        self.drugVolume = cmd.drugVolume
        self.volUnit = cmd.volUnit


class GetSerialNumber(BaseCommand):
    """
    GetSerialNumber
    """
    _fields_ = [("serial_num_length", ctypes.c_byte), ("serial_number_buffer", ctypes.c_byte * 256)]

    def copy(self, cmd):
        self.serial_num_length = cmd.serial_num_length
        # print("GetSerialNumber serial_num_length=", cmd.serial_num_length)
        self.serial_number_buffer = cmd.serial_number_buffer


class RollbackVolume(BaseCommand):
    """
    RollbackVolume
    """
    _fields_ = [("volume", ctypes.c_uint32)]

    def __init__(self):
        BaseCommand.__init__(self)
        self.command_id = CommandID.convert_command_id_to_int(CommandID.ERollbackVolume)
        self.sequence_id = 0
        self.direction = 0
        self.product_id = PRODUCT_ID

    def fill_parameter(self, volume=51):
        self.volume = volume * 1000

    def copy(self, cmd):
        pass


class ForwardVolume(BaseCommand):
    """
    ForwardVolume
    """
    _fields_ = [("volume", ctypes.c_uint32)]

    def __init__(self):
        BaseCommand.__init__(self)
        self.command_id = CommandID.convert_command_id_to_int(CommandID.EForwardVolume)
        self.sequence_id = 0
        self.direction = 0
        self.product_id = PRODUCT_ID

    def fill_parameter(self, volume=1):
        self.volume = volume * 1000

    def copy(self, cmd):
        pass


class StopMotor(BaseCommand):
    """
    StopMotor
    """

    def copy(self, cmd):
        pass


class GetTitleHint(BaseCommand):
    """
    GetTitleHint
    """
    _fields_ = [("flag", ctypes.c_byte), ("data_length", ctypes.c_byte), ("data_buffer", ctypes.c_byte * 128)]

    def copy(self, cmd):
        self.flag = cmd.flag
        self.data_length = cmd.data_length
        self.data_buffer = cmd.data_buffer


class GetPumpAlarm(BaseCommand):
    """
    GetPumpAlarm
    """

    def __init__(self):
        BaseCommand.__init__(self)
        self.command_id = CommandID.convert_command_id_to_int(CommandID.EGetPumpAlarm)
        self.sequence_id = 0
        self.direction = 0
        self.product_id = PRODUCT_ID

    _fields_ = [("alarm_count", ctypes.c_byte),
                ("alarm_buffer", ctypes.c_byte * 250)]

    def copy(self, cmd):
        self.alarm_count = cmd.alarm_count
        self.alarm_buffer = cmd.alarm_buffer


class GetAlarmName(BaseCommand):
    """
    GetAlarmName
    """

    _fields_ = [
        ("alarm_index", ctypes.c_byte),
        ("alarm_level", ctypes.c_byte),
        ("alarm_name_length", ctypes.c_byte),
        ("alarm_name_buffer", ctypes.c_byte * 64)
    ]

    def copy(self, cmd):
        self.alarm_index = cmd.alarm_index
        self.alarm_level = cmd.alarm_level
        self.alarm_name_length = cmd.alarm_name_length
        self.alarm_name_buffer = cmd.alarm_name_buffer


class GetAlarmCount(BaseCommand):
    """
    GetAlarmCount
    """

    _fields_ = [
        ("alarm_count", ctypes.c_byte),
    ]

    def copy(self, cmd):
        self.alarm_count = cmd.alarm_count


class SetAlarmVolume(BaseCommand):
    """
    SetAlarmVolume
    """

    _fields_ = [
        ("alarm_volume", ctypes.c_byte),
    ]

    def copy(self, cmd):
        self.alarm_volume = cmd.alarm_volume


class GetAlarmVolume(BaseCommand):
    """
    GetAlarmVolume
    """

    _fields_ = [
        ("alarm_volume", ctypes.c_byte),
    ]

    def copy(self, cmd):
        self.alarm_volume = cmd.alarm_volume


class SetAlarmSoundType(BaseCommand):
    """
    SetAlarmSoundType
    """

    _fields_ = [
        ("sound_type", ctypes.c_byte),
    ]

    def copy(self, cmd):
        self.sound_type = cmd.sound_type


class GetAlarmSoundType(BaseCommand):
    """
    GetAlarmSoundType
    """

    _fields_ = [
        ("sound_type", ctypes.c_byte),
    ]

    def copy(self, cmd):
        self.sound_type = cmd.sound_type


class GetKVO(BaseCommand):
    """
    GetKVO
    """
    _fields_ = [("KVO", ctypes.c_float)]

    def copy(self, cmd):
        self.KVO = cmd.KVO


class GetScreenValue(BaseCommand):
    """
    GetScreenValue
    """
    _fields_ = [("row", ctypes.c_byte), ("column", ctypes.c_byte), ("screen_id", ctypes.c_byte),
                ("screen_value", ctypes.c_byte * 255)]

    def copy(self, cmd):
        self.row = cmd.row
        self.column = cmd.column
        self.screen_id = cmd.screen_id
        self.screen_value = cmd.screen_value


class GetCurrentMode(BaseCommand):
    """
    GetCurrentMode
    """

    def __init__(self):
        BaseCommand.__init__(self)
        self.command_id = CommandID.convert_command_id_to_int(CommandID.EGetCurrentMode)
        self.sequence_id = 0
        self.direction = 0
        self.product_id = PRODUCT_ID

    _fields_ = [("mode", ctypes.c_byte)]

    def copy(self, cmd):
        self.mode = cmd.mode


class GetOcclusionLevel(BaseCommand):
    """
    GetOcclusionLevel
    """
    _fields_ = [("level", ctypes.c_byte)]

    def copy(self, cmd):
        self.cmd_level = cmd.level
        self.level = self.cmd_level


class GetInfusionMode(BaseCommand):
    """
    GetInfusionMode
    """
    _fields_ = [("infusion_mode", ctypes.c_byte)]

    def copy(self, cmd):
        self.infusion_mode = cmd.infusion_mode


class GetBrand(BaseCommand):
    """
    GetBrand
    """
    _fields_ = [("brand", ctypes.c_int)]

    def copy(self, cmd):
        self.brand = cmd.brand


class GetDoseUnit(BaseCommand):
    """
    GetDoseUnit
    """
    _fields_ = [("dose_unit", ctypes.c_byte)]

    def copy(self, cmd):
        self.dose_unit = cmd.dose_unit


class GetDrugMassUnit(BaseCommand):
    """
    GetDrugMassUnit
    """
    _fields_ = [("drug_mass_unit", ctypes.c_byte)]

    def copy(self, cmd):
        self.drug_mass_unit = cmd.drug_mass_unit


class GetBasicModeRateUnit(BaseCommand):
    """
    GetBasicModeRateUnit
    """
    _fields_ = [("basic_mode_rate_unit", ctypes.c_byte)]

    def copy(self, cmd):
        self.basic_mode_rate_unit = cmd.basic_mode_rate_unit


class GetCurrentDrug(BaseCommand):
    """
    GetCurrentDrug
    """
    _fields_ = [("drug_index", ctypes.c_ushort)]

    def copy(self, cmd):
        self.drug_index = cmd.drug_index


class SetOcclusionLevel(BaseCommand):
    """
    SetOcclusionLevel
    """
    _fields_ = [("pressure_level", ctypes.c_byte)]

    def copy(self, cmd):
        self.pressure_level = cmd.pressure_level


class SetInfusionMode(BaseCommand):
    """
    SetInfusionMode
    """
    _fields_ = [("infusion_mode", ctypes.c_byte)]

    def __init__(self):
        BaseCommand.__init__(self)
        self.command_id = CommandID.convert_command_id_to_int(CommandID.ESetInfusionMode)
        self.sequence_id = 0
        self.direction = 0
        self.product_id = PRODUCT_ID

    def copy(self, cmd):
        self.infusion_mode = cmd.infusion_mode


class SetBrand(BaseCommand):
    """
    SetBrand
    """
    _fields_ = [("brand", ctypes.c_byte)]

    def copy(self, cmd):
        self.brand = cmd.brand


class SetDoseUnit(BaseCommand):
    """
    SetDoseUnit
    """
    _fields_ = [("unit", ctypes.c_byte)]

    def copy(self, cmd):
        self.unit = cmd.unit


class SetDrugMassUnit(BaseCommand):
    """
    SetDrugMassUnit
    """
    _fields_ = [("unit", ctypes.c_byte)]

    def copy(self, cmd):
        self.unit = cmd.unit


class SetWeightUnit(BaseCommand):
    """
    SetWeightUnit
    """
    _fields_ = [("unit", ctypes.c_byte)]

    def copy(self, cmd):
        self.unit = cmd.unit


class SetBasicModeRateUnit(BaseCommand):
    """
    SetBasicModeRateUnit
    """
    _fields_ = [("unit", ctypes.c_byte)]

    def copy(self, cmd):
        self.unit = cmd.unit


class SetKVO(BaseCommand):
    """
    SetKVO
    """
    _fields_ = [("KVO", ctypes.c_float)]

    def copy(self, cmd):
        self.KVO = cmd.KVO


class SetCompleteInfusionAlarmTime(BaseCommand):
    """
    SetCompleteInfusionAlarmTime
    """
    _fields_ = [("alarm_time", ctypes.c_byte)]

    def copy(self, cmd):
        self.alarm_time = cmd.alarm_time


class GetInfusionNearCompleteCriteria(BaseCommand):
    """
    GetInfusionNearCompleteCriteria
    """
    _fields_ = [
        ("infusion_near_complete_criteria", ctypes.c_byte),
        ("parameters_for_criteria", ctypes.c_int)
    ]

    def copy(self, cmd):
        self.infusion_near_complete_criteria = cmd.infusion_near_complete_criteria
        self.parameters_for_criteria = cmd.parameters_for_criteria


class SetInfusionNearCompleteCriteria(BaseCommand):
    """
    SetInfusionNearCompleteCriteria
    """
    pass


class SetTubePrecisionCalibrationBrand(BaseCommand):
    """
    SetTubePrecisionCalibrationBrand
    """
    _fields_ = [("set_result", ctypes.c_byte)]

    def copy(self, cmd):
        self.set_result = cmd.set_result


class SetTubePrecisionCalibrationParameter(BaseCommand):
    """
    SetTubePrecisionCalibrationParameter
    """
    _fields_ = [
        ("sequence_number", ctypes.c_byte),
        ("set_result", ctypes.c_byte),
    ]

    def copy(self, cmd):
        self.sequence_number = cmd.sequence_number
        self.set_result = cmd.set_result


class SetCurrentDrug(BaseCommand):
    """
    SetCurrentDrug
    """
    _fields_ = [("drug_index", ctypes.c_ushort)]

    def copy(self, cmd):
        self.drug_index = cmd.drug_index


class SetDateTime(BaseCommand):
    """
    SetDateTime
    """
    _fields_ = [("year", ctypes.c_ushort),
                ("month", ctypes.c_byte),
                ("day", ctypes.c_byte),
                ("hour", ctypes.c_byte),
                ("minute", ctypes.c_byte),
                ("second", ctypes.c_byte)
                ]

    def copy(self, cmd):
        self.year = cmd.year
        self.month = cmd.month
        self.day = cmd.day
        self.hour = cmd.hour
        self.minute = cmd.minute
        self.second = cmd.second


class SetBrightness(BaseCommand):
    """
    SetBrightness
    """
    _fields_ = [("brightness", ctypes.c_byte),
                ]

    def copy(self, cmd):
        self.brightness = cmd.brightness


class GetBrightness(BaseCommand):
    """
    GetBrightness
    """
    _fields_ = [("brightness", ctypes.c_byte),
                ]

    def copy(self, cmd):
        self.brightness = cmd.brightness


class RestoreFactorySetting(BaseCommand):
    """
    RestoreFactorySetting
    """
    pass


class GetInfusionParameter(BaseCommand):
    """
    GetInfusionParameter
    """
    _fields_ = [("infusion_mode", ctypes.c_byte),
                ("rate_ratemode", ctypes.c_float),
                ("vtbi_ratemode", ctypes.c_float),
                ("hour_timemode", ctypes.c_byte),
                ("minute_timemode", ctypes.c_byte),
                ("vtbi_timemode", ctypes.c_float),
                ("dose_weightmode", ctypes.c_float),
                ("unit_weightmode", ctypes.c_byte),
                ("weight_weightmode", ctypes.c_float),
                ("drug_weightmode", ctypes.c_float),
                ("sol_weightmode", ctypes.c_float),
                ("vtbi_weightmode", ctypes.c_float),
                ("rate1_multiratemode", ctypes.c_float),
                ("hour1_multiratemode", ctypes.c_byte),
                ("minute1_multiratemode", ctypes.c_byte),
                ("rate2_multiratemode", ctypes.c_float),
                ("hour2_multiratemode", ctypes.c_byte),
                ("minute2_multiratemode", ctypes.c_byte),
                ("rate3_multiratemode", ctypes.c_float),
                ("hour3_multiratemode", ctypes.c_byte),
                ("minute3_multiratemode", ctypes.c_byte)]

    def copy(self, cmd):
        self.infusion_mode = cmd.infusion_mode
        self.rate_ratemode = cmd.rate_ratemode
        self.vtbi_ratemode = cmd.vtbi_ratemode
        self.hour_timemode = cmd.hour_timemode
        self.minute_timemode = cmd.minute_timemode
        self.vtbi_timemode = cmd.vtbi_timemode
        self.dose_weightmode = cmd.dose_weightmode
        self.unit_weightmode = cmd.unit_weightmode
        self.weight_weightmode = cmd.weight_weightmode
        self.drug_weightmode = cmd.drug_weightmode
        self.sol_weightmode = cmd.sol_weightmode
        self.vtbi_weightmode = cmd.vtbi_weightmode
        self.rate1_multiratemode = cmd.rate1_multiratemode
        self.hour1_multiratemode = cmd.hour1_multiratemode
        self.minute1_multiratemode = cmd.minute1_multiratemode
        self.rate2_multiratemode = cmd.rate2_multiratemode
        self.hour2_multiratemode = cmd.hour2_multiratemode
        self.minute2_multiratemode = cmd.minute2_multiratemode
        self.rate3_multiratemode = cmd.rate3_multiratemode
        self.hour3_multiratemode = cmd.hour3_multiratemode
        self.minute3_multiratemode = cmd.minute3_multiratemode


class GetInfusingParasOfMode(BaseCommand):
    """
    GetInfusingParasOfMode
    """
    _fields_ = [("infusion_mode", ctypes.c_byte),
                ("brand", ctypes.c_byte),
                ("size", ctypes.c_byte),
                ("current_rate", ctypes.c_float),
                ("remain_hour", ctypes.c_byte),
                ("remain_minute", ctypes.c_byte),
                ("occlusion_level", ctypes.c_byte),
                ("druglib_switch", ctypes.c_byte),
                ("drug_index", ctypes.c_ushort),
                ("total", ctypes.c_float),
                ("remain_volume", ctypes.c_float),
                ("bolus_rate", ctypes.c_float),
                ("bolus_vtbi", ctypes.c_float),
                ("dose", ctypes.c_float),
                ("dose_unit", ctypes.c_byte),
                ("rate1", ctypes.c_float),
                ("remain_hour1", ctypes.c_byte),
                ("remain_minute1", ctypes.c_byte),
                ("rate2", ctypes.c_float),
                ("remain_hour2", ctypes.c_byte),
                ("remain_minute2", ctypes.c_byte),
                ("rate3", ctypes.c_float),
                ("remain_hour3", ctypes.c_byte),
                ("remain_minute3", ctypes.c_byte)
                ]

    def copy(self, cmd):
        self.infusion_mode = cmd.infusion_mode
        self.brand = cmd.brand
        self.size = cmd.size
        self.current_rate = cmd.current_rate
        self.remain_hour = cmd.remain_hour
        self.remain_minute = cmd.remain_minute
        self.occlusion_level = cmd.occlusion_level
        self.druglib_switch = cmd.druglib_switch
        self.drug_index = cmd.drug_index
        self.total = cmd.total
        self.remain_volume = cmd.remain_volume
        self.bolus_rate = cmd.bolus_rate
        self.bolus_vtbi = cmd.bolus_vtbi
        self.dose = cmd.dose
        self.dose_unit = cmd.dose_unit
        self.rate1 = cmd.rate1
        self.remain_hour1 = cmd.remain_hour1
        self.remain_minute1 = cmd.remain_minute1
        self.rate2 = cmd.rate2
        self.remain_hour2 = cmd.remain_hour2
        self.remain_minute2 = cmd.remain_minute2
        self.rate3 = cmd.rate3
        self.remain_hour3 = cmd.remain_hour3
        self.remain_minute3 = cmd.remain_minute3


class ResetPumpMode(BaseCommand):
    """
    ResetPumpMode
    """

    def __init__(self):
        BaseCommand.__init__(self)
        self.command_id = CommandID.convert_command_id_to_int(CommandID.EResetPumpMode)
        self.sequence_id = 0
        self.direction = 0
        self.product_id = PRODUCT_ID

    _fields_ = [("mode", ctypes.c_byte)]

    def copy(self, cmd):
        self.mode = cmd.mode


class SendFileStart(BaseCommand):
    """
    SendFileStart
    """

    _fields_ = [("filetype", ctypes.c_byte),
                ("subid", ctypes.c_byte),
                ("filesize", ctypes.c_uint),
                ("checksum", ctypes.c_uint),
                ("blockcount", ctypes.c_uint)]

    def __init__(self):
        BaseCommand.__init__(self)
        self.command_id = CommandID.convert_command_id_to_int(CommandID.ESendFileStart)
        self.sequence_id = 0
        self.direction = 0
        self.product_id = PRODUCT_ID

    def fill_parameter(self, filetype, subid, filesize, checksum, blockcount):
        self.filetype = filetype
        self.subid = subid
        self.filesize = filesize
        self.checksum = checksum
        self.blockcount = blockcount

    def copy(self, cmd):
        self.filetype = cmd.filetype
        self.subid = cmd.subid
        self.filesize = cmd.filesize
        self.checksum = cmd.checksum
        self.blockcount = cmd.blockcount


class SendFilePackage(BaseCommand):
    """
    SendFilePackage
    """

    _fields_ = [("filetype", ctypes.c_byte),
                ("subid", ctypes.c_byte),
                ("sequencenumber", ctypes.c_uint),
                ("packagedatalength", ctypes.c_ushort),
                ("packagedata", ctypes.c_byte * 128)]

    def __init__(self):
        BaseCommand.__init__(self)
        self.command_id = CommandID.convert_command_id_to_int(CommandID.ESendFilePackage)
        self.sequence_id = 0
        self.direction = 0
        self.product_id = PRODUCT_ID

    def fill_parameter(self, filetype, subid, sequencenumber, packagedatalength, packagedata):
        self.filetype = filetype
        self.subid = subid
        self.sequencenumber = sequencenumber
        self.packagedatalength = packagedatalength
        for i in range(packagedatalength):
            self.packagedata[i] = packagedata[i]

    def copy(self, cmd):
        self.filetype = cmd.filetype
        self.subid = cmd.subid
        self.sequencenumber = cmd.sequencenumber
        self.packagedatalength = cmd.packagedatalength
        self.packagedata = cmd.packagedata


class SendFileCompleted(BaseCommand):
    """
    SendFileCompleted, sendresult: Fail = 0x00,Success = 0x01,Cancel = 0x02,
    """

    _fields_ = [("filetype", ctypes.c_byte), ("subid", ctypes.c_byte), ("sendresult", ctypes.c_byte)]

    def __init__(self):
        BaseCommand.__init__(self)
        self.command_id = CommandID.convert_command_id_to_int(CommandID.ESendFileCompleted)
        self.sequence_id = 0
        self.direction = 0
        self.product_id = PRODUCT_ID

    def fill_parameter(self, filetype, subid, sendresult):
        self.filetype = filetype
        self.subid = subid
        self.sendresult = sendresult

    def copy(self, cmd):
        self.filetype = cmd.filetype
        self.subid = cmd.subid
        self.sendresult = cmd.sendresult


class SetInfusionParameter(BaseCommand):
    """
    SetInfusionParameter
    """

    _fields_ = [
        ("infusion_mode", ctypes.c_byte),
        ("rate_ratemode", ctypes.c_float),
        ("vtbi_ratemode", ctypes.c_float),
        ("hour_timemode", ctypes.c_byte),
        ("minute_timemode", ctypes.c_byte),
        ("vtbi_timemode", ctypes.c_float),
        ("dose_weightmode", ctypes.c_float),
        ("unit_weightmode", ctypes.c_byte),
        ("weight_weightmode", ctypes.c_float),
        ("drug_weightmode", ctypes.c_float),
        ("sol_weightmode", ctypes.c_float),
        ("vtbi_weightmode", ctypes.c_float),
        ("rate1_multiratemode", ctypes.c_float),
        ("hour1_multiratemode", ctypes.c_byte),
        ("minute1_multiratemode", ctypes.c_byte),
        ("rate2_multiratemode", ctypes.c_float),
        ("hour2_multiratemode", ctypes.c_byte),
        ("minute2_multiratemode", ctypes.c_byte),
        ("rate3_multiratemode", ctypes.c_float),
        ("hour3_multiratemode", ctypes.c_byte),
        ("minute3_multiratemode", ctypes.c_byte),
        ("rate_basicmode", ctypes.c_float),
        ("rateunit_basicmode", ctypes.c_byte),
        ("dropsize_basicmode", ctypes.c_uint),
        ("droprate_basicmode", ctypes.c_uint),
        ("infusion_time_basicmode", ctypes.c_uint),
        ("vtbi_basicmode", ctypes.c_float),
        ("delay_start_time_basicmode", ctypes.c_uint),
        ("dose_weightmodeLVP", ctypes.c_float),
        ("doseunit_weightmodeLVP", ctypes.c_byte),
        ("weight_weightmodeLVP", ctypes.c_float),
        ("weightunit_weightmodeLVP", ctypes.c_byte),
        ("drugmass_weightmodeLVP", ctypes.c_float),
        ("drugmass_unit_weightmodeLVP", ctypes.c_byte),
        ("volume_weightmodeLVP", ctypes.c_float),
        ("vtbi_weightmodeLVP", ctypes.c_float),
        ("delay_start_time_weightmodeLVP", ctypes.c_byte),
        ("rate1_multiratemodeLVP", ctypes.c_float),
        ("infusion_time1_multiratemodeLVP", ctypes.c_byte),
        ("rate2_multiratemodeLVP", ctypes.c_float),
        ("infusion_time2_multiratemodeLVP", ctypes.c_byte),
        ("rate3_multiratemodeLVP", ctypes.c_float),
        ("infusion_time3_multiratemodeLVP", ctypes.c_byte),
        ("vtbi_tapermode", ctypes.c_float),
        ("infusion_time_tapermode", ctypes.c_byte),
        ("taperup_time_tapermode", ctypes.c_byte),
        ("taperdown_time_tapermode", ctypes.c_byte),
        ("plateau_rate_stepmode", ctypes.c_float),
        ("vtbi_stepmode", ctypes.c_float),
        ("initial_rate_stepmode", ctypes.c_float),
        ("step_increment_stepmode", ctypes.c_float),
        ("step_duration_time_stepmode", ctypes.c_byte),
        ("druglib_switch", ctypes.c_byte),
        ("drug_index", ctypes.c_byte)

    ]

    def __init__(self):
        BaseCommand.__init__(self)
        self.command_id = CommandID.convert_command_id_to_int(CommandID.ESetInfusionParameter)
        self.sequence_id = 0
        self.direction = 0
        self.product_id = PRODUCT_ID

    def fill_rate_mode_parameter(self, rate, vtbi):
        self.infusion_mode = 0
        self.rate_ratemode = rate
        self.vtbi_ratemode = vtbi

    def fill_time_mode_parameter(self, hour, minute, vtbi):
        self.infusion_mode = 1
        self.hour_timemode = hour
        self.minute_timemode = minute
        self.vtbi_timemode = vtbi

    def fill_weight_mode_parameter(self, dose, weight, drug, sol, vtbi, unit=2):
        self.infusion_mode = 2
        self.dose_weightmode = dose
        self.unit_weightmode = unit
        self.weight_weightmode = weight
        self.drug_weightmode = drug
        self.sol_weightmode = sol
        self.vtbi_weightmode = vtbi

    def fill_multi_rate_mode_parameter(self, rate1, hour1, minute1, rate2, hour2, minute2, rate3, hour3, minute3):
        self.infusion_mode = 3
        self.rate1_multiratemode = rate1
        self.hour1_multiratemode = hour1
        self.minute1_multiratemode = minute1
        self.rate2_multiratemode = rate2
        self.hour2_multiratemode = hour2
        self.minute2_multiratemode = minute2
        self.rate3_multiratemode = rate3
        self.hour3_multiratemode = hour3
        self.minute3_multiratemode = minute3

    def fill_basic_mode_parameter(self, rate, infusion_time, vtbi):
        self.infusion_mode = 16
        self.rate_basicmode = rate
        self.infusion_time_basicmode = infusion_time
        self.vtbi_basicmode = vtbi

    def copy(self, cmd):
        self.infusion_mode = cmd.infusion_mode
        self.rate_ratemode = cmd.rate_ratemode
        self.vtbi_ratemode = cmd.vtbi_ratemode
        self.hour_timemode = cmd.hour_timemode
        self.minute_timemode = cmd.minute_timemode
        self.vtbi_timemode = cmd.vtbi_timemode
        self.dose_weightmode = cmd.dose_weightmode
        self.unit_weightmode = cmd.unit_weightmode
        self.weight_weightmode = cmd.weight_weightmode
        self.drug_weightmode = cmd.drug_weightmode
        self.sol_weightmode = cmd.sol_weightmode
        self.vtbi_weightmode = cmd.vtbi_weightmode
        self.rate1_multiratemode = cmd.rate1_multiratemode
        self.hour1_multiratemode = cmd.hour1_multiratemode
        self.minute1_multiratemode = cmd.minute1_multiratemode
        self.rate2_multiratemode = cmd.rate2_multiratemode
        self.hour2_multiratemode = cmd.hour2_multiratemode
        self.minute2_multiratemode = cmd.minute2_multiratemode
        self.rate3_multiratemode = cmd.rate3_multiratemode
        self.hour3_multiratemode = cmd.hour3_multiratemode
        self.minute3_multiratemode = cmd.minute3_multiratemode
        self.rate_basicmode = cmd.rate_basicmode
        self.rateunit_basicmode = cmd.rateunit_basicmode
        self.dropsize_basicmode = cmd.dropsize_basicmode
        self.droprate_basicmode = cmd.droprate_basicmode
        self.infusion_time_basicmode = cmd.infusion_time_basicmode
        self.vtbi_basicmode = cmd.vtbi_basicmode
        self.delay_start_time_basicmode = cmd.delay_start_time_basicmode
        self.dose_weightmodeLVP = cmd.dose_weightmodeLVP
        self.doseunit_weightmodeLVP = cmd.doseunit_weightmodeLVP
        self.weight_weightmodeLVP = cmd.weight_weightmodeLVP
        self.weightunit_weightmodeLVP = cmd.weightunit_weightmodeLVP
        self.drugmass_weightmodeLVP = cmd.drugmass_weightmodeLVP
        self.drugmass_unit_weightmodeLVP = cmd.drugmass_unit_weightmodeLVP
        self.volume_weightmodeLVP = cmd.volume_weightmodeLVP
        self.vtbi_weightmodeLVP = cmd.vtbi_weightmodeLVP
        self.delay_start_time_weightmodeLVP = cmd.delay_start_time_weightmodeLVP
        self.rate1_multiratemodeLVP = cmd.rate1_multiratemodeLVP
        self.infusion_time1_multiratemodeLVP = cmd.infusion_time1_multiratemodeLVP
        self.rate2_multiratemodeLVP = cmd.rate2_multiratemodeLVP
        self.infusion_time2_multiratemodeLVP = cmd.infusion_time2_multiratemodeLVP
        self.rate3_multiratemodeLVP = cmd.rate3_multiratemodeLVP
        self.infusion_time3_multiratemodeLVP = cmd.infusion_time3_multiratemodeLVP
        self.vtbi_tapermode = cmd.vtbi_tapermode
        self.infusion_time_tapermode = cmd.infusion_time_tapermode
        self.taperup_time_tapermode = cmd.taperup_time_tapermode
        self.taperdown_time_tapermode = cmd.taperdown_time_tapermode
        self.plateau_rate_stepmode = cmd.plateau_rate_stepmode
        self.vtbi_stepmode = cmd.vtbi_stepmode
        self.initial_rate_stepmode = cmd.initial_rate_stepmode
        self.step_increment_stepmode = cmd.step_increment_stepmode
        self.step_duration_time_stepmode = cmd.step_duration_time_stepmode
        self.druglib_switch = cmd.druglib_switch
        self.drug_index = cmd.drug_index


class StructInfusionParameter(ctypes.Structure):
    """
    StructInfusionParameter
    """
    _fields_ = [
        ("infusion_mode", ctypes.c_byte),
        ("rate_ratemode", ctypes.c_float),
        ("vtbi_ratemode", ctypes.c_float),
        ("hour_timemode", ctypes.c_byte),
        ("minute_timemode", ctypes.c_byte),
        ("vtbi_timemode", ctypes.c_float),
        ("dose_weightmode", ctypes.c_float),
        ("unit_weightmode", ctypes.c_byte),
        ("weight_weightmode", ctypes.c_float),
        ("drug_weightmode", ctypes.c_float),
        ("sol_weightmode", ctypes.c_float),
        ("vtbi_weightmode", ctypes.c_float),
        ("rate1_multiratemode", ctypes.c_float),
        ("hour1_multiratemode", ctypes.c_byte),
        ("minute1_multiratemode", ctypes.c_byte),
        ("rate2_multiratemode", ctypes.c_float),
        ("hour2_multiratemode", ctypes.c_byte),
        ("minute2_multiratemode", ctypes.c_byte),
        ("rate3_multiratemode", ctypes.c_float),
        ("hour3_multiratemode", ctypes.c_byte),
        ("minute3_multiratemode", ctypes.c_byte),
        ("rate_basicmode", ctypes.c_float),
        ("rateunit_basicmode", ctypes.c_byte),
        ("dropsize_basicmode", ctypes.c_uint),
        ("droprate_basicmode", ctypes.c_uint),
        ("infusion_time_basicmode", ctypes.c_uint),
        ("vtbi_basicmode", ctypes.c_float),
        ("delay_start_time_basicmode", ctypes.c_uint),
        ("dose_weightmodeLVP", ctypes.c_float),
        ("doseunit_weightmodeLVP", ctypes.c_byte),
        ("weight_weightmodeLVP", ctypes.c_float),
        ("weightunit_weightmodeLVP", ctypes.c_byte),
        ("drugmass_weightmodeLVP", ctypes.c_float),
        ("drugmass_unit_weightmodeLVP", ctypes.c_byte),
        ("volume_weightmodeLVP", ctypes.c_float),
        ("vtbi_weightmodeLVP", ctypes.c_float),
        ("delay_start_time_weightmodeLVP", ctypes.c_byte),
        ("rate1_multiratemodeLVP", ctypes.c_float),
        ("infusion_time1_multiratemodeLVP", ctypes.c_byte),
        ("rate2_multiratemodeLVP", ctypes.c_float),
        ("infusion_time2_multiratemodeLVP", ctypes.c_byte),
        ("rate3_multiratemodeLVP", ctypes.c_float),
        ("infusion_time3_multiratemodeLVP", ctypes.c_byte),
        ("vtbi_tapermode", ctypes.c_float),
        ("infusion_time_tapermode", ctypes.c_byte),
        ("taperup_time_tapermode", ctypes.c_byte),
        ("taperdown_time_tapermode", ctypes.c_byte),
        ("plateau_rate_stepmode", ctypes.c_float),
        ("vtbi_stepmode", ctypes.c_float),
        ("initial_rate_stepmode", ctypes.c_float),
        ("step_increment_stepmode", ctypes.c_float),
        ("step_duration_time_stepmode", ctypes.c_byte),
        ("druglib_switch", ctypes.c_byte),
        ("drug_index", ctypes.c_byte),

    ]

    def __init__(self):
        pass

    def copy(self, cmd):
        self.infusion_mode = cmd.infusion_mode
        self.rate_ratemode = cmd.rate_ratemode
        self.vtbi_ratemode = cmd.vtbi_ratemode
        self.hour_timemode = cmd.hour_timemode
        self.minute_timemode = cmd.minute_timemode
        self.vtbi_timemode = cmd.vtbi_timemode
        self.dose_weightmode = cmd.dose_weightmode
        self.unit_weightmode = cmd.unit_weightmode
        self.weight_weightmode = cmd.weight_weightmode
        self.drug_weightmode = cmd.drug_weightmode
        self.sol_weightmode = cmd.sol_weightmode
        self.vtbi_weightmode = cmd.vtbi_weightmode
        self.rate1_multiratemode = cmd.rate1_multiratemode
        self.hour1_multiratemode = cmd.hour1_multiratemode
        self.minute1_multiratemode = cmd.minute1_multiratemode
        self.rate2_multiratemode = cmd.rate2_multiratemode
        self.hour2_multiratemode = cmd.hour2_multiratemode
        self.minute2_multiratemode = cmd.minute2_multiratemode
        self.rate3_multiratemode = cmd.rate3_multiratemode
        self.hour3_multiratemode = cmd.hour3_multiratemode
        self.minute3_multiratemode = cmd.minute3_multiratemode
        self.rate_basicmode = cmd.rate_basicmode
        self.rateunit_basicmode = cmd.rateunit_basicmode
        self.dropsize_basicmode = cmd.dropsize_basicmode
        self.droprate_basicmode = cmd.droprate_basicmode
        self.infusion_time_basicmode = cmd.infusion_time_basicmode
        self.vtbi_basicmode = cmd.vtbi_basicmode
        self.delay_start_time_basicmode = cmd.delay_start_time_basicmode
        self.dose_weightmodeLVP = cmd.dose_weightmodeLVP
        self.doseunit_weightmodeLVP = cmd.doseunit_weightmodeLVP
        self.weight_weightmodeLVP = cmd.weight_weightmodeLVP
        self.weightunit_weightmodeLVP = cmd.weightunit_weightmodeLVP
        self.drugmass_weightmodeLVP = cmd.drugmass_weightmodeLVP
        self.drugmass_unit_weightmodeLVP = cmd.drugmass_unit_weightmodeLVP
        self.volume_weightmodeLVP = cmd.volume_weightmodeLVP
        self.vtbi_weightmodeLVP = cmd.vtbi_weightmodeLVP
        self.delay_start_time_weightmodeLVP = cmd.delay_start_time_weightmodeLVP
        self.rate1_multiratemodeLVP = cmd.rate1_multiratemodeLVP
        self.infusion_time1_multiratemodeLVP = cmd.infusion_time1_multiratemodeLVP
        self.rate2_multiratemodeLVP = cmd.rate2_multiratemodeLVP
        self.infusion_time2_multiratemodeLVP = cmd.infusion_time2_multiratemodeLVP
        self.rate3_multiratemodeLVP = cmd.rate3_multiratemodeLVP
        self.infusion_time3_multiratemodeLVP = cmd.infusion_time3_multiratemodeLVP
        self.vtbi_tapermode = cmd.vtbi_tapermode
        self.infusion_time_tapermode = cmd.infusion_time_tapermode
        self.taperup_time_tapermode = cmd.taperup_time_tapermode
        self.taperdown_time_tapermode = cmd.taperdown_time_tapermode
        self.plateau_rate_stepmode = cmd.plateau_rate_stepmode
        self.vtbi_stepmode = cmd.vtbi_stepmode
        self.initial_rate_stepmode = cmd.initial_rate_stepmode
        self.step_increment_stepmode = cmd.step_increment_stepmode
        self.step_duration_time_stepmode = cmd.step_duration_time_stepmode
        self.druglib_switch = cmd.druglib_switch
        self.drug_index = cmd.drug_index


class SetInfusingParameter(BaseCommand):
    """
    SetInfusingParameter
    """

    _fields_ = [
        # rate mode
        ("infusion_mode", ctypes.c_byte),
        ("current_rate_ratemode", ctypes.c_float),
        # time mode
        ("hour_timemode", ctypes.c_byte),
        ("minute_timemode", ctypes.c_byte),
        # weight mode
        ("dose_weightmode", ctypes.c_float)
    ]

    def __init__(self):
        BaseCommand.__init__(self)
        self.command_id = CommandID.convert_command_id_to_int(CommandID.ESetInfusingParameterOfMode)
        self.sequence_id = 0
        self.direction = 0
        self.product_id = PRODUCT_ID

    def fill_rate_mode_parameter(self, rate):
        self.infusion_mode = 0
        self.current_rate_ratemode = rate

    def fill_time_mode_parameter(self, hour, minute):
        self.infusion_mode = 1
        self.hour_timemode = hour
        self.minute_timemode = minute

    def fill_weight_mode_parameter(self, dose):
        self.infusion_mode = 2
        self.dose_weightmode = dose

    def fill_multi_rate_mode_parameter(self, rate):
        self.infusion_mode = 3
        self.current_rate_ratemode = rate

    def copy(self, cmd):
        self.infusion_mode = cmd.infusion_mode
        self.current_rate_ratemode = cmd.current_rate_ratemode
        self.hour_timemode = cmd.hour_timemode
        self.minute_timemode = cmd.minute_timemode
        self.dose_weightmode = cmd.dose_weightmode


class StructInfusingParameter(ctypes.Structure):
    _fields_ = [
        # rate mode
        # multirate mode
        ("infusion_mode", ctypes.c_byte),
        ("current_rate_ratemode", ctypes.c_float),
        # time mode
        ("hour_timemode", ctypes.c_byte),
        ("minute_timemode", ctypes.c_byte),
        # weight mode
        ("dose_weightmode", ctypes.c_float)]

    def __init__(self):
        pass

    def copy(self, cmd):
        self.infusion_mode = cmd.infusion_mode
        self.current_rate_ratemode = cmd.current_rate_ratemode
        self.hour_timemode = cmd.hour_timemode
        self.minute_timemode = cmd.minute_timemode
        self.dose_weightmode = cmd.dose_weightmode


class RemoteStartStopInfusion(BaseCommand):
    """
    RemoteStartStopInfusion
    """

    _fields_ = [("is_start", ctypes.c_byte)]

    def __init__(self):
        BaseCommand.__init__(self)
        self.command_id = CommandID.convert_command_id_to_int(CommandID.ERemoteStartStopInfusion)
        self.sequence_id = 0
        self.direction = 0
        self.product_id = PRODUCT_ID

    def fill_parameter(self, start_or_stop=1):
        self.is_start = start_or_stop

    def copy(self, cmd):
        pass
        # self.is_start = cmd.is_start


class GetSystemStatus(BaseCommand):
    """
    GetSystemStatus
    """

    def __init__(self):
        BaseCommand.__init__(self)
        self.command_id = CommandID.convert_command_id_to_int(CommandID.EGetSystemStatus)
        self.sequence_id = 0
        self.direction = 0
        self.product_id = PRODUCT_ID

    _fields_ = [("pump_status", ctypes.c_byte)]

    def copy(self, cmd):
        self.pump_status = cmd.pump_status


class SetBolusRate(BaseCommand):
    """
    SetBolusRate
    """

    def __init__(self):
        BaseCommand.__init__(self)
        self.command_id = CommandID.convert_command_id_to_int(CommandID.ESetBolusRate)
        self.sequence_id = 0
        self.direction = 0
        self.product_id = PRODUCT_ID

    _fields_ = [("bolus_rate", ctypes.c_byte)]

    def copy(self, cmd):
        self.bolus_rate = cmd.bolus_rate


class SetNightModePeriod(BaseCommand):
    """
    SetNightModePeriod
    """
    _fields_ = [("begin_hour", ctypes.c_byte),
                ("begin_minute", ctypes.c_byte),
                ("end_hour", ctypes.c_byte),
                ("end_minute", ctypes.c_byte),
                ]

    def copy(self, cmd):
        self.begin_hour = cmd.begin_hour
        self.begin_minute = cmd.begin_minute
        self.end_hour = cmd.end_hour
        self.end_minute = cmd.end_minute


class GetNightModePeriod(BaseCommand):
    """
    GetNightModePeriod
    """
    _fields_ = [("begin_hour", ctypes.c_byte),
                ("begin_minute", ctypes.c_byte),
                ("end_hour", ctypes.c_byte),
                ("end_minute", ctypes.c_byte),
                ]

    def copy(self, cmd):
        self.begin_hour = cmd.begin_hour
        self.begin_minute = cmd.begin_minute
        self.end_hour = cmd.end_hour
        self.end_minute = cmd.end_minute


class SetNightModeAlarmVolume(BaseCommand):
    """
    SetNightModeAlarmVolume
    """
    _fields_ = [("alarm_volume", ctypes.c_byte),
                ]

    def copy(self, cmd):
        self.alarm_volume = cmd.alarm_volume


class GetNightModeAlarmVolume(BaseCommand):
    """
    GetNightModeAlarmVolume
    """
    _fields_ = [("alarm_volume", ctypes.c_byte),
                ]

    def copy(self, cmd):
        self.alarm_volume = cmd.alarm_volume


class SetNightModeBrightness(BaseCommand):
    """
    SetNightModeBrightness
    """
    _fields_ = [("brightness", ctypes.c_byte),
                ]

    def copy(self, cmd):
        self.brightness = cmd.brightness


class GetNightModeBrightness(BaseCommand):
    """
    GetNightModeBrightness
    """
    _fields_ = [("brightness", ctypes.c_byte),
                ]

    def copy(self, cmd):
        self.brightness = cmd.brightness


class SetSecuritySwitch(BaseCommand):
    """
    SetSecuritySwitch
    """

    _fields_ = [("switch_mask", ctypes.c_int),
                ("switch_status", ctypes.c_int)
                ]

    def copy(self, cmd):
        self.switch_mask = cmd.switch_mask
        self.switch_status = cmd.switch_status


class GetSecuritySwitch(BaseCommand):
    """
    GetSecuritySwitch
    """

    _fields_ = [("switch_mask", ctypes.c_int),
                ("switch_status", ctypes.c_int)
                ]

    def copy(self, cmd):
        self.switch_mask = cmd.switch_mask
        self.switch_status = cmd.switch_status


class ClearHistoryLog(BaseCommand):
    """
    ClearHistoryLog
    """

    pass
    # _fields_ = [("switch_mask", ctypes.c_int),
    #             ("switch_status", ctypes.c_int)
    #             ]
    #
    # def copy(self, cmd):
    #     self.switch_mask = cmd.switch_mask
    #     self.switch_status = cmd.switch_status


class GetLogTotalNum(BaseCommand):
    """
    GetLogTotalNum
    """

    _fields_ = [("log_total_number", ctypes.c_byte),
                ]

    def copy(self, cmd):
        self.log_total_number = cmd.log_total_number


class GetBubbleSensitivity(BaseCommand):
    """
    GetBubbleSensitivity
    """

    _fields_ = [
        ("air_detection_option", ctypes.c_byte),
        ("bubble_sensitivity", ctypes.c_byte),
    ]

    def copy(self, cmd):
        self.air_detection_option = cmd.air_detection_option
        self.bubble_sensitivity = cmd.bubble_sensitivity


class SetBubbleSensitivity(BaseCommand):
    """
    SetBubbleSensitivity
    """

    pass


class VerifyPasscode(BaseCommand):
    """
    VerifyPasscode
    """

    _fields_ = [
        ("screen_type", ctypes.c_byte),
        ("verified_result", ctypes.c_byte),
    ]

    def copy(self, cmd):
        self.screen_type = cmd.screen_type
        self.verified_result = cmd.verified_result


class GetLogItem(BaseCommand):
    """
    GetLogItem
    """

    _fields_ = [
        ("sequence_num", ctypes.c_int),
        ("timestamp", ctypes.c_int),
        ("summaryLength", ctypes.c_short),
        ("summary", ctypes.c_byte * 64),
        ("detailLength", ctypes.c_short),
        ("admin_detail", ctypes.c_byte * 384),
    ]

    def copy(self, cmd):
        self.sequence_num = cmd.sequence_num
        self.timestamp = cmd.timestamp
        self.summaryLength = cmd.summaryLength
        self.summary = cmd.summary
        self.detailLength = cmd.detailLength
        self.admin_detail = cmd.admin_detail


class WriteLog(BaseCommand):
    """
    WriteLog
    """
    _fields_ = [("log_index", ctypes.c_int),
                ]

    def copy(self, cmd):
        self.log_index = cmd.log_index


class GetMaintenanceDateTime(BaseCommand):
    """
    GetMaintenanceDateTime
    """
    _fields_ = [
        ("last_maintenance_year", ctypes.c_short),
        ("last_maintenance_month", ctypes.c_byte),
        ("last_maintenance_day", ctypes.c_byte),
        ("last_maintenance_hour", ctypes.c_byte),
        ("last_maintenance_minute", ctypes.c_byte),
        ("last_maintenance_second", ctypes.c_byte),
        ("next_maintenance_year", ctypes.c_short),
        ("next_maintenance_month", ctypes.c_byte),
        ("next_maintenance_day", ctypes.c_byte),
        ("next_maintenance_hour", ctypes.c_byte),
        ("next_maintenance_minute", ctypes.c_byte),
        ("next_maintenance_second", ctypes.c_byte),
    ]

    def copy(self, cmd):
        self.last_maintenance_year = cmd.last_maintenance_year
        self.last_maintenance_month = cmd.last_maintenance_month
        self.last_maintenance_day = cmd.last_maintenance_day
        self.last_maintenance_hour = cmd.last_maintenance_hour
        self.last_maintenance_minute = cmd.last_maintenance_minute
        self.last_maintenance_second = cmd.last_maintenance_second

        self.next_maintenance_year = cmd.next_maintenance_year
        self.next_maintenance_month = cmd.next_maintenance_month
        self.next_maintenance_day = cmd.next_maintenance_day
        self.next_maintenance_hour = cmd.next_maintenance_hour
        self.next_maintenance_minute = cmd.next_maintenance_minute
        self.next_maintenance_second = cmd.next_maintenance_second


class GetMaintenancePeriod(BaseCommand):
    """
    GetMaintenancePeriod
    """
    _fields_ = [("maintenance_period", ctypes.c_byte),
                ]

    def copy(self, cmd):
        self.maintenance_period = cmd.maintenance_period


class GetAlarmTypePassword(BaseCommand):
    """
    GetAlarmTypePassword
    """
    _fields_ = [("passcode", ctypes.c_int),
                ]

    def copy(self, cmd):
        self.passcode = cmd.passcode


class GetFactoryFirmwareVersion(BaseCommand):
    """
    GetFactoryFirmwareVersion
    """
    _fields_ = [
        ("firmware_type", ctypes.c_byte),
        ("major_version", ctypes.c_byte),
        ("minor_version", ctypes.c_short),
        ("revision_version", ctypes.c_short),
        ("build_number", ctypes.c_int),
    ]

    def copy(self, cmd):
        self.firmware_type = cmd.firmware_type
        self.major_version = cmd.major_version
        self.minor_version = cmd.minor_version
        self.revision_version = cmd.revision_version
        self.build_number = cmd.build_number


class GetSensorStatus(BaseCommand):
    """
    GetSensorStatus
    """
    _fields_ = [
        ("sensor_status", ctypes.c_int),

    ]

    def copy(self, cmd):
        self.sensor_status = cmd.sensor_status


class GetFirmwareVersion(BaseCommand):
    """
    GetFirmwareVersion
    """

    # def __init__(self):
    #     BaseCommand.__init__(self)
    #     self.command_id = CommandID.convert_command_id_to_int(CommandID.EGetFirmwareVersion)
    #     self.sequence_id = 0
    #     self.direction = 0
    #     self.product_id = PRODUCT_ID

    _fields_ = [
        # MainFirmware
        ("main_firmware_firmware_type", ctypes.c_byte),
        ("main_firmware_major_version", ctypes.c_byte),
        ("main_firmware_minor_version", ctypes.c_short),
        ("main_firmware_revision_version", ctypes.c_short),
        ("main_firmware_build_number", ctypes.c_int),
        # UIFirmware
        ("ui_firmware_firmware_type", ctypes.c_byte),
        ("ui_firmware_major_version", ctypes.c_byte),
        ("ui_firmware_minor_version", ctypes.c_short),
        ("ui_firmware_revision_version", ctypes.c_short),
        ("ui_firmware_build_number", ctypes.c_int),
        # MainBootloader
        ("main_bootloader_firmware_type", ctypes.c_byte),
        ("main_bootloader_major_version", ctypes.c_byte),
        ("main_bootloader_minor_version", ctypes.c_short),
        ("main_bootloader_revision_version", ctypes.c_short),
        ("main_bootloader_build_number", ctypes.c_int),
        # UIBootloader
        ("ui_bootloader_firmware_type", ctypes.c_byte),
        ("ui_bootloader_major_version", ctypes.c_byte),
        ("ui_bootloader_minor_version", ctypes.c_short),
        ("ui_bootloader_revision_version", ctypes.c_short),
        ("ui_bootloader_build_number", ctypes.c_int),
        # SafetyFirmware
        ("safety_firmware_firmware_type", ctypes.c_byte),
        ("safety_firmware_major_version", ctypes.c_byte),
        ("safety_firmware_minor_version", ctypes.c_short),
        ("safety_firmware_revision_version", ctypes.c_short),
        ("safety_firmware_build_number", ctypes.c_int),
        # SafetyBootloaderFirmware
        ("safety_bootloader_firmware_firmware_type", ctypes.c_byte),
        ("safety_bootloader_firmware_major_version", ctypes.c_byte),
        ("safety_bootloader_firmware_minor_version", ctypes.c_short),
        ("safety_bootloader_firmware_revision_version", ctypes.c_short),
        ("safety_bootloader_firmware_build_number", ctypes.c_int),
    ]

    def copy(self, cmd):
        self.main_firmware_firmware_type = cmd.main_firmware_firmware_type
        self.main_firmware_major_version = cmd.main_firmware_major_version
        self.main_firmware_minor_version = cmd.main_firmware_minor_version
        self.main_firmware_revision_version = cmd.main_firmware_revision_version
        self.main_firmware_build_number = cmd.main_firmware_build_number

        self.ui_firmware_firmware_type = cmd.ui_firmware_firmware_type
        self.ui_firmware_major_version = cmd.ui_firmware_major_version
        self.ui_firmware_minor_version = cmd.ui_firmware_minor_version
        self.ui_firmware_revision_version = cmd.ui_firmware_revision_version
        self.ui_firmware_build_number = cmd.ui_firmware_build_number

        self.main_bootloader_firmware_type = cmd.main_bootloader_firmware_type
        self.main_bootloader_major_version = cmd.main_bootloader_major_version
        self.main_bootloader_minor_version = cmd.main_bootloader_minor_version
        self.main_bootloader_revision_version = cmd.main_bootloader_revision_version
        self.main_bootloader_build_number = cmd.main_bootloader_build_number

        self.ui_bootloader_firmware_type = cmd.ui_bootloader_firmware_type
        self.ui_bootloader_major_version = cmd.ui_bootloader_major_version
        self.ui_bootloader_minor_version = cmd.ui_bootloader_minor_version
        self.ui_bootloader_revision_version = cmd.ui_bootloader_revision_version
        self.ui_bootloader_build_number = cmd.ui_bootloader_build_number

        self.safety_firmware_firmware_type = cmd.safety_firmware_firmware_type
        self.safety_firmware_major_version = cmd.safety_firmware_major_version
        self.safety_firmware_minor_version = cmd.safety_firmware_minor_version
        self.safety_firmware_revision_version = cmd.safety_firmware_revision_version
        self.safety_firmware_build_number = cmd.safety_firmware_build_number

        self.safety_bootloader_firmware_firmware_type = cmd.safety_bootloader_firmware_firmware_type
        self.safety_bootloader_firmware_major_version = cmd.safety_bootloader_firmware_major_version
        self.safety_bootloader_firmware_minor_version = cmd.safety_bootloader_firmware_minor_version
        self.safety_bootloader_firmware_revision_version = cmd.safety_bootloader_firmware_revision_version
        self.safety_bootloader_firmware_build_number = cmd.safety_bootloader_firmware_build_number


class RemoteStartPrime(BaseCommand):
    """
    RemoteStartPrime
    """

    _fields_ = [("is_start", ctypes.c_byte)]

    def __init__(self):
        BaseCommand.__init__(self)
        self.command_id = CommandID.convert_command_id_to_int(CommandID.ERemoteStartPrime)
        self.sequence_id = 0
        self.direction = 0
        self.product_id = PRODUCT_ID

    def fill_parameter(self, start_or_stop=1):
        self.is_start = start_or_stop

    def copy(self, cmd):
        # self.is_start = cmd.is_start
        pass


class RemoteStartBolus(BaseCommand):
    """
    RemoteStartBolus
    """

    _fields_ = [("is_start", ctypes.c_byte)]

    def __init__(self):
        BaseCommand.__init__(self)
        self.command_id = CommandID.convert_command_id_to_int(CommandID.ERemoteStartBolus)
        self.sequence_id = 0
        self.direction = 0
        self.product_id = PRODUCT_ID

    def fill_parameter(self, start_or_stop=1):
        self.is_start = start_or_stop

    def copy(self, cmd):
        # self.is_start = cmd.is_start
        pass


class RemoteSetBolusParameter(BaseCommand):
    """
    RemoteSetBolusParameter
    """

    _fields_ = [
        ("bolus_rate", ctypes.c_float),
        ("bolus_volume", ctypes.c_float)
    ]

    def __init__(self):
        BaseCommand.__init__(self)
        self.command_id = CommandID.convert_command_id_to_int(CommandID.ERemoteSetBolusParameter)
        self.sequence_id = 0
        self.direction = 0
        self.product_id = PRODUCT_ID

    # def fill_parameter(self, start_or_stop=1):
    #     self.is_start = start_or_stop

    def copy(self, cmd):
        # self.bolus_rate = cmd.bolus_rate
        # self.bolus_volume = cmd.bolus_volume
        pass


class SystemStatus(Enum):
    """
    SystemStatus
    """
    EWaitPowerUpStatus = 0x00
    EPostStatus = 0x01
    EStopStatus = 0x02
    EPauseStatus = 0x03
    ERunStatus = 0x04
    EPowerOffStatus = 0x05
    ENoneStatus = 0xFF

    @classmethod
    def convert_int_to_status(cls, value):
        for name, member in SystemStatus.__members__.items():
            if member.value == value:
                return member
            else:
                continue
        return None

    @classmethod
    def convert_status_to_int(cls, value):
        for name, member in SystemStatus.__members__.items():
            if member == value:
                return member.value
            else:
                continue
        return None


def create_command(command_id):
    """
    create_command
    """
    cmd = None
    ecommand_id = CommandID.convert_int_to_command_id(command_id)
    if ecommand_id == CommandID.EGetSerialNumber:
        cmd = GetSerialNumber()
    elif ecommand_id == CommandID.ERollbackVolume:
        cmd = RollbackVolume()
    elif ecommand_id == CommandID.EForwardVolume:
        cmd = ForwardVolume()
    elif ecommand_id == CommandID.EStopMotor:
        cmd = StopMotor()
    elif ecommand_id == CommandID.EGetTitleHint:
        cmd = GetTitleHint()
    elif ecommand_id == CommandID.EGetKVO:
        cmd = GetKVO()
    elif ecommand_id == CommandID.EGetScreenValue:
        cmd = GetScreenValue()
    elif ecommand_id == CommandID.EGetCurrentMode:
        cmd = GetCurrentMode()
    elif ecommand_id == CommandID.EGetOcclusionLevel:
        cmd = GetOcclusionLevel()
    elif ecommand_id == CommandID.EGetInfusionMode:
        cmd = GetInfusionMode()
    elif ecommand_id == CommandID.EGetBrand:
        cmd = GetBrand()
    elif ecommand_id == CommandID.EGetDoseUnit:
        cmd = GetDoseUnit()
    elif ecommand_id == CommandID.EGetCurrentDrug:
        cmd = GetCurrentDrug()
    elif ecommand_id == CommandID.ESetOcclusionLevel:
        cmd = SetOcclusionLevel()
    elif ecommand_id == CommandID.ESetInfusionMode:
        cmd = SetInfusionMode()
    elif ecommand_id == CommandID.ESetBrand:
        cmd = SetBrand()
    elif ecommand_id == CommandID.ESetDoseUnit:
        cmd = SetDoseUnit()
    elif ecommand_id == CommandID.ESetKVO:
        cmd = SetKVO()
    elif ecommand_id == CommandID.ESetCurrentDrug:
        cmd = SetCurrentDrug()
    elif ecommand_id == CommandID.ESetCompleteInfusionAlarmTime:
        cmd = SetCompleteInfusionAlarmTime()
    elif ecommand_id == CommandID.EGetInfusionParameter:
        cmd = GetInfusionParameter()
    elif ecommand_id == CommandID.EGetPumpAlarm:
        cmd = GetPumpAlarm()
    elif ecommand_id == CommandID.EGetInfusingParasOfMode:
        cmd = GetInfusingParasOfMode()
    elif ecommand_id == CommandID.EResetPumpMode:
        cmd = ResetPumpMode()
    elif ecommand_id == CommandID.ESetInfusionParameter:
        cmd = SetInfusionParameter()
    elif ecommand_id == CommandID.ESetInfusingParameterOfMode:
        cmd = SetInfusingParameter()
    elif ecommand_id == CommandID.ERemoteStartStopInfusion:
        cmd = RemoteStartStopInfusion()
    elif ecommand_id == CommandID.EGetSystemStatus:
        cmd = GetSystemStatus()
    elif ecommand_id == CommandID.ESetBolusRate:
        cmd = SetBolusRate()
    else:
        cmd = None
        return cmd
    cmd.direction = 0
    cmd.product_id = PRODUCT_ID
    cmd.command_id = command_id
    return cmd


def get_system_status_string(pumpstatus):
    statuses = {SystemStatus.EWaitPowerUpStatus: "WaitPowerUp",
                SystemStatus.EPostStatus: "Post",
                SystemStatus.EStopStatus: "Stop",
                SystemStatus.EPauseStatus: "Pause",
                SystemStatus.ERunStatus: "Run",
                SystemStatus.EPowerOffStatus: "PowerOff",
                SystemStatus.ENoneStatus: "None"
                }

    return statuses[pumpstatus]
