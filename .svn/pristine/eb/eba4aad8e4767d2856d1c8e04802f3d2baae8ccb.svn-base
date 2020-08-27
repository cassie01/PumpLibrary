# -*-coding:utf-8 -*-

from ParserProtocol.struct_define import *


class BaseInvoker:
    """
    This class is used to call API of dynamic link library.
    """

    def __init__(self, dll_path):
        # Dynamic link library path
        # Note that the DLLs used here must match the python platform, such as 32-bit or 64 bit. Because essentially an EXE loads a DLL, it cannot cross platform.
        self.path = dll_path
        # Load dynamic link library and create objects
        # Loading DLL and fetching functions
        self.protocol_parser = ctypes.WinDLL(self.path)
        # After loading the DLL, the address of the exported function in the DLL can be obtained directly.
        # If the function address is obtained, the function call cannot be made. To make a correct function call, the parameter and return value type must be set
        # Initialize the function in the dll, must be called first.
        self.protocol_parser.InitHandlers()
        # Create command ID and structure mapping table
        self.dict_command_id_structure = {}
        # A dictionary defining the length of various command byte arrays
        self.dict_command_bytes_buffer_length = {}
        # Initialization command ID and corresponding structure dictionary
        self.__init_dict()

        '''EmptyBuffer'''
        self.func_empty_buffer = self.protocol_parser.EmptyBuffer

        '''GetCommandID'''
        self.func_get_command_id = self.protocol_parser.GetCommandID
        self.func_get_command_id.restype = ctypes.c_int

        '''GetCommandData'''
        self.func_get_command_data = self.protocol_parser.GetCommandData
        self.func_get_command_data.restype = ctypes.c_int
        self.func_get_command_data.argtypes = [ctypes.c_ushort, ctypes.c_void_p]

        '''GetKVOCommandBytes of DLL'''
        self.func_get_kvo_bytes = self.protocol_parser.GetKVOCommandBytes
        self.func_get_kvo_bytes.restype = ctypes.c_int
        self.func_get_kvo_bytes.argtypes = [ctypes.c_byte, ctypes.c_byte, ctypes.c_ushort,
                                            ctypes.c_byte * self.dict_command_bytes_buffer_length[
                                                CommandID.EGetKVO]]

        '''GetSerialNumberCommandBytes of DLL'''
        self.func_get_serial_number_bytes = self.protocol_parser.GetSerialNumberCommandBytes
        self.func_get_serial_number_bytes.restype = ctypes.c_int
        self.func_get_serial_number_bytes.argtypes = [ctypes.c_byte, ctypes.c_byte, ctypes.c_ushort,
                                                      ctypes.c_byte * self.dict_command_bytes_buffer_length[
                                                          CommandID.EGetSerialNumber]]

        '''TAARollbackVolumeCommandBytes of DLL'''
        self.func_rollback_volume_bytes = self.protocol_parser.TAARollbackVolumeCommandBytes
        self.func_rollback_volume_bytes.restype = ctypes.c_int
        self.func_rollback_volume_bytes.argtypes = [ctypes.c_byte, ctypes.c_byte, ctypes.c_uint32, ctypes.c_ushort,
                                                    ctypes.c_byte * self.dict_command_bytes_buffer_length[
                                                        CommandID.ERollbackVolume]]

        '''TAASetForwardVolumeCommandBytes of DLL'''
        self.func_forward_volume_bytes = self.protocol_parser.TAASetForwardVolumeCommandBytes
        self.func_forward_volume_bytes.restype = ctypes.c_int
        self.func_forward_volume_bytes.argtypes = [ctypes.c_byte, ctypes.c_byte, ctypes.c_uint32, ctypes.c_ushort,
                                                   ctypes.c_byte * self.dict_command_bytes_buffer_length[
                                                       CommandID.EForwardVolume]]

        '''TAAStopMotorCommandBytes of DLL'''
        self.func_stop_motor_bytes = self.protocol_parser.TAAStopMotorCommandBytes
        self.func_stop_motor_bytes.restype = ctypes.c_int
        self.func_stop_motor_bytes.argtypes = [ctypes.c_byte, ctypes.c_byte, ctypes.c_ushort,
                                               ctypes.c_byte * self.dict_command_bytes_buffer_length[
                                                   CommandID.EStopMotor]]

        '''GetTitleHintCommandBytes of DLL'''
        self.func_get_title_hint_bytes = self.protocol_parser.TAAGetTitleHintCommandBytes
        self.func_get_title_hint_bytes.restype = ctypes.c_int
        self.func_get_title_hint_bytes.argtypes = [ctypes.c_byte, ctypes.c_byte, ctypes.c_byte, ctypes.c_ushort,
                                                   ctypes.c_byte * self.dict_command_bytes_buffer_length[
                                                       CommandID.EGetTitleHint]]

        '''TAAGetScreenValueCommandBytes of DLL'''
        self.func_get_screen_value_bytes = self.protocol_parser.TAAGetScreenValueCommandBytes
        self.func_get_screen_value_bytes.restype = ctypes.c_int
        self.func_get_screen_value_bytes.argtypes = [ctypes.c_byte, ctypes.c_byte, ctypes.c_byte, ctypes.c_byte,
                                                     ctypes.c_byte, ctypes.c_ushort,
                                                     ctypes.c_byte * self.dict_command_bytes_buffer_length[
                                                         CommandID.EGetTitleHint]]

        '''GetCurrentModeCommandBytes of DLL'''
        self.func_get_current_mode_bytes = self.protocol_parser.GetCurrentModeCommandBytes
        self.func_get_current_mode_bytes.restype = ctypes.c_int
        self.func_get_current_mode_bytes.argtypes = [ctypes.c_byte, ctypes.c_byte, ctypes.c_ushort,
                                                     ctypes.c_byte * self.dict_command_bytes_buffer_length[
                                                         CommandID.EGetCurrentMode]]

        '''GetOcclusionLevelCommandBytes of DLL'''
        self.func_get_occlusion_level_bytes = self.protocol_parser.GetOcclusionLevelCommandBytes
        self.func_get_occlusion_level_bytes.restype = ctypes.c_int
        self.func_get_occlusion_level_bytes.argtypes = [ctypes.c_byte, ctypes.c_byte, ctypes.c_ushort,
                                                        ctypes.c_byte * self.dict_command_bytes_buffer_length[
                                                            CommandID.EGetOcclusionLevel]]

        '''GetInfusionModeCommandBytes of DLL'''
        self.func_get_infusion_mode_bytes = self.protocol_parser.GetInfusionModeCommandBytes
        self.func_get_infusion_mode_bytes.restype = ctypes.c_int
        self.func_get_infusion_mode_bytes.argtypes = [ctypes.c_byte, ctypes.c_byte, ctypes.c_ushort,
                                                      ctypes.c_byte * self.dict_command_bytes_buffer_length[
                                                          CommandID.EGetInfusionMode]]

        '''GetSyringeBrandCommandBytes of DLL'''
        self.func_get_syringe_brand_bytes = self.protocol_parser.GetSyringeBrandCommandBytes
        self.func_get_syringe_brand_bytes.restype = ctypes.c_int
        self.func_get_syringe_brand_bytes.argtypes = [ctypes.c_byte, ctypes.c_byte, ctypes.c_ushort,
                                                      ctypes.c_byte * self.dict_command_bytes_buffer_length[
                                                          CommandID.EGetBrand]]

        '''GetDoseUnitCommandBytes of DLL'''
        self.func_get_dose_uint_bytes = self.protocol_parser.GetDoseUnitCommandBytes
        self.func_get_dose_uint_bytes.restype = ctypes.c_int
        self.func_get_dose_uint_bytes.argtypes = [ctypes.c_byte, ctypes.c_byte, ctypes.c_ushort,
                                                  ctypes.c_byte * self.dict_command_bytes_buffer_length[
                                                      CommandID.EGetDoseUnit]]

        '''GetDrugMassUnitCommandBytes of DLL'''
        self.func_get_drug_mass_uint_bytes = self.protocol_parser.GetDrugMassUnitCommandBytes
        self.func_get_drug_mass_uint_bytes.restype = ctypes.c_int
        self.func_get_drug_mass_uint_bytes.argtypes = [ctypes.c_byte, ctypes.c_byte, ctypes.c_ushort,
                                                       ctypes.c_byte * self.dict_command_bytes_buffer_length[
                                                           CommandID.EGetDrugMassUnit]]

        '''GetBasicModeRateUnitCommandBytes of DLL'''
        self.func_get_basic_mode_rate_uint_bytes = self.protocol_parser.GetBasicModeRateUnitCommandBytes
        self.func_get_basic_mode_rate_uint_bytes.restype = ctypes.c_int
        self.func_get_basic_mode_rate_uint_bytes.argtypes = [ctypes.c_byte, ctypes.c_byte, ctypes.c_ushort,
                                                             ctypes.c_byte * self.dict_command_bytes_buffer_length[
                                                                 CommandID.EGetBasicModeRateUnit]]

        '''GetCurrentDrugCommandBytes of DLL'''
        self.func_get_current_drug_bytes = self.protocol_parser.GetCurrentDrugCommandBytes
        self.func_get_current_drug_bytes.restype = ctypes.c_int
        self.func_get_current_drug_bytes.argtypes = [ctypes.c_byte, ctypes.c_byte, ctypes.c_ushort,
                                                     ctypes.c_byte * self.dict_command_bytes_buffer_length[
                                                         CommandID.EGetCurrentDrug]]

        '''SetOcclusionLevelCommandBytes of DLL'''
        self.func_set_occlusion_level_bytes = self.protocol_parser.SetOcclusionLevelCommandBytes
        self.func_set_occlusion_level_bytes.restype = ctypes.c_int
        self.func_set_occlusion_level_bytes.argtypes = [ctypes.c_byte, ctypes.c_byte, ctypes.c_byte, ctypes.c_ushort,
                                                        ctypes.c_byte * self.dict_command_bytes_buffer_length[
                                                            CommandID.ESetOcclusionLevel]]

        '''SetInfusionModeCommandBytes of DLL'''
        self.func_set_infusion_mode_bytes = self.protocol_parser.SetInfusionModeCommandBytes
        self.func_set_infusion_mode_bytes.restype = ctypes.c_int
        self.func_set_infusion_mode_bytes.argtypes = [ctypes.c_byte, ctypes.c_byte, ctypes.c_byte, ctypes.c_ushort,
                                                      ctypes.c_byte * self.dict_command_bytes_buffer_length[
                                                          CommandID.ESetInfusionMode]]

        '''SetSyringeBrandCommandBytes of DLL'''
        self.func_set_syringe_brand_bytes = self.protocol_parser.SetSyringeBrandCommandBytes
        self.func_set_syringe_brand_bytes.restype = ctypes.c_int
        self.func_set_syringe_brand_bytes.argtypes = [ctypes.c_byte, ctypes.c_byte, ctypes.c_byte, ctypes.c_ushort,
                                                      ctypes.c_byte * self.dict_command_bytes_buffer_length[
                                                          CommandID.ESetBrand]]

        '''SetDoseUnitCommandBytes of DLL'''
        self.func_set_dose_unit_bytes = self.protocol_parser.SetDoseUnitCommandBytes
        self.func_set_dose_unit_bytes.restype = ctypes.c_int
        self.func_set_dose_unit_bytes.argtypes = [ctypes.c_byte, ctypes.c_byte, ctypes.c_byte, ctypes.c_ushort,
                                                  ctypes.c_byte * self.dict_command_bytes_buffer_length[
                                                      CommandID.ESetDoseUnit]]

        '''SetDrugMassUnitCommandBytes of DLL'''
        self.func_set_drug_mass_unit_bytes = self.protocol_parser.SetDrugMassUnitCommandBytes
        self.func_set_drug_mass_unit_bytes.restype = ctypes.c_int
        self.func_set_drug_mass_unit_bytes.argtypes = [ctypes.c_byte, ctypes.c_byte, ctypes.c_byte, ctypes.c_ushort,
                                                       ctypes.c_byte * self.dict_command_bytes_buffer_length[
                                                           CommandID.ESetDoseUnit]]

        '''SetWeightUnitCommandBytes of DLL'''
        self.func_set_weight_unit_bytes = self.protocol_parser.SetWeightUnitCommandBytes
        self.func_set_weight_unit_bytes.restype = ctypes.c_int
        self.func_set_weight_unit_bytes.argtypes = [ctypes.c_byte, ctypes.c_byte, ctypes.c_byte, ctypes.c_ushort,
                                                    ctypes.c_byte * self.dict_command_bytes_buffer_length[
                                                        CommandID.ESetDoseUnit]]

        '''SetBasicModeRateUnitCommandBytes of DLL'''
        self.func_set_basic_mode_rate_unit_bytes = self.protocol_parser.SetBasicModeRateUnitCommandBytes
        self.func_set_basic_mode_rate_unit_bytes.restype = ctypes.c_int
        self.func_set_basic_mode_rate_unit_bytes.argtypes = [ctypes.c_byte, ctypes.c_byte, ctypes.c_byte,
                                                             ctypes.c_ushort,
                                                             ctypes.c_byte * self.dict_command_bytes_buffer_length[
                                                                 CommandID.ESetBasicModeRateUnit]]

        '''SetKVOCommandBytes of DLL'''
        self.func_set_kvo_bytes = self.protocol_parser.SetKVOCommandBytes
        self.func_set_kvo_bytes.restype = ctypes.c_int
        self.func_set_kvo_bytes.argtypes = [ctypes.c_byte, ctypes.c_byte, ctypes.c_float, ctypes.c_ushort,
                                            ctypes.c_byte * self.dict_command_bytes_buffer_length[CommandID.ESetKVO]]

        '''SetCurrentDrugCommandBytes of DLL'''
        self.func_set_current_drug_bytes = self.protocol_parser.SetCurrentDrugCommandBytes
        self.func_set_current_drug_bytes.restype = ctypes.c_int
        self.func_set_current_drug_bytes.argtypes = [ctypes.c_byte, ctypes.c_byte, ctypes.c_ushort, ctypes.c_ushort,
                                                     ctypes.c_byte * self.dict_command_bytes_buffer_length[
                                                         CommandID.ESetCurrentDrug]]

        '''SetCompleteInfusionAlarmTimeCommandBytes of DLL'''
        self.func_set_complete_infusion_alarm_time_bytes = self.protocol_parser.SetCompleteInfusionAlarmTimeCommandBytes
        self.func_set_complete_infusion_alarm_time_bytes.restype = ctypes.c_int
        self.func_set_complete_infusion_alarm_time_bytes.argtypes = [ctypes.c_byte, ctypes.c_byte, ctypes.c_byte,
                                                                     ctypes.c_ushort,
                                                                     ctypes.c_byte *
                                                                     self.dict_command_bytes_buffer_length[
                                                                         CommandID.ESetCompleteInfusionAlarmTime]]

        '''GetInfusionParameterCommandBytes of DLL'''
        self.func_get_infusion_parameter_bytes = self.protocol_parser.GetInfusionParameterCommandBytes
        self.func_get_infusion_parameter_bytes.restype = ctypes.c_int
        self.func_get_infusion_parameter_bytes.argtypes = [ctypes.c_byte, ctypes.c_byte, ctypes.c_ushort,
                                                           ctypes.c_byte * self.dict_command_bytes_buffer_length[
                                                               CommandID.EGetInfusionParameter]]

        '''GetPumpAlarmCommandBytes of DLL'''
        self.func_get_pump_alarm_bytes = self.protocol_parser.GetPumpAlarmCommandBytes
        self.func_get_pump_alarm_bytes.restype = ctypes.c_int
        self.func_get_pump_alarm_bytes.argtypes = [ctypes.c_byte, ctypes.c_byte, ctypes.c_ushort,
                                                   ctypes.c_byte * self.dict_command_bytes_buffer_length[
                                                       CommandID.EGetPumpAlarm]]

        '''GetInfusingParameterOfModeCommandBytes of DLL'''
        self.func_get_infusing_parameter_of_mode_bytes = self.protocol_parser.GetInfusingParameterOfModeCommandBytes
        self.func_get_infusing_parameter_of_mode_bytes.restype = ctypes.c_int
        self.func_get_infusing_parameter_of_mode_bytes.argtypes = [ctypes.c_byte, ctypes.c_byte, ctypes.c_ushort,
                                                                   ctypes.c_byte *
                                                                   self.dict_command_bytes_buffer_length[
                                                                       CommandID.EGetInfusingParasOfMode]]

        '''ResetPumpCommandBytes of DLL'''
        self.func_reset_pump_mode_bytes = self.protocol_parser.ResetPumpCommandBytes
        self.func_reset_pump_mode_bytes.restype = ctypes.c_int
        self.func_reset_pump_mode_bytes.argtypes = [ctypes.c_byte, ctypes.c_byte, ctypes.c_byte, ctypes.c_ushort,
                                                    ctypes.c_byte * self.dict_command_bytes_buffer_length[
                                                        CommandID.EResetPumpMode]]

        '''SendFileStartCommandBytes of DLL'''
        self.func_send_file_start_bytes = self.protocol_parser.SendFileStartCommandBytes
        self.func_send_file_start_bytes.restype = ctypes.c_int
        self.func_send_file_start_bytes.argtypes = [ctypes.c_byte, ctypes.c_byte, ctypes.c_byte, ctypes.c_byte,
                                                    ctypes.c_uint32, ctypes.c_uint32, ctypes.c_ushort, ctypes.c_ushort,
                                                    ctypes.c_byte * self.dict_command_bytes_buffer_length[
                                                        CommandID.ESendFileStart]]

        '''SendFilePackageCommandBytes of DLL'''
        self.func_send_file_package_bytes = self.protocol_parser.SendFilePackageCommandBytes
        self.func_send_file_package_bytes.restype = ctypes.c_int

        '''SendFileCompletedCommandBytes of DLL'''
        self.func_send_file_complete_bytes = self.protocol_parser.SendFileCompletedCommandBytes
        self.func_send_file_complete_bytes.restype = ctypes.c_int
        self.func_send_file_complete_bytes.argtypes = [ctypes.c_byte, ctypes.c_byte, ctypes.c_byte, ctypes.c_byte,
                                                       ctypes.c_byte, ctypes.c_ushort,
                                                       ctypes.c_byte * self.dict_command_bytes_buffer_length[
                                                           CommandID.ESendFileCompleted]]

        '''SetInfusionParameterCommandBytes of DLL'''
        self.func_set_infusion_parameter_bytes = self.protocol_parser.SetInfusionParameterCommandBytes
        self.func_set_infusion_parameter_bytes.restype = ctypes.c_int
        # self.func_set_infusion_parameter_bytes.restype = ctypes.c_long
        self.func_set_infusion_parameter_bytes.argtypes = [ctypes.c_byte, ctypes.c_byte, StructInfusionParameter,
                                                           ctypes.c_ushort,
                                                           ctypes.c_byte * self.dict_command_bytes_buffer_length[
                                                               CommandID.ESetInfusionParameter]]

        '''SetInfusingParameterOfModeCommandBytes of DLL'''
        self.func_set_infusing_parameter_bytes = self.protocol_parser.SetInfusingParameterOfModeCommandBytes
        self.func_set_infusing_parameter_bytes.restype = ctypes.c_int

        '''RemoteStartstopInfusionCommandBytes of DLL'''
        self.func_remote_start_stop_infusion_bytes = self.protocol_parser.RemoteStartstopInfusionCommandBytes
        self.func_remote_start_stop_infusion_bytes.restype = ctypes.c_int
        self.func_remote_start_stop_infusion_bytes.argtypes = [ctypes.c_byte, ctypes.c_byte, ctypes.c_byte,
                                                               ctypes.c_ushort,
                                                               ctypes.c_byte * self.dict_command_bytes_buffer_length[
                                                                   CommandID.ERemoteStartStopInfusion]]

        '''GetSystemStatusCommandBytes of DLL'''
        self.func_get_system_status_bytes = self.protocol_parser.GetSystemStatusCommandBytes
        self.func_get_system_status_bytes.restype = ctypes.c_int
        self.func_get_system_status_bytes.argtypes = [ctypes.c_byte, ctypes.c_byte, ctypes.c_ushort,
                                                      ctypes.c_byte * self.dict_command_bytes_buffer_length[
                                                          CommandID.EGetSystemStatus]]

        """SetAlarmSoundTypeCommandBytes of DLL"""
        self.func_set_alarm_sound_type_bytes = self.protocol_parser.SetAlarmSoundTypeCommandBytes
        self.func_set_alarm_sound_type_bytes.retypes = ctypes.c_int
        self.func_set_alarm_sound_type_bytes.argtypes = [ctypes.c_byte, ctypes.c_byte, ctypes.c_byte, ctypes.c_ushort,
                                                         ctypes.c_byte * self.dict_command_bytes_buffer_length[
                                                             CommandID.ESetAlarmSoundType]]

        """GetAlarmSoundTypeCommandBytes of DLL"""
        self.func_get_alarm_sound_type_bytes = self.protocol_parser.GetAlarmSoundTypeCommandBytes
        self.func_get_alarm_sound_type_bytes.retypes = ctypes.c_int
        self.func_get_alarm_sound_type_bytes.argtypes = [ctypes.c_byte, ctypes.c_byte, ctypes.c_ushort,
                                                         ctypes.c_byte * self.dict_command_bytes_buffer_length[
                                                             CommandID.EGetAlarmSoundType]]

        """SetAlarmVolumeCommandBytes of DLL"""
        self.func_set_alarm_volume_bytes = self.protocol_parser.SetAlarmVolumeCommandBytes
        self.func_set_alarm_volume_bytes.retypes = ctypes.c_int
        self.func_set_alarm_volume_bytes.argtypes = [ctypes.c_byte, ctypes.c_byte, ctypes.c_byte, ctypes.c_ushort,
                                                     ctypes.c_byte * self.dict_command_bytes_buffer_length[
                                                         CommandID.ESetAlarmVolume]]

        """GetAlarmVolumeCommandBytes of DLL"""
        self.func_get_alarm_volume_bytes = self.protocol_parser.GetAlarmVolumeCommandBytes
        self.func_get_alarm_volume_bytes.retypes = ctypes.c_int
        self.func_get_alarm_volume_bytes.argtypes = [ctypes.c_byte, ctypes.c_byte, ctypes.c_ushort,
                                                     ctypes.c_byte * self.dict_command_bytes_buffer_length[
                                                         CommandID.EGetAlarmVolume]]

        """GetProductIDCommandBytes of DLL"""
        self.func_get_productID_bytes = self.protocol_parser.GetProductIDCommandBytes
        self.func_get_productID_bytes.retypes = ctypes.c_int
        self.func_get_productID_bytes.argtypes = [ctypes.c_byte, ctypes.c_byte, ctypes.c_ushort,
                                                  ctypes.c_byte * self.dict_command_bytes_buffer_length[
                                                      CommandID.EGetProductID]]

        """GetFirmwareVersionCommandBytes of DLL"""
        self.func_get_firmware_version_bytes = self.protocol_parser.GetFirmwareVersionCommandBytes
        self.func_get_firmware_version_bytes.retypes = ctypes.c_int
        self.func_get_firmware_version_bytes.argtypes = [ctypes.c_byte, ctypes.c_byte, ctypes.c_ushort,
                                                         ctypes.c_byte * self.dict_command_bytes_buffer_length[
                                                             CommandID.EGetFirmwareVersion]]

        """GetFirmwareDataVersionCommandBytes of DLL"""
        self.func_get_firmware_data_version_bytes = self.protocol_parser.GetFirmwareDataVersionCommandBytes
        self.func_get_firmware_data_version_bytes.retypes = ctypes.c_int
        self.func_get_firmware_data_version_bytes.argtypes = [ctypes.c_byte, ctypes.c_byte, ctypes.c_byte,
                                                              ctypes.c_ushort,
                                                              ctypes.c_byte * self.dict_command_bytes_buffer_length[
                                                                  CommandID.EGetFactoryFirmwareVersion]]

        """GetSupportedMaxFileSizeCommandBytes of DLL"""
        self.func_get_supported_max_file_size_bytes = self.protocol_parser.GetSupportedMaxFileSizeCommandBytes
        self.func_get_supported_max_file_size_bytes.retypes = ctypes.c_int
        self.func_get_supported_max_file_size_bytes.argtypes = [ctypes.c_int, ctypes.c_int, ctypes.c_int,
                                                                ctypes.c_ushort,
                                                                ctypes.c_byte * self.dict_command_bytes_buffer_length[
                                                                    CommandID.EGetFirmwareVersion]]

        """GetMaintenanceDateTimeCommandBytes of DLL"""
        self.func_get_maintenance_date_time_bytes = self.protocol_parser.GetMaintenanceDateTimeCommandBytes
        self.func_get_maintenance_date_time_bytes.retypes = ctypes.c_int
        self.func_get_maintenance_date_time_bytes.argtypes = [ctypes.c_byte, ctypes.c_byte, ctypes.c_ushort,
                                                              ctypes.c_byte * self.dict_command_bytes_buffer_length[
                                                                  CommandID.EGetMaintenanceDateTime]]

        """GetMaintenancePeriodCommandBytes of DLL"""
        self.func_get_maintenance_period_bytes = self.protocol_parser.GetMaintenancePeriodCommandBytes
        self.func_get_maintenance_period_bytes.retypes = ctypes.c_int
        self.func_get_maintenance_period_bytes.argtypes = [ctypes.c_byte, ctypes.c_byte, ctypes.c_ushort,
                                                           ctypes.c_byte * self.dict_command_bytes_buffer_length[
                                                               CommandID.EGetMaintenancePeriod]]

        """GetBatteryAlarmDurationCommandBytes of DLL"""
        self.func_get_battery_alarm_duration_bytes = self.protocol_parser.GetBatteryAlarmDurationCommandBytes
        self.func_get_battery_alarm_duration_bytes.retypes = ctypes.c_int
        self.func_get_battery_alarm_duration_bytes.argtypes = [ctypes.c_int, ctypes.c_int, ctypes.c_ushort,
                                                               ctypes.c_byte * self.dict_command_bytes_buffer_length[
                                                                   CommandID.EGetBatteryAlarmDuration]]

        """"WriteLogCommandBytes of DLL"""
        self.func_write_log_bytes = self.protocol_parser.WriteLogCommandBytes
        self.func_write_log_bytes.retypes = ctypes.c_int
        self.func_write_log_bytes.argtypes = [ctypes.c_byte, ctypes.c_byte, ctypes.c_int, ctypes.c_ushort,
                                              ctypes.c_byte * self.dict_command_bytes_buffer_length[
                                                  CommandID.EWriteLog]]

        """GetAlarmTypePasswordCommandBytes of DLL"""
        self.func_get_alarm_type_password_bytes = self.protocol_parser.GetAlarmTypePasswordCommandBytes
        self.func_get_alarm_type_password_bytes.retypes = ctypes.c_int
        self.func_get_alarm_type_password_bytes.argtypes = [ctypes.c_byte, ctypes.c_byte, ctypes.c_ushort,
                                                            ctypes.c_byte * self.dict_command_bytes_buffer_length[
                                                                CommandID.EGetAlarmTypePassword]]

        """GetAlarmNameCommandBytes of DLL"""
        self.func_get_alarm_name_bytes = self.protocol_parser.GetAlarmNameCommandBytes
        self.func_get_alarm_name_bytes.retypes = ctypes.c_int
        self.func_get_alarm_name_bytes.argtypes = [ctypes.c_byte, ctypes.c_byte, ctypes.c_byte, ctypes.c_ushort,
                                                   ctypes.c_byte * self.dict_command_bytes_buffer_length[
                                                       CommandID.EGetAlarmName]]

        """GetAlarmCountCommandBytes of DLL"""
        self.func_get_alarm_count_bytes = self.protocol_parser.GetAlarmCountCommandBytes
        self.func_get_alarm_count_bytes.retypes = ctypes.c_int
        self.func_get_alarm_count_bytes.argtypes = [ctypes.c_byte, ctypes.c_byte, ctypes.c_ushort,
                                                    ctypes.c_byte * self.dict_command_bytes_buffer_length[
                                                        CommandID.EGetAlarmCount]]

        """GetDateTimeCommandBytes of DLL"""
        self.func_get_date_time_bytes = self.protocol_parser.GetDateTimeCommandBytes
        self.func_get_date_time_bytes.retypes = ctypes.c_int
        self.func_get_date_time_bytes.argtypes = [ctypes.c_byte, ctypes.c_byte, ctypes.c_ushort,
                                                  ctypes.c_byte * self.dict_command_bytes_buffer_length[
                                                      CommandID.EGetDateTime]]

        """SetDateTimeCommandBytes of DLL"""
        self.func_set_date_time_bytes = self.protocol_parser.SetDateTimeCommandBytes
        self.func_set_date_time_bytes.retypes = ctypes.c_int
        self.func_set_date_time_bytes.argtypes = [ctypes.c_byte, ctypes.c_byte, ctypes.c_ushort,
                                                  ctypes.c_byte, ctypes.c_byte, ctypes.c_byte,
                                                  ctypes.c_byte, ctypes.c_byte, ctypes.c_ushort,
                                                  ctypes.c_byte * self.dict_command_bytes_buffer_length[
                                                      CommandID.ESetDateTime]]

        """SetBrightnessCommandBytes of DLL"""
        self.func_set_brightness_bytes = self.protocol_parser.SetBrightnessCommandBytes
        self.func_set_brightness_bytes.retypes = ctypes.c_int
        self.func_set_brightness_bytes.argtypes = [ctypes.c_byte, ctypes.c_byte, ctypes.c_byte, ctypes.c_ushort,
                                                   ctypes.c_byte * self.dict_command_bytes_buffer_length[
                                                       CommandID.ESetBrightness]]
        """GetBrightnessCommandBytes of DLL"""
        self.func_get_brightness_bytes = self.protocol_parser.GetBrightnessCommandBytes
        self.func_get_brightness_bytes.retypes = ctypes.c_int
        self.func_get_brightness_bytes.argtypes = [ctypes.c_byte, ctypes.c_byte, ctypes.c_ushort,
                                                   ctypes.c_byte * self.dict_command_bytes_buffer_length[
                                                       CommandID.EGetBrightness]]

        """SetNightModePeriodCommandBytes of DLL"""
        self.func_set_night_mode_period_bytes = self.protocol_parser.SetNightModePeriodCommandBytes
        self.func_set_night_mode_period_bytes.retypes = ctypes.c_int
        self.func_set_night_mode_period_bytes.argtypes = [ctypes.c_byte, ctypes.c_byte, ctypes.c_byte, ctypes.c_byte,
                                                          ctypes.c_byte, ctypes.c_byte, ctypes.c_ushort,
                                                          ctypes.c_byte * self.dict_command_bytes_buffer_length[
                                                              CommandID.ESetNightModePeriod]]

        """GetNightModePeriodCommandBytes of DLL"""
        self.func_get_night_mode_period_bytes = self.protocol_parser.GetNightModePeriodCommandBytes
        self.func_get_night_mode_period_bytes.retypes = ctypes.c_int
        self.func_get_night_mode_period_bytes.argtypes = [ctypes.c_byte, ctypes.c_byte, ctypes.c_ushort,
                                                          ctypes.c_byte * self.dict_command_bytes_buffer_length[
                                                              CommandID.EGetNightModePeriod]]

        """SetNightModeAlarmVolumeCommandBytes of DLL"""
        self.func_set_night_mode_alarm_volume_bytes = self.protocol_parser.SetNightModeAlarmVolumeCommandBytes
        self.func_set_night_mode_alarm_volume_bytes.retypes = ctypes.c_int
        self.func_set_night_mode_alarm_volume_bytes.argtypes = [ctypes.c_byte, ctypes.c_byte, ctypes.c_byte,
                                                                ctypes.c_ushort,
                                                                ctypes.c_byte * self.dict_command_bytes_buffer_length[
                                                                    CommandID.ESetNightModeAlarmVolume]]

        """GetNightModeAlarmVolumeCommandBytes of DLL"""
        self.func_get_night_mode_alarm_volume_bytes = self.protocol_parser.GetNightModeAlarmVolumeCommandBytes
        self.func_get_night_mode_alarm_volume_bytes.retypes = ctypes.c_int
        self.func_get_night_mode_alarm_volume_bytes.argtypes = [ctypes.c_byte, ctypes.c_byte, ctypes.c_ushort,
                                                                ctypes.c_byte * self.dict_command_bytes_buffer_length[
                                                                    CommandID.EGetNightModeAlarmVolume]]

        """SetNightModeBrightnessCommandBytes of DLL"""
        self.func_set_night_mode_brightness_bytes = self.protocol_parser.SetNightModeBrightnessCommandBytes
        self.func_set_night_mode_brightness_bytes.retypes = ctypes.c_int
        self.func_set_night_mode_brightness_bytes.argtypes = [ctypes.c_byte, ctypes.c_byte, ctypes.c_byte,
                                                              ctypes.c_ushort,
                                                              ctypes.c_byte * self.dict_command_bytes_buffer_length[
                                                                  CommandID.ESetNightModeBrightness]]
        """GetNightModeBrightnessCommandBytes of DLL"""
        self.func_get_night_mode_brightness_bytes = self.protocol_parser.GetNightModeBrightnessCommandBytes
        self.func_get_night_mode_brightness_bytes.retypes = ctypes.c_int
        self.func_get_night_mode_brightness_bytes.argtypes = [ctypes.c_byte, ctypes.c_byte,
                                                              ctypes.c_ushort,
                                                              ctypes.c_byte * self.dict_command_bytes_buffer_length[
                                                                  CommandID.EGetNightModeBrightness]]

        """SetSecuritySwitchCommandBytes of DLL"""
        self.func_set_security_switch_bytes = self.protocol_parser.SetSecuritySwitchCommandBytes
        self.func_set_security_switch_bytes.retypes = ctypes.c_int
        self.func_set_security_switch_bytes.argtypes = [ctypes.c_byte, ctypes.c_byte, ctypes.c_int, ctypes.c_int,
                                                        ctypes.c_ushort,
                                                        ctypes.c_byte * self.dict_command_bytes_buffer_length[
                                                            CommandID.ESetSecuritySwitch]]

        """GetSecuritySwitchCommandBytes of DLL"""
        self.func_get_security_switch_bytes = self.protocol_parser.GetSecuritySwitchCommandBytes
        self.func_get_security_switch_bytes.retypes = ctypes.c_int
        self.func_get_security_switch_bytes.argtypes = [ctypes.c_byte, ctypes.c_byte, ctypes.c_int,
                                                        ctypes.c_ushort,
                                                        ctypes.c_byte * self.dict_command_bytes_buffer_length[
                                                            CommandID.EGetSecuritySwitch]]

        """ClearHistoryLogCommandBytes of DLL"""
        self.func_clear_history_log_bytes = self.protocol_parser.ClearHistoryLogCommandBytes
        self.func_clear_history_log_bytes.retypes = ctypes.c_int
        self.func_clear_history_log_bytes.argtypes = [ctypes.c_byte, ctypes.c_byte,
                                                      ctypes.c_ushort,
                                                      ctypes.c_byte * self.dict_command_bytes_buffer_length[
                                                          CommandID.EClearHistoryLog]]
        """GetLogTotalNumCommandBytes of DLL"""
        self.func_get_log_total_num_bytes = self.protocol_parser.GetLogTotalNumCommandBytes
        self.func_get_log_total_num_bytes.retypes = ctypes.c_int
        self.func_get_log_total_num_bytes.argtypes = [ctypes.c_byte, ctypes.c_byte,
                                                      ctypes.c_ushort,
                                                      ctypes.c_byte * self.dict_command_bytes_buffer_length[
                                                          CommandID.EGetLogTotalNum]]

        """GetLogCommandBytes of DLL"""
        self.func_get_log_bytes = self.protocol_parser.GetLogCommandBytes
        self.func_get_log_bytes.retypes = ctypes.c_int
        self.func_get_log_bytes.argtypes = [ctypes.c_byte, ctypes.c_byte, ctypes.c_int,
                                            ctypes.c_ushort,
                                            ctypes.c_byte * self.dict_command_bytes_buffer_length[
                                                CommandID.EGetLogItem]]

        """RestoreFactorySettingCommandBytes of DLL"""
        self.func_restore_factory_setting_bytes = self.protocol_parser.RestoreFactorySettingCommandBytes
        self.func_restore_factory_setting_bytes.retypes = ctypes.c_int
        self.func_restore_factory_setting_bytes.argtypes = [ctypes.c_byte, ctypes.c_byte,
                                                            ctypes.c_ushort,
                                                            ctypes.c_byte * self.dict_command_bytes_buffer_length[
                                                                CommandID.ERestoreFactorySetting]]

        """RestoreFactorySettingCommandBytes of DLL"""
        self.func_get_lock_password_bytes = self.protocol_parser.GetSecuritySettingLockPasswordCommandBytes
        self.func_get_lock_password_bytes.retypes = ctypes.c_int
        self.func_get_lock_password_bytes.argtypes = [ctypes.c_byte, ctypes.c_byte,
                                                      ctypes.c_ushort,
                                                      ctypes.c_byte * self.dict_command_bytes_buffer_length[
                                                          CommandID.EGetLockPassword]]

        """SetTubePrecisionCalibrationBrandCommandBytes of DLL"""
        self.func_set_tube_precision_calibration_brand_bytes = self.protocol_parser.SetTubePrecisionCalibrationBrandCommandBytes
        self.func_set_tube_precision_calibration_brand_bytes.retypes = ctypes.c_int
        self.func_set_tube_precision_calibration_brand_bytes.argtypes = [ctypes.c_byte, ctypes.c_byte, ctypes.c_byte,
                                                                         ctypes.c_ushort,
                                                                         ctypes.c_byte *
                                                                         self.dict_command_bytes_buffer_length[
                                                                             CommandID.ESetTubePrecisionCalibrationBrand]]

        """SetTubePrecisionCalibrationParameterCommandBytes of DLL"""
        self.func_set_tube_precision_calibration_parameter_bytes = self.protocol_parser.SetTubePrecisionCalibrationParameterCommandBytes
        self.func_set_tube_precision_calibration_parameter_bytes.retypes = ctypes.c_int
        self.func_set_tube_precision_calibration_parameter_bytes.argtypes = [ctypes.c_byte, ctypes.c_byte,
                                                                             ctypes.c_byte, ctypes.c_float,
                                                                             ctypes.c_float,
                                                                             ctypes.c_ushort,
                                                                             ctypes.c_byte *
                                                                             self.dict_command_bytes_buffer_length[
                                                                                 CommandID.ESetTubePrecisionCalibrationParameter]]

        """GetInfusionNearCompleteCriteriaCommandBytes of DLL"""
        self.func_get_infusion_near_complete_criteria_bytes = self.protocol_parser.GetInfusionNearCompleteCriteriaCommandBytes
        self.func_get_infusion_near_complete_criteria_bytes.retypes = ctypes.c_int
        self.func_get_infusion_near_complete_criteria_bytes.argtypes = [ctypes.c_byte, ctypes.c_byte,
                                                                        ctypes.c_ushort,
                                                                        ctypes.c_byte *
                                                                        self.dict_command_bytes_buffer_length[
                                                                            CommandID.EGetInfusionNearCompleteCriteria]]

        """SetInfusionNearCompleteCriteriaCommandBytes of DLL"""
        self.func_set_infusion_near_complete_criteria_bytes = self.protocol_parser.SetInfusionNearCompleteCriteriaCommandBytes
        self.func_set_infusion_near_complete_criteria_bytes.retypes = ctypes.c_int
        self.func_set_infusion_near_complete_criteria_bytes.argtypes = [ctypes.c_byte, ctypes.c_byte, ctypes.c_byte,
                                                                        ctypes.c_int,
                                                                        ctypes.c_ushort,
                                                                        ctypes.c_byte *
                                                                        self.dict_command_bytes_buffer_length[
                                                                            CommandID.ESetInfusionNearCompleteCriteria]]
        """GetBubbleSensitivityCommandBytes of DLL"""
        self.func_get_bubble_sensitivity_bytes = self.protocol_parser.GetBubbleSensitivityCommandBytes
        self.func_get_bubble_sensitivity_bytes.retypes = ctypes.c_int
        self.func_get_bubble_sensitivity_bytes.argtypes = [ctypes.c_byte, ctypes.c_byte, ctypes.c_byte,
                                                           ctypes.c_ushort,
                                                           ctypes.c_byte *
                                                           self.dict_command_bytes_buffer_length[
                                                               CommandID.EGetBubbleSensitivity]]

        """SetBubbleSensitivityCommandBytes of DLL"""
        self.func_set_bubble_sensitivity_bytes = self.protocol_parser.SetBubbleSensitivityCommandBytes
        self.func_set_bubble_sensitivity_bytes.retypes = ctypes.c_int
        self.func_set_bubble_sensitivity_bytes.argtypes = [ctypes.c_byte, ctypes.c_byte, ctypes.c_byte,
                                                           ctypes.c_byte,
                                                           ctypes.c_ushort,
                                                           ctypes.c_byte *
                                                           self.dict_command_bytes_buffer_length[
                                                               CommandID.ESetBubbleSensitivity]]

        """GetSensorStatusCommandBytes of DLL"""
        self.func_get_sensor_status_bytes = self.protocol_parser.GetSensorStatusCommandBytes
        self.func_get_sensor_status_bytes.retypes = ctypes.c_int
        self.func_get_sensor_status_bytes.argtypes = [ctypes.c_byte, ctypes.c_byte,
                                                      ctypes.c_int,
                                                      ctypes.c_ushort,
                                                      ctypes.c_byte * self.dict_command_bytes_buffer_length[
                                                          CommandID.EGetSensorStatus]]

        """RemoteStartPrimeCommandBytes of DLL"""
        self.func_start_prime_bytes = self.protocol_parser.RemoteStartPrimeCommandBytes
        self.func_start_prime_bytes.retypes = ctypes.c_int
        self.func_start_prime_bytes.argtypes = [ctypes.c_byte, ctypes.c_byte,
                                                ctypes.c_byte,
                                                ctypes.c_ushort,
                                                ctypes.c_byte * self.dict_command_bytes_buffer_length[
                                                    CommandID.ERemoteStartPrime]]

        """RemoteStartBolusCommandBytes of DLL"""
        self.func_start_bolus_bytes = self.protocol_parser.RemoteStartBolusCommandBytes
        self.func_start_bolus_bytes.retypes = ctypes.c_int
        self.func_start_bolus_bytes.argtypes = [ctypes.c_byte, ctypes.c_byte,
                                                ctypes.c_byte,
                                                ctypes.c_ushort,
                                                ctypes.c_byte * self.dict_command_bytes_buffer_length[
                                                    CommandID.ERemoteStartBolus]]

        """RemoteSetBolusParameterCommandBytes of DLL"""
        self.func_set_bolus_parameter_bytes = self.protocol_parser.RemoteSetBolusParameterCommandBytes
        self.func_set_bolus_parameter_bytes.retypes = ctypes.c_int
        self.func_set_bolus_parameter_bytes.argtypes = [ctypes.c_byte, ctypes.c_byte,
                                                        ctypes.c_float,
                                                        ctypes.c_float,
                                                        ctypes.c_ushort,
                                                        ctypes.c_byte * self.dict_command_bytes_buffer_length[
                                                            CommandID.ERemoteSetBolusParameter]]

        # """VerifyPasscodeCommandBytes of DLL"""
        # self.func_verify_passcode_bytes = self.protocol_parser.VerifyPasscodeCommandBytes
        # self.func_verify_passcode_bytes.retypes = ctypes.c_int
        # self.func_verify_passcode_bytes.argtypes = [ctypes.c_byte, ctypes.c_byte, ctypes.c_byte, ctypes.c_byte,
        #                                             ctypes.c_byte * 4,
        #                                             ctypes.c_ushort,
        #                                             ctypes.c_byte * self.dict_command_bytes_buffer_length[
        #                                                 CommandID.EVerifyPasscode]]

    def __init_dict(self):
        self.dict_command_bytes_buffer_length.clear()
        # Define the command byte length mapping table, that is, the length of the byte number that actually sends the command to the pump.The number of bytes returned by the pump need not be considered.
        self.dict_command_bytes_buffer_length[CommandID.ESetKVO] = 31
        self.dict_command_bytes_buffer_length[CommandID.EGetKVO] = 22
        self.dict_command_bytes_buffer_length[CommandID.EGetBrand] = 22
        self.dict_command_bytes_buffer_length[CommandID.EWriteLog] = 30
        self.dict_command_bytes_buffer_length[CommandID.ESetBrand] = 27
        self.dict_command_bytes_buffer_length[CommandID.EStopMotor] = 22
        self.dict_command_bytes_buffer_length[CommandID.EGetLogItem] = 30
        self.dict_command_bytes_buffer_length[CommandID.ESetDateTime] = 33
        self.dict_command_bytes_buffer_length[CommandID.EGetDateTime] = 22
        self.dict_command_bytes_buffer_length[CommandID.EGetDoseUnit] = 22
        self.dict_command_bytes_buffer_length[CommandID.ESetDoseUnit] = 27
        self.dict_command_bytes_buffer_length[CommandID.EGetTitleHint] = 27
        self.dict_command_bytes_buffer_length[CommandID.EGetProductID] = 22
        self.dict_command_bytes_buffer_length[CommandID.EGetPumpAlarm] = 22
        self.dict_command_bytes_buffer_length[CommandID.EGetAlarmName] = 27
        self.dict_command_bytes_buffer_length[CommandID.EGetAlarmCount] = 22
        self.dict_command_bytes_buffer_length[CommandID.EResetPumpMode] = 27
        self.dict_command_bytes_buffer_length[CommandID.ESendFileStart] = 38
        self.dict_command_bytes_buffer_length[CommandID.EForwardVolume] = 30
        self.dict_command_bytes_buffer_length[CommandID.EGetBrightness] = 22
        self.dict_command_bytes_buffer_length[CommandID.ESetBrightness] = 27
        self.dict_command_bytes_buffer_length[CommandID.EVerifyPasscode] = 31
        self.dict_command_bytes_buffer_length[CommandID.EGetLogTotalNum] = 22
        self.dict_command_bytes_buffer_length[CommandID.ESetAlarmVolume] = 27
        self.dict_command_bytes_buffer_length[CommandID.EGetAlarmVolume] = 22
        self.dict_command_bytes_buffer_length[CommandID.EGetPowerStatus] = 22
        self.dict_command_bytes_buffer_length[CommandID.ERollbackVolume] = 30
        self.dict_command_bytes_buffer_length[CommandID.EGetScreenValue] = 29
        self.dict_command_bytes_buffer_length[CommandID.EGetCurrentDrug] = 22
        self.dict_command_bytes_buffer_length[CommandID.EGetCurrentMode] = 22
        self.dict_command_bytes_buffer_length[CommandID.ESetCurrentDrug] = 28
        self.dict_command_bytes_buffer_length[CommandID.ESetDrugMassUnit] = 27
        self.dict_command_bytes_buffer_length[CommandID.EGetSensorStatus] = 30
        self.dict_command_bytes_buffer_length[CommandID.EGetLockPassword] = 22
        self.dict_command_bytes_buffer_length[CommandID.EGetDrugMassUnit] = 22
        self.dict_command_bytes_buffer_length[CommandID.EGetSerialNumber] = 22
        self.dict_command_bytes_buffer_length[CommandID.EGetInfusionMode] = 22
        self.dict_command_bytes_buffer_length[CommandID.EGetPumpLanguage] = 22
        self.dict_command_bytes_buffer_length[CommandID.EGetSystemStatus] = 22
        self.dict_command_bytes_buffer_length[CommandID.ESetLockPassword] = 30
        self.dict_command_bytes_buffer_length[CommandID.ESetInfusionMode] = 27
        self.dict_command_bytes_buffer_length[CommandID.EClearHistoryLog] = 22
        self.dict_command_bytes_buffer_length[CommandID.ESendFilePackage] = 200
        self.dict_command_bytes_buffer_length[CommandID.ERemoteStartPrime] = 27
        self.dict_command_bytes_buffer_length[CommandID.ERemoteStartBolus] = 27
        self.dict_command_bytes_buffer_length[CommandID.ESendFileCompleted] = 29
        self.dict_command_bytes_buffer_length[CommandID.EGetOcclusionLevel] = 22
        self.dict_command_bytes_buffer_length[CommandID.ESetOcclusionLevel] = 27
        self.dict_command_bytes_buffer_length[CommandID.ESetAlarmSoundType] = 27
        self.dict_command_bytes_buffer_length[CommandID.EGetAlarmSoundType] = 22
        self.dict_command_bytes_buffer_length[CommandID.ESetSecuritySwitch] = 34
        self.dict_command_bytes_buffer_length[CommandID.EGetSecuritySwitch] = 30
        self.dict_command_bytes_buffer_length[CommandID.EGetNightModePeriod] = 22
        self.dict_command_bytes_buffer_length[CommandID.EGetFirmwareVersion] = 22
        self.dict_command_bytes_buffer_length[CommandID.ESetNightModePeriod] = 30
        self.dict_command_bytes_buffer_length[CommandID.EGetCaliCustomBrand] = 22
        self.dict_command_bytes_buffer_length[CommandID.ESetPreselectonBrand] = 32
        self.dict_command_bytes_buffer_length[CommandID.EGetPreselectonBrand] = 22
        self.dict_command_bytes_buffer_length[CommandID.ESetInfusionParameter] = 43
        self.dict_command_bytes_buffer_length[CommandID.ESetAlarmTypePassword] = 30
        self.dict_command_bytes_buffer_length[CommandID.EGetBasicModeRateUnit] = 22
        self.dict_command_bytes_buffer_length[CommandID.EGetInfusionParameter] = 22
        self.dict_command_bytes_buffer_length[CommandID.ESetBasicModeRateUnit] = 27
        self.dict_command_bytes_buffer_length[CommandID.EGetMaintenancePeriod] = 22
        self.dict_command_bytes_buffer_length[CommandID.EGetAlarmTypePassword] = 22
        self.dict_command_bytes_buffer_length[CommandID.EGetBubbleSensitivity] = 27
        self.dict_command_bytes_buffer_length[CommandID.ESetBubbleSensitivity] = 28
        self.dict_command_bytes_buffer_length[CommandID.ERestoreFactorySetting] = 22
        self.dict_command_bytes_buffer_length[CommandID.ESetNightModeBrightness] = 27
        self.dict_command_bytes_buffer_length[CommandID.EGetNightModeBrightness] = 22
        self.dict_command_bytes_buffer_length[CommandID.ESetCustomBrandCaliPara] = 37
        self.dict_command_bytes_buffer_length[CommandID.EGetCustomBrandCaliPara] = 22
        self.dict_command_bytes_buffer_length[CommandID.EGetMaintenanceDateTime] = 22
        self.dict_command_bytes_buffer_length[CommandID.EGetInfusingParasOfMode] = 22
        self.dict_command_bytes_buffer_length[CommandID.ERemoteSetBolusParameter] = 34
        self.dict_command_bytes_buffer_length[CommandID.ESetNightModeAlarmVolume] = 27
        self.dict_command_bytes_buffer_length[CommandID.EGetNightModeAlarmVolume] = 22
        self.dict_command_bytes_buffer_length[CommandID.EGetSupportedMaxFileSize] = 22
        self.dict_command_bytes_buffer_length[CommandID.ERemoteStartStopInfusion] = 27
        self.dict_command_bytes_buffer_length[CommandID.EGetBatteryAlarmDuration] = 22
        self.dict_command_bytes_buffer_length[CommandID.EGetFactoryFirmwareVersion] = 27
        self.dict_command_bytes_buffer_length[CommandID.ESetInfusingParameterOfMode] = 22
        self.dict_command_bytes_buffer_length[CommandID.EClearAllCustomBrandCaliPara] = 22
        self.dict_command_bytes_buffer_length[CommandID.EGetCompleteInfusionAlarmTime] = 22
        self.dict_command_bytes_buffer_length[CommandID.ESetCompleteInfusionAlarmTime] = 27
        self.dict_command_bytes_buffer_length[CommandID.EGetInfusionNearCompleteCriteria] = 22
        self.dict_command_bytes_buffer_length[CommandID.ESetInfusionNearCompleteCriteria] = 31
        self.dict_command_bytes_buffer_length[CommandID.ESetTubePrecisionCalibrationBrand] = 27
        self.dict_command_bytes_buffer_length[CommandID.ESetTubePrecisionCalibrationParameter] = 37

        # self.dict_command_bytes_buffer_length[CommandID.EClearCustomBrandCaliPara] =
        # self.dict_command_bytes_buffer_length[CommandID.ESetInfusingParameterOfMode] =
        # self.dict_command_bytes_buffer_length[CommandID.ESetMaintenancePeriod] =
        # self.dict_command_bytes_buffer_length[CommandID.EGetPressureSensorValue] =
        # self.dict_command_bytes_buffer_length[CommandID.EGetPressurePValue] =
        # self.dict_command_bytes_buffer_length[CommandID.EGetPressureFactor_ABC] =
        # self.dict_command_bytes_buffer_length[CommandID.EGetSizeSensorCalibrationFactor_KP] =
        # self.dict_command_bytes_buffer_length[CommandID.EGetSizeSensorValue] =
        # self.dict_command_bytes_buffer_length[CommandID.EGetBatteryVoltage] =
        # self.dict_command_bytes_buffer_length[CommandID.EGetUIUserDefineSyringeBrandName] =
        # self.dict_command_bytes_buffer_length[CommandID.ESetPumpLanguage] =
        # self.dict_command_bytes_buffer_length[CommandID.ESetSerialNumber] =
        # self.dict_command_bytes_buffer_length[CommandID.ESetUIUserDefineSyringeBrandName] =
        # self.dict_command_bytes_buffer_length[CommandID.EGetDrugItem] =
        # self.dict_command_bytes_buffer_length[CommandID.EUpdateDrugItem] =
        # self.dict_command_bytes_buffer_length[CommandID.EGetCategoryItem] =
        # self.dict_command_bytes_buffer_length[CommandID.EUpdateCategoryItem] =
        # self.dict_command_bytes_buffer_length[CommandID.EGetDrugLibCount] =
        # self.dict_command_bytes_buffer_length[CommandID.EGetCategoryCount] =
        # self.dict_command_bytes_buffer_length[CommandID.EClearDrugLib] =
        # self.dict_command_bytes_buffer_length[CommandID.EGetLanguageCount] =
        # self.dict_command_bytes_buffer_length[CommandID.EUpdateCategoryDrugIndex] =
        # self.dict_command_bytes_buffer_length[CommandID.EGetCategoryDrugIndex] =
        # self.dict_command_bytes_buffer_length[CommandID.EGetOcculsionPressureThreshold] =
        # self.dict_command_bytes_buffer_length[CommandID.EGetSyringeData] =
        # self.dict_command_bytes_buffer_length[CommandID.EGetInputsAtMain] =
        # self.dict_command_bytes_buffer_length[CommandID.EGetBatteryThreshold] =
        # self.dict_command_bytes_buffer_length[CommandID.EGetFlashAddressData] =
        # self.dict_command_bytes_buffer_length[CommandID.EGetFCTFlag] =
        # self.dict_command_bytes_buffer_length[CommandID.EGetADCRedress] =
        # self.dict_command_bytes_buffer_length[CommandID.EGetSyringePressureSelfCaliValue] =
        # self.dict_command_bytes_buffer_length[CommandID.EGetSyringeCaliFlag] =
        # self.dict_command_bytes_buffer_length[CommandID.EGetAppImgValidFlag] =
        # self.dict_command_bytes_buffer_length[CommandID.EGetUIDeliverySecureConfig] =
        # self.dict_command_bytes_buffer_length[CommandID.EGetSyringeSizeCaliRange] =
        # self.dict_command_bytes_buffer_length[CommandID.EResetSPIFlashData] =
        # self.dict_command_bytes_buffer_length[CommandID.ESetOcculsionPressureThreshold] =
        # self.dict_command_bytes_buffer_length[CommandID.ESetSyringeData] =
        # self.dict_command_bytes_buffer_length[CommandID.ESetBatteryThreshold] =
        # self.dict_command_bytes_buffer_length[CommandID.ESetFlashAddressData] =
        # self.dict_command_bytes_buffer_length[CommandID.ESetFCTFlag] =
        # self.dict_command_bytes_buffer_length[CommandID.ESetADCRedress] =
        # self.dict_command_bytes_buffer_length[CommandID.ESetPressurePValue] =
        # self.dict_command_bytes_buffer_length[CommandID.ESetSyringePressureSelfCaliValue] =
        # self.dict_command_bytes_buffer_length[CommandID.ESetSyringeCaliFlag] =
        # self.dict_command_bytes_buffer_length[CommandID.ESetAppImgValidFlag] =
        # self.dict_command_bytes_buffer_length[CommandID.ESetUIDeliverySecureConfig] =
        # self.dict_command_bytes_buffer_length[CommandID.ESetPressureFactor_ABC] =
        # self.dict_command_bytes_buffer_length[CommandID.ESetSizeSensorCalibrationFactor_KP] =
        # self.dict_command_bytes_buffer_length[CommandID.ESetSyringeSizeCaliRange] =
        # self.dict_command_bytes_buffer_length[CommandID.EGetTitleHint] =
        # self.dict_command_bytes_buffer_length[CommandID.EISFCTMODE] =
        # self.dict_command_bytes_buffer_length[CommandID.EGetTestCaseCount] =
        # self.dict_command_bytes_buffer_length[CommandID.EGetTestCaseItem] =
        # self.dict_command_bytes_buffer_length[CommandID.EGetTestCaseHint] =
        # self.dict_command_bytes_buffer_length[CommandID.ETriggerTestCaseItem] =
        # self.dict_command_bytes_buffer_length[CommandID.ESetBolusRate] =

        self.dict_command_id_structure.clear()
        self.dict_command_id_structure[CommandID.ESetKVO] = SetKVO
        self.dict_command_id_structure[CommandID.EGetKVO] = GetKVO
        self.dict_command_id_structure[CommandID.EGetBrand] = GetBrand
        self.dict_command_id_structure[CommandID.ESetBrand] = SetBrand
        self.dict_command_id_structure[CommandID.EWriteLog] = WriteLog
        self.dict_command_id_structure[CommandID.EStopMotor] = StopMotor
        self.dict_command_id_structure[CommandID.EGetLogItem] = GetLogItem
        self.dict_command_id_structure[CommandID.EGetDateTime] = GetDateTime
        self.dict_command_id_structure[CommandID.ESetDateTime] = SetDateTime
        self.dict_command_id_structure[CommandID.ESetDoseUnit] = SetDoseUnit
        self.dict_command_id_structure[CommandID.EGetDoseUnit] = GetDoseUnit
        self.dict_command_id_structure[CommandID.EGetTitleHint] = GetTitleHint
        self.dict_command_id_structure[CommandID.EGetPumpAlarm] = GetPumpAlarm
        self.dict_command_id_structure[CommandID.EGetAlarmName] = GetAlarmName
        self.dict_command_id_structure[CommandID.EGetAlarmCount] = GetAlarmCount
        self.dict_command_id_structure[CommandID.ESetBrightness] = SetBrightness
        self.dict_command_id_structure[CommandID.EGetBrightness] = GetBrightness
        self.dict_command_id_structure[CommandID.EForwardVolume] = ForwardVolume
        self.dict_command_id_structure[CommandID.ESendFileStart] = SendFileStart
        self.dict_command_id_structure[CommandID.EResetPumpMode] = ResetPumpMode
        self.dict_command_id_structure[CommandID.EGetAlarmVolume] = GetAlarmVolume
        self.dict_command_id_structure[CommandID.ESetAlarmVolume] = SetAlarmVolume
        self.dict_command_id_structure[CommandID.ERollbackVolume] = RollbackVolume
        self.dict_command_id_structure[CommandID.EGetScreenValue] = GetScreenValue
        self.dict_command_id_structure[CommandID.ESetCurrentDrug] = SetCurrentDrug
        self.dict_command_id_structure[CommandID.EGetCurrentDrug] = GetCurrentDrug
        self.dict_command_id_structure[CommandID.EGetCurrentMode] = GetCurrentMode
        self.dict_command_id_structure[CommandID.EGetLogTotalNum] = GetLogTotalNum
        self.dict_command_id_structure[CommandID.EVerifyPasscode] = VerifyPasscode
        self.dict_command_id_structure[CommandID.EGetSystemStatus] = GetSystemStatus
        self.dict_command_id_structure[CommandID.ESendFilePackage] = SendFilePackage
        self.dict_command_id_structure[CommandID.ESetDrugMassUnit] = SetDrugMassUnit
        self.dict_command_id_structure[CommandID.EGetInfusionMode] = GetInfusionMode
        self.dict_command_id_structure[CommandID.ESetInfusionMode] = SetInfusionMode
        self.dict_command_id_structure[CommandID.EGetDrugMassUnit] = GetDrugMassUnit
        self.dict_command_id_structure[CommandID.EGetSerialNumber] = GetSerialNumber
        self.dict_command_id_structure[CommandID.EClearHistoryLog] = ClearHistoryLog
        self.dict_command_id_structure[CommandID.EGetSensorStatus] = GetSensorStatus
        self.dict_command_id_structure[CommandID.ESetSecuritySwitch] = SetSecuritySwitch
        self.dict_command_id_structure[CommandID.EGetSecuritySwitch] = GetSecuritySwitch
        self.dict_command_id_structure[CommandID.ESendFileCompleted] = SendFileCompleted
        self.dict_command_id_structure[CommandID.ESetAlarmSoundType] = SetAlarmSoundType
        self.dict_command_id_structure[CommandID.EGetAlarmSoundType] = GetAlarmSoundType
        self.dict_command_id_structure[CommandID.ESetOcclusionLevel] = SetOcclusionLevel
        self.dict_command_id_structure[CommandID.EGetOcclusionLevel] = GetOcclusionLevel
        self.dict_command_id_structure[CommandID.ESetNightModePeriod] = SetNightModePeriod
        self.dict_command_id_structure[CommandID.EGetNightModePeriod] = GetNightModePeriod
        self.dict_command_id_structure[CommandID.EGetFirmwareVersion] = GetFirmwareVersion
        self.dict_command_id_structure[CommandID.EGetBubbleSensitivity] = GetBubbleSensitivity
        self.dict_command_id_structure[CommandID.ESetBubbleSensitivity] = SetBubbleSensitivity
        self.dict_command_id_structure[CommandID.ESetInfusionParameter] = SetInfusionParameter
        self.dict_command_id_structure[CommandID.EGetInfusionParameter] = GetInfusionParameter
        self.dict_command_id_structure[CommandID.EGetBasicModeRateUnit] = GetBasicModeRateUnit
        self.dict_command_id_structure[CommandID.EGetMaintenancePeriod] = GetMaintenancePeriod
        self.dict_command_id_structure[CommandID.ESetBasicModeRateUnit] = SetBasicModeRateUnit
        self.dict_command_id_structure[CommandID.EGetAlarmTypePassword] = GetAlarmTypePassword
        self.dict_command_id_structure[CommandID.ERestoreFactorySetting] = RestoreFactorySetting
        self.dict_command_id_structure[CommandID.ESetNightModeBrightness] = SetNightModeBrightness
        self.dict_command_id_structure[CommandID.EGetNightModeBrightness] = GetNightModeBrightness
        self.dict_command_id_structure[CommandID.EGetMaintenanceDateTime] = GetMaintenanceDateTime
        self.dict_command_id_structure[CommandID.EGetInfusingParasOfMode] = GetInfusingParasOfMode
        self.dict_command_id_structure[CommandID.ESetNightModeAlarmVolume] = SetNightModeAlarmVolume
        self.dict_command_id_structure[CommandID.ERemoteStartStopInfusion] = RemoteStartStopInfusion
        self.dict_command_id_structure[CommandID.ERemoteStartPrime] = RemoteStartPrime
        self.dict_command_id_structure[CommandID.ERemoteStartBolus] = RemoteStartBolus
        self.dict_command_id_structure[CommandID.ERemoteSetBolusParameter] = RemoteSetBolusParameter
        self.dict_command_id_structure[CommandID.EGetNightModeAlarmVolume] = GetNightModeAlarmVolume
        self.dict_command_id_structure[CommandID.ESetInfusingParameterOfMode] = SetInfusingParameter
        self.dict_command_id_structure[CommandID.EGetFactoryFirmwareVersion] = GetFactoryFirmwareVersion
        self.dict_command_id_structure[CommandID.ESetCompleteInfusionAlarmTime] = SetCompleteInfusionAlarmTime
        self.dict_command_id_structure[CommandID.EGetInfusionNearCompleteCriteria] = GetInfusionNearCompleteCriteria
        self.dict_command_id_structure[CommandID.ESetInfusionNearCompleteCriteria] = SetInfusionNearCompleteCriteria
        self.dict_command_id_structure[CommandID.ESetTubePrecisionCalibrationBrand] = SetTubePrecisionCalibrationBrand
        self.dict_command_id_structure[
            CommandID.ESetTubePrecisionCalibrationParameter] = SetTubePrecisionCalibrationParameter
