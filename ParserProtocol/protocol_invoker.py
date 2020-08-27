# -*-coding:utf-8 -*-
import os
import sys
current_dir = os.path.abspath(os.path.dirname(__file__))
sys.path.append(current_dir)
sys.path.append("..")

from PumpLibrary.ParserProtocol.base_invoker import *



class ProtocolParserInvoker(BaseInvoker):

    def get_command_id(self, input_buffer, length):

        self.func_get_command_id.argtypes = [ctypes.c_byte * length, ctypes.c_ushort, ctypes.c_void_p]
        typeof_buffer_bytes = ctypes.c_byte * length
        c_type_buffer = typeof_buffer_bytes(*input_buffer)
        process_length = ctypes.c_ushort(0)
        command_id = 0
        try:
            command_id = self.func_get_command_id(c_type_buffer, length, ctypes.byref(process_length))
        except OSError as oserror:
            self.func_empty_buffer()
            print("OSError Occured", oserror)
        except Exception as e:
            print("Exception Occured", e)
        return command_id, process_length.value

    def get_command_data(self, command_id):

        if command_id not in self.dict_command_id_structure.keys():
            return None
        cmd = self.dict_command_id_structure[command_id]()
        if cmd is None:
            return None
        cmd_id = self.func_get_command_data(command_id.value, ctypes.byref(cmd))
        cmd.command_id = cmd_id
        if cmd_id <= 0:
            return None
        else:
            return cmd

    def get_kvo_command_bytes(self, sequence_id, product_id):

        typeof_bytes = ctypes.c_byte * self.dict_command_bytes_buffer_length[CommandID.EGetKVO]
        temp_buffer = typeof_bytes()
        length = self.func_get_kvo_bytes(sequence_id, product_id,
                                         self.dict_command_bytes_buffer_length[CommandID.EGetKVO], temp_buffer)
        if length != self.dict_command_bytes_buffer_length[CommandID.EGetKVO]:
            return None
        bytes_buffer = bytes(temp_buffer)
        return bytes_buffer

    def get_serial_number_command_bytes(self, sequence_id, product_id):

        typeof_bytes = ctypes.c_byte * self.dict_command_bytes_buffer_length[CommandID.EGetSerialNumber]
        temp_buffer = typeof_bytes()
        length = self.func_get_serial_number_bytes(sequence_id, product_id,
                                                   self.dict_command_bytes_buffer_length[CommandID.EGetSerialNumber],
                                                   temp_buffer)
        if length != self.dict_command_bytes_buffer_length[CommandID.EGetSerialNumber]:
            return None
        bytes_buffer = bytes(temp_buffer)
        return bytes_buffer

    def rollback_volume_command_bytes(self, sequence_id, product_id, volume):

        typeof_bytes = ctypes.c_byte * self.dict_command_bytes_buffer_length[CommandID.ERollbackVolume]
        temp_buffer = typeof_bytes()
        length = self.func_rollback_volume_bytes(sequence_id, product_id, volume,
                                                 self.dict_command_bytes_buffer_length[CommandID.ERollbackVolume],
                                                 temp_buffer)
        if length != self.dict_command_bytes_buffer_length[CommandID.ERollbackVolume]:
            return None
        bytes_buffer = bytes(temp_buffer)
        return bytes_buffer

    def forward_volume_command_bytes(self, sequence_id, product_id, volume):

        print("forward_volume_command_bytes parameter volume=", volume)
        typeof_bytes = ctypes.c_byte * self.dict_command_bytes_buffer_length[CommandID.EForwardVolume]
        temp_buffer = typeof_bytes()
        length = self.func_forward_volume_bytes(sequence_id, product_id, volume,
                                                self.dict_command_bytes_buffer_length[CommandID.EForwardVolume],
                                                temp_buffer)
        print("forward_volume_command_bytes length =", length)
        if length != self.dict_command_bytes_buffer_length[CommandID.EForwardVolume]:
            return None
        bytes_buffer = bytes(temp_buffer)
        print("forward_volume_command_bytes bytes_buffer =", bytes_buffer)
        return bytes_buffer

    def stop_motor_command_bytes(self, sequence_id, product_id):

        print("stop_motor_command_bytes parameter")
        typeof_bytes = ctypes.c_byte * self.dict_command_bytes_buffer_length[CommandID.EStopMotor]
        temp_buffer = typeof_bytes()
        length = self.func_stop_motor_bytes(sequence_id, product_id,
                                            self.dict_command_bytes_buffer_length[CommandID.EStopMotor], temp_buffer)
        print("stop_motor_command_bytes length =", length)
        if length != self.dict_command_bytes_buffer_length[CommandID.EStopMotor]:
            return None
        bytes_buffer = bytes(temp_buffer)
        print("stop_motor_command_bytes bytes_buffer =", bytes_buffer)
        return bytes_buffer

    def get_title_hint_command_bytes(self, sequence_id, product_id, flag):

        typeof_bytes = ctypes.c_byte * self.dict_command_bytes_buffer_length[CommandID.EGetTitleHint]
        temp_buffer = typeof_bytes()
        length = self.func_get_title_hint_bytes(sequence_id, product_id, flag,
                                                self.dict_command_bytes_buffer_length[CommandID.EGetTitleHint],
                                                temp_buffer)
        if length != self.dict_command_bytes_buffer_length[CommandID.EGetTitleHint]:
            return None
        bytes_buffer = bytes(temp_buffer)
        return bytes_buffer

    def get_screen_value_command_bytes(self, sequence_id, product_id, row, col, screen_id):

        typeof_bytes = ctypes.c_byte * self.dict_command_bytes_buffer_length[CommandID.EGetScreenValue]
        temp_buffer = typeof_bytes()
        length = self.func_get_screen_value_bytes(sequence_id, product_id, row, col, screen_id,
                                                  self.dict_command_bytes_buffer_length[CommandID.EGetScreenValue],
                                                  temp_buffer)
        if length != self.dict_command_bytes_buffer_length[CommandID.EGetScreenValue]:
            return None
        bytes_buffer = bytes(temp_buffer)
        return bytes_buffer

    def get_current_mode_command_bytes(self, sequence_id, product_id):

        typeof_bytes = ctypes.c_byte * self.dict_command_bytes_buffer_length[CommandID.EGetCurrentMode]
        temp_buffer = typeof_bytes()
        length = self.func_get_current_mode_bytes(sequence_id, product_id,
                                                  self.dict_command_bytes_buffer_length[CommandID.EGetCurrentMode],
                                                  temp_buffer)
        if length != self.dict_command_bytes_buffer_length[CommandID.EGetCurrentMode]:
            return None
        bytes_buffer = bytes(temp_buffer)
        return bytes_buffer

    def get_occlusion_level_command_bytes(self, sequence_id, product_id):

        typeof_bytes = ctypes.c_byte * self.dict_command_bytes_buffer_length[CommandID.EGetOcclusionLevel]
        temp_buffer = typeof_bytes()
        length = self.func_get_occlusion_level_bytes(sequence_id, product_id,
                                                     self.dict_command_bytes_buffer_length[
                                                         CommandID.EGetOcclusionLevel], temp_buffer)
        if length != self.dict_command_bytes_buffer_length[CommandID.EGetOcclusionLevel]:
            return None
        bytes_buffer = bytes(temp_buffer)
        return bytes_buffer

    def get_infusion_mode_command_bytes(self, sequence_id, product_id):

        typeof_bytes = ctypes.c_byte * self.dict_command_bytes_buffer_length[CommandID.EGetInfusionMode]
        temp_buffer = typeof_bytes()
        length = self.func_get_infusion_mode_bytes(sequence_id, product_id,
                                                   self.dict_command_bytes_buffer_length[CommandID.EGetInfusionMode],
                                                   temp_buffer)
        if length != self.dict_command_bytes_buffer_length[CommandID.EGetInfusionMode]:
            return None
        bytes_buffer = bytes(temp_buffer)
        return bytes_buffer

    def get_brand_command_bytes(self, sequence_id, product_id):

        typeof_bytes = ctypes.c_byte * self.dict_command_bytes_buffer_length[CommandID.EGetBrand]
        temp_buffer = typeof_bytes()
        length = self.func_get_syringe_brand_bytes(sequence_id, product_id,
                                                   self.dict_command_bytes_buffer_length[CommandID.EGetBrand],
                                                   temp_buffer)
        if length != self.dict_command_bytes_buffer_length[CommandID.EGetBrand]:
            return None
        bytes_buffer = bytes(temp_buffer)
        return bytes_buffer

    def get_dose_uint_command_bytes(self, sequence_id, product_id):

        typeof_bytes = ctypes.c_byte * self.dict_command_bytes_buffer_length[CommandID.EGetDoseUnit]
        temp_buffer = typeof_bytes()
        length = self.func_get_dose_uint_bytes(sequence_id, product_id,
                                               self.dict_command_bytes_buffer_length[CommandID.EGetDoseUnit],
                                               temp_buffer)
        if length != self.dict_command_bytes_buffer_length[CommandID.EGetDoseUnit]:
            return None
        bytes_buffer = bytes(temp_buffer)
        return bytes_buffer

    def get_drug_mass_uint_command_bytes(self, sequence_id, product_id):

        typeof_bytes = ctypes.c_byte * self.dict_command_bytes_buffer_length[CommandID.EGetDrugMassUnit]
        temp_buffer = typeof_bytes()
        length = self.func_get_drug_mass_uint_bytes(sequence_id, product_id,
                                                    self.dict_command_bytes_buffer_length[CommandID.EGetDrugMassUnit],
                                                    temp_buffer)
        if length != self.dict_command_bytes_buffer_length[CommandID.EGetDrugMassUnit]:
            return None
        bytes_buffer = bytes(temp_buffer)
        return bytes_buffer

    def get_basic_mode_rate_unit_command_bytes(self, sequence_id, product_id):

        typeof_bytes = ctypes.c_byte * self.dict_command_bytes_buffer_length[CommandID.EGetBasicModeRateUnit]
        temp_buffer = typeof_bytes()
        length = self.func_get_basic_mode_rate_uint_bytes(sequence_id, product_id,
                                                          self.dict_command_bytes_buffer_length[
                                                              CommandID.EGetBasicModeRateUnit],
                                                          temp_buffer)
        if length != self.dict_command_bytes_buffer_length[CommandID.EGetBasicModeRateUnit]:
            return None
        bytes_buffer = bytes(temp_buffer)
        return bytes_buffer

    def set_occlusion_level_command_bytes(self, sequence_id, product_id, level):

        typeof_bytes = ctypes.c_byte * self.dict_command_bytes_buffer_length[CommandID.ESetOcclusionLevel]
        temp_buffer = typeof_bytes()
        length = self.func_set_occlusion_level_bytes(sequence_id, product_id, level,
                                                     self.dict_command_bytes_buffer_length[
                                                         CommandID.ESetOcclusionLevel],
                                                     temp_buffer)
        if length != self.dict_command_bytes_buffer_length[CommandID.ESetOcclusionLevel]:
            return None
        bytes_buffer = bytes(temp_buffer)
        return bytes_buffer

    def set_infusion_mode_command_bytes(self, sequence_id, product_id, mode):

        typeof_bytes = ctypes.c_byte * self.dict_command_bytes_buffer_length[CommandID.ESetInfusionMode]
        temp_buffer = typeof_bytes()
        # print(temp_buffer)
        # print(temp_buffer[3])
        # print(type(temp_buffer))
        # print(len(temp_buffer))
        length = self.func_set_infusion_mode_bytes(sequence_id, product_id, mode,
                                                   self.dict_command_bytes_buffer_length[CommandID.ESetInfusionMode],
                                                   temp_buffer)
        # print(length)
        # print(type(length))
        # print(temp_buffer[0])
        if length != self.dict_command_bytes_buffer_length[CommandID.ESetInfusionMode]:
            return None
        bytes_buffer = bytes(temp_buffer)
        # print(bytes_buffer)
        return bytes_buffer

    def set_brand_command_bytes(self, sequence_id, product_id, brand):

        typeof_bytes = ctypes.c_byte * self.dict_command_bytes_buffer_length[CommandID.ESetBrand]
        temp_buffer = typeof_bytes()
        length = self.func_set_syringe_brand_bytes(sequence_id, product_id, brand,
                                                   self.dict_command_bytes_buffer_length[CommandID.ESetBrand],
                                                   temp_buffer)
        if length != self.dict_command_bytes_buffer_length[CommandID.ESetBrand]:
            return None
        bytes_buffer = bytes(temp_buffer)
        return bytes_buffer

    def set_dose_unit_command_bytes(self, sequence_id, product_id, unit):

        typeof_bytes = ctypes.c_byte * self.dict_command_bytes_buffer_length[CommandID.ESetDoseUnit]
        temp_buffer = typeof_bytes()
        length = self.func_set_dose_unit_bytes(sequence_id, product_id, unit,
                                               self.dict_command_bytes_buffer_length[CommandID.ESetDoseUnit],
                                               temp_buffer)
        if length != self.dict_command_bytes_buffer_length[CommandID.ESetDoseUnit]:
            return None
        bytes_buffer = bytes(temp_buffer)
        return bytes_buffer

    def set_drug_mass_unit_command_bytes(self, sequence_id, product_id, unit):

        typeof_bytes = ctypes.c_byte * self.dict_command_bytes_buffer_length[CommandID.ESetDrugMassUnit]
        temp_buffer = typeof_bytes()
        length = self.func_set_drug_mass_unit_bytes(sequence_id, product_id, unit,
                                                    self.dict_command_bytes_buffer_length[CommandID.ESetDrugMassUnit],
                                                    temp_buffer)
        if length != self.dict_command_bytes_buffer_length[CommandID.ESetDrugMassUnit]:
            return None
        bytes_buffer = bytes(temp_buffer)
        return bytes_buffer

    def set_weight_unit_command_bytes(self, sequence_id, product_id, unit):

        typeof_bytes = ctypes.c_byte * self.dict_command_bytes_buffer_length[CommandID.ESetWeightUnit]
        temp_buffer = typeof_bytes()
        length = self.func_set_weight_unit_bytes(sequence_id, product_id, unit,
                                                 self.dict_command_bytes_buffer_length[CommandID.ESetWeightUnit],
                                                 temp_buffer)
        if length != self.dict_command_bytes_buffer_length[CommandID.ESetWeightUnit]:
            return None
        bytes_buffer = bytes(temp_buffer)
        return bytes_buffer

    def set_kvo_command_bytes(self, sequence_id, product_id, kvo):

        typeof_bytes = ctypes.c_byte * self.dict_command_bytes_buffer_length[CommandID.ESetKVO]
        temp_buffer = typeof_bytes()
        length = self.func_set_kvo_bytes(sequence_id, product_id, kvo,
                                         self.dict_command_bytes_buffer_length[CommandID.ESetKVO], temp_buffer)
        if length != self.dict_command_bytes_buffer_length[CommandID.ESetKVO]:
            return None
        bytes_buffer = bytes(temp_buffer)
        return bytes_buffer

    def set_complete_infusion_alarm_command_bytes(self, sequence_id, product_id, time):

        typeof_bytes = ctypes.c_byte * self.dict_command_bytes_buffer_length[CommandID.ESetCompleteInfusionAlarmTime]
        temp_buffer = typeof_bytes()
        length = self.func_set_complete_infusion_alarm_time_bytes(sequence_id, product_id, time,
                                                                  self.dict_command_bytes_buffer_length[
                                                                      CommandID.ESetCompleteInfusionAlarmTime],
                                                                  temp_buffer)
        if length != self.dict_command_bytes_buffer_length[CommandID.ESetCompleteInfusionAlarmTime]:
            return None
        bytes_buffer = bytes(temp_buffer)
        return bytes_buffer

    def get_infusion_parameter_command_bytes(self, sequence_id, product_id):

        typeof_bytes = ctypes.c_byte * self.dict_command_bytes_buffer_length[CommandID.EGetInfusionParameter]
        temp_buffer = typeof_bytes()
        length = self.func_get_infusion_parameter_bytes(sequence_id, product_id,
                                                        self.dict_command_bytes_buffer_length[
                                                            CommandID.EGetInfusionParameter], temp_buffer)
        if length != self.dict_command_bytes_buffer_length[CommandID.EGetInfusionParameter]:
            return None
        bytes_buffer = bytes(temp_buffer)
        return bytes_buffer

    def get_pump_alarm_command_bytes(self, sequence_id, product_id):

        typeof_bytes = ctypes.c_byte * self.dict_command_bytes_buffer_length[CommandID.EGetPumpAlarm]
        temp_buffer = typeof_bytes()
        length = self.func_get_pump_alarm_bytes(sequence_id, product_id,
                                                self.dict_command_bytes_buffer_length[CommandID.EGetPumpAlarm],
                                                temp_buffer)
        if length != self.dict_command_bytes_buffer_length[CommandID.EGetPumpAlarm]:
            return None
        bytes_buffer = bytes(temp_buffer)
        return bytes_buffer

    def get_alarm_name_command_bytes(self, sequence_id, product_id, alarm_index):

        typeof_bytes = ctypes.c_byte * self.dict_command_bytes_buffer_length[CommandID.EGetAlarmName]
        temp_buffer = typeof_bytes()
        length = self.func_get_alarm_name_bytes(sequence_id, product_id, alarm_index,
                                                self.dict_command_bytes_buffer_length[CommandID.EGetAlarmName],
                                                temp_buffer)
        if length != self.dict_command_bytes_buffer_length[CommandID.EGetAlarmName]:
            return None
        bytes_buffer = bytes(temp_buffer)
        return bytes_buffer

    def get_alarm_count_command_bytes(self, sequence_id, product_id):

        typeof_bytes = ctypes.c_byte * self.dict_command_bytes_buffer_length[CommandID.EGetAlarmCount]
        temp_buffer = typeof_bytes()
        length = self.func_get_alarm_count_bytes(sequence_id, product_id,
                                                 self.dict_command_bytes_buffer_length[CommandID.EGetAlarmCount],
                                                 temp_buffer)
        if length != self.dict_command_bytes_buffer_length[CommandID.EGetAlarmCount]:
            return None
        bytes_buffer = bytes(temp_buffer)
        return bytes_buffer

    def get_infusing_parameter_of_mode_command_bytes(self, sequence_id, product_id):

        typeof_bytes = ctypes.c_byte * self.dict_command_bytes_buffer_length[CommandID.EGetInfusingParasOfMode]
        temp_buffer = typeof_bytes()
        length = self.func_get_infusing_parameter_of_mode_bytes(sequence_id, product_id,
                                                                self.dict_command_bytes_buffer_length[
                                                                    CommandID.EGetInfusingParasOfMode], temp_buffer)
        if length != self.dict_command_bytes_buffer_length[CommandID.EGetInfusingParasOfMode]:
            return None
        bytes_buffer = bytes(temp_buffer)
        return bytes_buffer

    def reset_pump_mode_command_bytes(self, sequence_id, product_id, mode):

        typeof_bytes = ctypes.c_byte * self.dict_command_bytes_buffer_length[CommandID.EResetPumpMode]
        temp_buffer = typeof_bytes()
        length = self.func_reset_pump_mode_bytes(sequence_id, product_id, mode,
                                                 self.dict_command_bytes_buffer_length[CommandID.EResetPumpMode],
                                                 temp_buffer)
        if length != self.dict_command_bytes_buffer_length[CommandID.EResetPumpMode]:
            return None
        bytes_buffer = bytes(temp_buffer)
        return bytes_buffer

    def send_file_start_command_bytes(self, sequence_id, product_id, filetype, subid, filesize, checksum, blockcount):

        typeof_bytes = ctypes.c_byte * self.dict_command_bytes_buffer_length[CommandID.ESendFileStart]
        temp_buffer = typeof_bytes()
        length = self.func_send_file_start_bytes(sequence_id, product_id, filetype, subid, filesize, checksum,
                                                 blockcount,
                                                 self.dict_command_bytes_buffer_length[CommandID.ESendFileStart],
                                                 temp_buffer)
        if length != self.dict_command_bytes_buffer_length[CommandID.ESendFileStart]:
            return None
        bytes_buffer = bytes(temp_buffer)
        return bytes_buffer

    def send_file_package_command_bytes(self, sequence_id, product_id, filetype, subid, sequencenumber,
                                        packagedatalength, packagedatabuffer):

        self.dict_command_bytes_buffer_length[CommandID.ESendFilePackage] = 32 + packagedatalength
        self.func_send_file_package_bytes.argtypes = [ctypes.c_byte, ctypes.c_byte, ctypes.c_byte, ctypes.c_byte,
                                                      ctypes.c_uint32, ctypes.c_ushort,
                                                      ctypes.c_byte * packagedatalength, ctypes.c_ushort,
                                                      ctypes.c_byte * self.dict_command_bytes_buffer_length[
                                                          CommandID.ESendFilePackage]]
        typeof_bytes = ctypes.c_byte * self.dict_command_bytes_buffer_length[CommandID.ESendFilePackage]
        temp_buffer = typeof_bytes()
        length = self.func_send_file_package_bytes(sequence_id, product_id, filetype, subid, sequencenumber,
                                                   packagedatalength, packagedatabuffer,
                                                   self.dict_command_bytes_buffer_length[CommandID.ESendFilePackage],
                                                   temp_buffer)
        if length != self.dict_command_bytes_buffer_length[CommandID.ESendFilePackage]:
            return None
        bytes_buffer = bytes(temp_buffer)
        return bytes_buffer

    def send_file_complete_command_bytes(self, sequence_id, product_id, filetype, subid, result):

        typeof_bytes = ctypes.c_byte * self.dict_command_bytes_buffer_length[CommandID.ESendFileCompleted]
        temp_buffer = typeof_bytes()
        length = self.func_send_file_complete_bytes(sequence_id, product_id, filetype, subid, result,
                                                    self.dict_command_bytes_buffer_length[CommandID.ESendFileCompleted],
                                                    temp_buffer)
        if length != self.dict_command_bytes_buffer_length[CommandID.ESendFileCompleted]:
            return None
        bytes_buffer = bytes(temp_buffer)
        return bytes_buffer

    def set_infusion_parameter_command_bytes(self, sequence_id, product_id, structinfusionparameter):

        if not isinstance(structinfusionparameter, StructInfusionParameter):
            return None
        # if structinfusionparameter.infusion_mode == 0:
        #     self.dict_command_bytes_buffer_length[CommandID.ESetInfusionParameter] = 22 + 15
        # elif structinfusionparameter.infusion_mode == 1:
        #     self.dict_command_bytes_buffer_length[CommandID.ESetInfusionParameter] = 22 + 12
        # elif structinfusionparameter.infusion_mode == 2:
        #     self.dict_command_bytes_buffer_length[CommandID.ESetInfusionParameter] = 22 + 31
        # elif structinfusionparameter.infusion_mode == 3:
        #     self.dict_command_bytes_buffer_length[CommandID.ESetInfusionParameter] = 22 + 26
        # elif structinfusionparameter.infusion_mode == 16:
        #     self.dict_command_bytes_buffer_length[CommandID.ESetInfusionParameter] = 43
        # else:
        #     self.dict_command_bytes_buffer_length[CommandID.ESetInfusionParameter] = 100
        # self.func_set_infusion_parameter_bytes.argtypes = [ctypes.c_byte, ctypes.c_byte, StructInfusionParameter,
        #                                                    ctypes.c_ushort,
        #                                                    ctypes.c_byte * self.dict_command_bytes_buffer_length[
        #                                                        CommandID.ESetInfusionParameter]]
        typeof_bytes = ctypes.c_byte * self.dict_command_bytes_buffer_length[CommandID.ESetInfusionParameter]
        temp_buffer = typeof_bytes()
        length = self.func_set_infusion_parameter_bytes(sequence_id, product_id, structinfusionparameter,
                                                        self.dict_command_bytes_buffer_length[
                                                            CommandID.ESetInfusionParameter], temp_buffer)
        if length != self.dict_command_bytes_buffer_length[CommandID.ESetInfusionParameter]:
            return None
        bytes_buffer = bytes(temp_buffer)
        # b'\x0b\x1c\x00\x00\x02\n \x13\x0b\x1d\x150&+\x00\x02\x15\x00\x01\x00\x11\x00\x10\x00\x00\xc8B\t\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\xf6\x9d\xc8\xb5'
        return bytes_buffer

    # 0B 1C 00 00 02 0A 20 13 0B 1D 15 30 26 2B 00 02 15 00 01 00 11 00 10 00 00 C8 42 09 00 00 00 00 00 00 00 00 00 00 00 F6 9D C8 B5

    def set_infusing_parameter_command_bytes(self, sequence_id, product_id, structinfusingparameter):

        if not isinstance(structinfusingparameter, StructInfusingParameter):
            return None
        if structinfusingparameter.infusion_mode == 0:
            self.dict_command_bytes_buffer_length[CommandID.ESetInfusingParameterOfMode] = 22 + 10
        elif structinfusingparameter.infusion_mode == 1:
            self.dict_command_bytes_buffer_length[CommandID.ESetInfusingParameterOfMode] = 22 + 7
        elif structinfusingparameter.infusion_mode == 2:
            self.dict_command_bytes_buffer_length[CommandID.ESetInfusingParameterOfMode] = 22 + 10
        elif structinfusingparameter.infusion_mode == 3:
            self.dict_command_bytes_buffer_length[CommandID.ESetInfusingParameterOfMode] = 22 + 10
        else:
            self.dict_command_bytes_buffer_length[CommandID.ESetInfusingParameterOfMode] = 22 + 10
        self.func_set_infusing_parameter_bytes.argtypes = [ctypes.c_byte, ctypes.c_byte, StructInfusingParameter,
                                                           ctypes.c_ushort,
                                                           ctypes.c_byte * self.dict_command_bytes_buffer_length[
                                                               CommandID.ESetInfusingParameterOfMode]]
        typeof_bytes = ctypes.c_byte * self.dict_command_bytes_buffer_length[CommandID.ESetInfusingParameterOfMode]
        temp_buffer = typeof_bytes()
        length = self.func_set_infusing_parameter_bytes(sequence_id, product_id, structinfusingparameter,
                                                        self.dict_command_bytes_buffer_length[
                                                            CommandID.ESetInfusingParameterOfMode], temp_buffer)
        if length != self.dict_command_bytes_buffer_length[CommandID.ESetInfusingParameterOfMode]:
            return None
        bytes_buffer = bytes(temp_buffer)
        return bytes_buffer

    def remote_start_stop_infusion_command_bytes(self, sequence_id, product_id, start_or_stop):

        typeof_bytes = ctypes.c_byte * self.dict_command_bytes_buffer_length[CommandID.ERemoteStartStopInfusion]
        temp_buffer = typeof_bytes()
        length = self.func_remote_start_stop_infusion_bytes(sequence_id, product_id, start_or_stop,
                                                            self.dict_command_bytes_buffer_length[
                                                                CommandID.ERemoteStartStopInfusion], temp_buffer)
        if length != self.dict_command_bytes_buffer_length[CommandID.ERemoteStartStopInfusion]:
            return None
        bytes_buffer = bytes(temp_buffer)
        return bytes_buffer

    def get_system_status_command_bytes(self, sequence_id, product_id):

        typeof_bytes = ctypes.c_byte * self.dict_command_bytes_buffer_length[CommandID.EGetSystemStatus]
        temp_buffer = typeof_bytes()
        length = self.func_get_system_status_bytes(sequence_id, product_id,
                                                   self.dict_command_bytes_buffer_length[CommandID.EGetSystemStatus],
                                                   temp_buffer)
        if length != self.dict_command_bytes_buffer_length[CommandID.EGetSystemStatus]:
            return None
        bytes_buffer = bytes(temp_buffer)
        return bytes_buffer

    def set_alarm_sound_type_command_bytes(self, sequence_id, product_id, alarm_sound_type):

        typeof_bytes = ctypes.c_byte * self.dict_command_bytes_buffer_length[CommandID.ESetAlarmSoundType]
        temp_buffer = typeof_bytes()
        length = self.func_set_alarm_sound_type_bytes(sequence_id, product_id, alarm_sound_type,
                                                      self.dict_command_bytes_buffer_length[
                                                          CommandID.ESetAlarmSoundType], temp_buffer)
        if length != self.dict_command_bytes_buffer_length[CommandID.ESetAlarmSoundType]:
            return None
        bytes_buffer = bytes(temp_buffer)
        return bytes_buffer

    def get_alarm_sound_type_command_bytes(self, sequence_id, product_id):

        typeof_bytes = ctypes.c_byte * self.dict_command_bytes_buffer_length[CommandID.EGetAlarmSoundType]
        temp_buffer = typeof_bytes()
        length = self.func_get_alarm_sound_type_bytes(sequence_id, product_id,
                                                      self.dict_command_bytes_buffer_length[
                                                          CommandID.EGetAlarmSoundType], temp_buffer)
        if length != self.dict_command_bytes_buffer_length[CommandID.EGetAlarmSoundType]:
            return None
        bytes_buffer = bytes(temp_buffer)
        return bytes_buffer

    def set_alarm_volume_command_bytes(self, sequence_id, product_id, alarm_volume):

        typeof_bytes = ctypes.c_byte * self.dict_command_bytes_buffer_length[CommandID.ESetAlarmVolume]
        temp_buffer = typeof_bytes()
        length = self.func_set_alarm_volume_bytes(sequence_id, product_id, alarm_volume,
                                                  self.dict_command_bytes_buffer_length[
                                                      CommandID.ESetAlarmVolume], temp_buffer)
        if length != self.dict_command_bytes_buffer_length[CommandID.ESetAlarmVolume]:
            return None
        bytes_buffer = bytes(temp_buffer)
        return bytes_buffer

    def get_alarm_volume_command_bytes(self, sequence_id, product_id):
        typeof_bytes = ctypes.c_byte * self.dict_command_bytes_buffer_length[CommandID.EGetAlarmVolume]
        temp_buffer = typeof_bytes()
        length = self.func_get_alarm_volume_bytes(sequence_id, product_id,
                                                  self.dict_command_bytes_buffer_length[
                                                      CommandID.EGetAlarmVolume], temp_buffer)
        if length != self.dict_command_bytes_buffer_length[CommandID.EGetAlarmVolume]:
            return None
        bytes_buffer = bytes(temp_buffer)
        return bytes_buffer

    def get_battery_alarm_duration_command_bytes(self, sequence_id, product_id):
        typeof_bytes = ctypes.c_byte * self.dict_command_bytes_buffer_length[CommandID.EGetBatteryAlarmDuration]
        temp_buffer = typeof_bytes()
        length = self.func_get_battery_alarm_duration_bytes(sequence_id, product_id,
                                                            self.dict_command_bytes_buffer_length[
                                                                CommandID.EGetBatteryAlarmDuration], temp_buffer)
        if length != self.dict_command_bytes_buffer_length[CommandID.EGetBatteryAlarmDuration]:
            return None
        bytes_buffer = bytes(temp_buffer)
        return bytes_buffer

    def get_alarm_type_password_command_bytes(self, sequence_id, product_id):
        typeof_bytes = ctypes.c_byte * self.dict_command_bytes_buffer_length[CommandID.EGetAlarmTypePassword]
        temp_buffer = typeof_bytes()
        length = self.func_get_alarm_type_password_bytes(sequence_id, product_id,
                                                         self.dict_command_bytes_buffer_length[
                                                             CommandID.EGetAlarmTypePassword], temp_buffer)
        if length != self.dict_command_bytes_buffer_length[CommandID.EGetAlarmTypePassword]:
            return None
        bytes_buffer = bytes(temp_buffer)
        return bytes_buffer

    def get_maintenance_date_time_command_bytes(self, sequence_id, product_id):
        typeof_bytes = ctypes.c_byte * self.dict_command_bytes_buffer_length[CommandID.EGetMaintenanceDateTime]
        temp_buffer = typeof_bytes()
        length = self.func_get_maintenance_date_time_bytes(sequence_id, product_id,
                                                           self.dict_command_bytes_buffer_length[
                                                               CommandID.EGetMaintenanceDateTime], temp_buffer)
        if length != self.dict_command_bytes_buffer_length[CommandID.EGetMaintenanceDateTime]:
            return None
        bytes_buffer = bytes(temp_buffer)
        return bytes_buffer

    def get_maintenance_period_command_bytes(self, sequence_id, product_id):
        typeof_bytes = ctypes.c_byte * self.dict_command_bytes_buffer_length[CommandID.EGetMaintenancePeriod]
        temp_buffer = typeof_bytes()
        length = self.func_get_maintenance_period_bytes(sequence_id, product_id,
                                                        self.dict_command_bytes_buffer_length[
                                                            CommandID.EGetMaintenancePeriod], temp_buffer)
        if length != self.dict_command_bytes_buffer_length[CommandID.EGetMaintenancePeriod]:
            return None
        bytes_buffer = bytes(temp_buffer)
        return bytes_buffer

    def get_firmware_version_command_bytes(self, sequence_id, product_id):
        typeof_bytes = ctypes.c_byte * self.dict_command_bytes_buffer_length[CommandID.EGetFirmwareVersion]
        temp_buffer = typeof_bytes()
        length = self.func_get_firmware_version_bytes(sequence_id, product_id,
                                                      self.dict_command_bytes_buffer_length[
                                                          CommandID.EGetFirmwareVersion], temp_buffer)
        if length != self.dict_command_bytes_buffer_length[CommandID.EGetFirmwareVersion]:
            return None
        bytes_buffer = bytes(temp_buffer)
        return bytes_buffer

    def get_firmware_data_version_command_bytes(self, sequence_id, product_id, firmware_type):
        typeof_bytes = ctypes.c_byte * self.dict_command_bytes_buffer_length[CommandID.EGetFactoryFirmwareVersion]
        temp_buffer = typeof_bytes()
        length = self.func_get_firmware_data_version_bytes(sequence_id, product_id, firmware_type,
                                                           self.dict_command_bytes_buffer_length[
                                                               CommandID.EGetFactoryFirmwareVersion], temp_buffer)
        if length != self.dict_command_bytes_buffer_length[CommandID.EGetFactoryFirmwareVersion]:
            return None
        bytes_buffer = bytes(temp_buffer)
        return bytes_buffer

    def set_basic_mode_rate_unit_command_bytes(self, sequence_id, product_id, basic_mode_rate_unit):
        typeof_bytes = ctypes.c_byte * self.dict_command_bytes_buffer_length[CommandID.ESetBasicModeRateUnit]
        temp_buffer = typeof_bytes()
        length = self.func_set_basic_mode_rate_unit_bytes(sequence_id, product_id, basic_mode_rate_unit,
                                                          self.dict_command_bytes_buffer_length[
                                                              CommandID.ESetBasicModeRateUnit], temp_buffer)
        if length != self.dict_command_bytes_buffer_length[CommandID.ESetBasicModeRateUnit]:
            return None
        bytes_buffer = bytes(temp_buffer)
        return bytes_buffer

    def get_date_time_command_bytes(self, sequence_id, product_id):
        typeof_bytes = ctypes.c_byte * self.dict_command_bytes_buffer_length[CommandID.EGetDateTime]
        temp_buffer = typeof_bytes()
        length = self.func_get_date_time_bytes(sequence_id, product_id,
                                               self.dict_command_bytes_buffer_length[
                                                   CommandID.EGetDateTime], temp_buffer)
        if length != self.dict_command_bytes_buffer_length[CommandID.EGetDateTime]:
            return None
        bytes_buffer = bytes(temp_buffer)
        return bytes_buffer

    def set_date_time_command_bytes(self, sequence_id, product_id, year, month, day, hour, minute, second):
        typeof_bytes = ctypes.c_byte * self.dict_command_bytes_buffer_length[CommandID.ESetDateTime]
        temp_buffer = typeof_bytes()
        length = self.func_set_date_time_bytes(sequence_id, product_id, year, month, day, hour, minute, second,
                                               self.dict_command_bytes_buffer_length[
                                                   CommandID.ESetDateTime], temp_buffer)
        if length != self.dict_command_bytes_buffer_length[CommandID.ESetDateTime]:
            return None
        bytes_buffer = bytes(temp_buffer)
        return bytes_buffer

    def set_brightness_command_bytes(self, sequence_id, product_id, brightness_value):
        typeof_bytes = ctypes.c_byte * self.dict_command_bytes_buffer_length[CommandID.ESetBrightness]
        temp_buffer = typeof_bytes()
        length = self.func_set_brightness_bytes(sequence_id, product_id, brightness_value,
                                                self.dict_command_bytes_buffer_length[
                                                    CommandID.ESetBrightness], temp_buffer)
        if length != self.dict_command_bytes_buffer_length[CommandID.ESetBrightness]:
            return None
        bytes_buffer = bytes(temp_buffer)
        return bytes_buffer

    def get_brightness_command_bytes(self, sequence_id, product_id):
        typeof_bytes = ctypes.c_byte * self.dict_command_bytes_buffer_length[CommandID.EGetBrightness]
        temp_buffer = typeof_bytes()
        length = self.func_get_brightness_bytes(sequence_id, product_id,
                                                self.dict_command_bytes_buffer_length[
                                                    CommandID.EGetBrightness], temp_buffer)
        if length != self.dict_command_bytes_buffer_length[CommandID.EGetBrightness]:
            return None
        bytes_buffer = bytes(temp_buffer)
        return bytes_buffer

    def set_night_mode_period_command_bytes(self, sequence_id, product_id, begin_hour, begin_minute, end_hour,
                                            end_minute):
        typeof_bytes = ctypes.c_byte * self.dict_command_bytes_buffer_length[CommandID.ESetNightModePeriod]
        temp_buffer = typeof_bytes()
        length = self.func_set_night_mode_period_bytes(sequence_id, product_id, begin_hour, begin_minute, end_hour,
                                                       end_minute,
                                                       self.dict_command_bytes_buffer_length[
                                                           CommandID.ESetNightModePeriod], temp_buffer)
        if length != self.dict_command_bytes_buffer_length[CommandID.ESetNightModePeriod]:
            return None
        bytes_buffer = bytes(temp_buffer)
        return bytes_buffer

    def get_night_mode_period_command_bytes(self, sequence_id, product_id):
        typeof_bytes = ctypes.c_byte * self.dict_command_bytes_buffer_length[CommandID.EGetNightModePeriod]
        temp_buffer = typeof_bytes()
        length = self.func_get_night_mode_period_bytes(sequence_id, product_id,
                                                       self.dict_command_bytes_buffer_length[
                                                           CommandID.EGetNightModePeriod], temp_buffer)
        if length != self.dict_command_bytes_buffer_length[CommandID.EGetNightModePeriod]:
            return None
        bytes_buffer = bytes(temp_buffer)
        return bytes_buffer

    def set_night_mode_alarm_volume_command_bytes(self, sequence_id, product_id, alarm_volume):
        typeof_bytes = ctypes.c_byte * self.dict_command_bytes_buffer_length[CommandID.ESetNightModeAlarmVolume]
        temp_buffer = typeof_bytes()
        length = self.func_set_night_mode_alarm_volume_bytes(sequence_id, product_id, alarm_volume,
                                                             self.dict_command_bytes_buffer_length[
                                                                 CommandID.ESetNightModeAlarmVolume], temp_buffer)
        if length != self.dict_command_bytes_buffer_length[CommandID.ESetNightModeAlarmVolume]:
            return None
        bytes_buffer = bytes(temp_buffer)
        return bytes_buffer

    def get_night_mode_alarm_volume_command_bytes(self, sequence_id, product_id):
        typeof_bytes = ctypes.c_byte * self.dict_command_bytes_buffer_length[CommandID.EGetNightModeAlarmVolume]
        temp_buffer = typeof_bytes()
        length = self.func_get_night_mode_alarm_volume_bytes(sequence_id, product_id,
                                                             self.dict_command_bytes_buffer_length[
                                                                 CommandID.EGetNightModeAlarmVolume], temp_buffer)
        if length != self.dict_command_bytes_buffer_length[CommandID.EGetNightModeAlarmVolume]:
            return None
        bytes_buffer = bytes(temp_buffer)
        return bytes_buffer

    def set_night_mode_brightness_command_bytes(self, sequence_id, product_id, alarm_volume):

        typeof_bytes = ctypes.c_byte * self.dict_command_bytes_buffer_length[CommandID.ESetNightModeBrightness]
        temp_buffer = typeof_bytes()
        length = self.func_set_night_mode_brightness_bytes(sequence_id, product_id, alarm_volume,
                                                           self.dict_command_bytes_buffer_length[
                                                               CommandID.ESetNightModeBrightness], temp_buffer)
        if length != self.dict_command_bytes_buffer_length[CommandID.ESetNightModeBrightness]:
            return None
        bytes_buffer = bytes(temp_buffer)
        return bytes_buffer

    def get_night_mode_brightness_command_bytes(self, sequence_id, product_id):
        typeof_bytes = ctypes.c_byte * self.dict_command_bytes_buffer_length[CommandID.EGetNightModeBrightness]
        temp_buffer = typeof_bytes()
        length = self.func_get_night_mode_brightness_bytes(sequence_id, product_id,
                                                           self.dict_command_bytes_buffer_length[
                                                               CommandID.EGetNightModeBrightness], temp_buffer)
        if length != self.dict_command_bytes_buffer_length[CommandID.EGetNightModeBrightness]:
            return None
        bytes_buffer = bytes(temp_buffer)
        return bytes_buffer

    def set_switch_status_command_bytes(self, sequence_id, product_id, switch_mask, switch_status):
        typeof_bytes = ctypes.c_byte * self.dict_command_bytes_buffer_length[CommandID.ESetSecuritySwitch]
        temp_buffer = typeof_bytes()
        length = self.func_set_security_switch_bytes(sequence_id, product_id, switch_mask, switch_status,
                                                     self.dict_command_bytes_buffer_length[
                                                         CommandID.ESetSecuritySwitch], temp_buffer)
        if length != self.dict_command_bytes_buffer_length[CommandID.ESetSecuritySwitch]:
            return None
        bytes_buffer = bytes(temp_buffer)
        return bytes_buffer

    def get_switch_status_command_bytes(self, sequence_id, product_id, switch_mask):
        typeof_bytes = ctypes.c_byte * self.dict_command_bytes_buffer_length[CommandID.EGetSecuritySwitch]
        temp_buffer = typeof_bytes()
        length = self.func_get_security_switch_bytes(sequence_id, product_id, switch_mask,
                                                     self.dict_command_bytes_buffer_length[
                                                         CommandID.EGetSecuritySwitch], temp_buffer)
        if length != self.dict_command_bytes_buffer_length[CommandID.EGetSecuritySwitch]:
            return None
        bytes_buffer = bytes(temp_buffer)
        return bytes_buffer

    def clear_history_command_bytes(self, sequence_id, product_id):
        typeof_bytes = ctypes.c_byte * self.dict_command_bytes_buffer_length[CommandID.EClearHistoryLog]
        temp_buffer = typeof_bytes()
        length = self.func_clear_history_log_bytes(sequence_id, product_id,
                                                   self.dict_command_bytes_buffer_length[
                                                       CommandID.EClearHistoryLog], temp_buffer)
        if length != self.dict_command_bytes_buffer_length[CommandID.EClearHistoryLog]:
            return None
        bytes_buffer = bytes(temp_buffer)
        return bytes_buffer

    def get_log_total_num_command_bytes(self, sequence_id, product_id):
        typeof_bytes = ctypes.c_byte * self.dict_command_bytes_buffer_length[CommandID.EGetLogTotalNum]
        temp_buffer = typeof_bytes()
        length = self.func_get_log_total_num_bytes(sequence_id, product_id,
                                                   self.dict_command_bytes_buffer_length[
                                                       CommandID.EGetLogTotalNum], temp_buffer)
        if length != self.dict_command_bytes_buffer_length[CommandID.EGetLogTotalNum]:
            return None
        bytes_buffer = bytes(temp_buffer)
        return bytes_buffer

    def write_log_command_bytes(self, sequence_id, product_id, log_index):
        typeof_bytes = ctypes.c_byte * self.dict_command_bytes_buffer_length[CommandID.EWriteLog]
        temp_buffer = typeof_bytes()
        length = self.func_write_log_bytes(sequence_id, product_id, log_index,
                                           self.dict_command_bytes_buffer_length[
                                               CommandID.EWriteLog], temp_buffer)
        if length != self.dict_command_bytes_buffer_length[CommandID.EWriteLog]:
            return None
        bytes_buffer = bytes(temp_buffer)
        return bytes_buffer

    def get_log_command_bytes(self, sequence_id, product_id, log_number):
        typeof_bytes = ctypes.c_byte * self.dict_command_bytes_buffer_length[CommandID.EGetLogItem]
        temp_buffer = typeof_bytes()
        length = self.func_get_log_bytes(sequence_id, product_id, log_number,
                                         self.dict_command_bytes_buffer_length[
                                             CommandID.EGetLogItem], temp_buffer)
        if length != self.dict_command_bytes_buffer_length[CommandID.EGetLogItem]:
            return None
        bytes_buffer = bytes(temp_buffer)
        return bytes_buffer

    def restore_factory_setting_command_bytes(self, sequence_id, product_id):
        typeof_bytes = ctypes.c_byte * self.dict_command_bytes_buffer_length[CommandID.ERestoreFactorySetting]
        temp_buffer = typeof_bytes()
        length = self.func_restore_factory_setting_bytes(sequence_id, product_id,
                                                         self.dict_command_bytes_buffer_length[
                                                             CommandID.ERestoreFactorySetting], temp_buffer)
        if length != self.dict_command_bytes_buffer_length[CommandID.ERestoreFactorySetting]:
            return None
        bytes_buffer = bytes(temp_buffer)
        return bytes_buffer

    def set_tube_precision_calibration_brand_command_bytes(self, sequence_id, product_id, brand):
        typeof_bytes = ctypes.c_byte * self.dict_command_bytes_buffer_length[
            CommandID.ESetTubePrecisionCalibrationBrand]
        temp_buffer = typeof_bytes()
        length = self.func_set_tube_precision_calibration_brand_bytes(sequence_id, product_id, brand,
                                                                      self.dict_command_bytes_buffer_length[
                                                                          CommandID.ESetTubePrecisionCalibrationBrand],
                                                                      temp_buffer)
        if length != self.dict_command_bytes_buffer_length[CommandID.ESetTubePrecisionCalibrationBrand]:
            return None
        bytes_buffer = bytes(temp_buffer)
        return bytes_buffer

    def set_tube_precision_calibration_parameter_command_bytes(self, sequence_id, product_id, sequence_number,
                                                               vtbi, rate):

        typeof_bytes = ctypes.c_byte * self.dict_command_bytes_buffer_length[
            CommandID.ESetTubePrecisionCalibrationParameter]
        temp_buffer = typeof_bytes()
        length = self.func_set_tube_precision_calibration_parameter_bytes(sequence_id, product_id, sequence_number,
                                                                          vtbi, rate,
                                                                          self.dict_command_bytes_buffer_length[
                                                                              CommandID.ESetTubePrecisionCalibrationParameter],
                                                                          temp_buffer)
        if length != self.dict_command_bytes_buffer_length[CommandID.ESetTubePrecisionCalibrationParameter]:
            return None
        bytes_buffer = bytes(temp_buffer)
        return bytes_buffer

    def get_infusion_near_complete_criteria_command_bytes(self, sequence_id, product_id, ):

        typeof_bytes = ctypes.c_byte * self.dict_command_bytes_buffer_length[
            CommandID.EGetInfusionNearCompleteCriteria]
        temp_buffer = typeof_bytes()
        length = self.func_get_infusion_near_complete_criteria_bytes(sequence_id, product_id,
                                                                     self.dict_command_bytes_buffer_length[
                                                                         CommandID.EGetInfusionNearCompleteCriteria],
                                                                     temp_buffer)
        if length != self.dict_command_bytes_buffer_length[CommandID.EGetInfusionNearCompleteCriteria]:
            return None
        bytes_buffer = bytes(temp_buffer)
        return bytes_buffer

    def set_infusion_near_complete_criteria_command_bytes(self, sequence_id, product_id,
                                                          infusion_near_complete_criteria, parameters_for_criteria):

        typeof_bytes = ctypes.c_byte * self.dict_command_bytes_buffer_length[
            CommandID.ESetInfusionNearCompleteCriteria]
        temp_buffer = typeof_bytes()
        length = self.func_set_infusion_near_complete_criteria_bytes(sequence_id, product_id,
                                                                     infusion_near_complete_criteria,
                                                                     parameters_for_criteria,
                                                                     self.dict_command_bytes_buffer_length[
                                                                         CommandID.ESetInfusionNearCompleteCriteria],
                                                                     temp_buffer)
        if length != self.dict_command_bytes_buffer_length[CommandID.ESetInfusionNearCompleteCriteria]:
            return None
        bytes_buffer = bytes(temp_buffer)
        return bytes_buffer

    def get_bubble_sensitivity_command_bytes(self, sequence_id, product_id, air_detection_option):

        typeof_bytes = ctypes.c_byte * self.dict_command_bytes_buffer_length[
            CommandID.EGetBubbleSensitivity]
        temp_buffer = typeof_bytes()
        length = self.func_get_bubble_sensitivity_bytes(sequence_id, product_id, air_detection_option,
                                                        self.dict_command_bytes_buffer_length[
                                                            CommandID.EGetBubbleSensitivity],
                                                        temp_buffer)
        if length != self.dict_command_bytes_buffer_length[CommandID.EGetBubbleSensitivity]:
            return None
        bytes_buffer = bytes(temp_buffer)
        return bytes_buffer

    def set_bubble_sensitivity_command_bytes(self, sequence_id, product_id, air_detection_option, bubble_sensitivity):

        typeof_bytes = ctypes.c_byte * self.dict_command_bytes_buffer_length[
            CommandID.ESetBubbleSensitivity]
        temp_buffer = typeof_bytes()
        length = self.func_set_bubble_sensitivity_bytes(sequence_id, product_id, air_detection_option,
                                                        bubble_sensitivity,
                                                        self.dict_command_bytes_buffer_length[
                                                            CommandID.ESetBubbleSensitivity],
                                                        temp_buffer)
        if length != self.dict_command_bytes_buffer_length[CommandID.ESetBubbleSensitivity]:
            return None
        bytes_buffer = bytes(temp_buffer)
        return bytes_buffer

    def get_sensor_status_command_bytes(self, sequence_id, product_id, sensor_mask):

        typeof_bytes = ctypes.c_byte * self.dict_command_bytes_buffer_length[
            CommandID.EGetSensorStatus]
        print(typeof_bytes)
        temp_buffer = typeof_bytes()
        print(type(temp_buffer))
        length = self.func_get_sensor_status_bytes(sequence_id, product_id, sensor_mask,
                                                   self.dict_command_bytes_buffer_length[
                                                       CommandID.EGetSensorStatus],
                                                   temp_buffer)
        if length != self.dict_command_bytes_buffer_length[CommandID.EGetSensorStatus]:
            return None
        bytes_buffer = bytes(temp_buffer)
        return bytes_buffer

    def get_current_drug_command_bytes(self, sequence_id, product_id):

        typeof_bytes = ctypes.c_byte * self.dict_command_bytes_buffer_length[CommandID.EGetCurrentDrug]
        temp_buffer = typeof_bytes()
        length = self.func_get_current_drug_bytes(sequence_id, product_id,
                                                  self.dict_command_bytes_buffer_length[CommandID.EGetCurrentDrug],
                                                  temp_buffer)
        if length != self.dict_command_bytes_buffer_length[CommandID.EGetCurrentDrug]:
            return None
        bytes_buffer = bytes(temp_buffer)
        return bytes_buffer

    def set_current_drug_command_bytes(self, sequence_id, product_id, drug_index):

        typeof_bytes = ctypes.c_byte * self.dict_command_bytes_buffer_length[CommandID.ESetCurrentDrug]
        temp_buffer = typeof_bytes()
        length = self.func_set_current_drug_bytes(sequence_id, product_id, drug_index,
                                                  self.dict_command_bytes_buffer_length[CommandID.ESetCurrentDrug],
                                                  temp_buffer)
        if length != self.dict_command_bytes_buffer_length[CommandID.ESetCurrentDrug]:
            return None
        bytes_buffer = bytes(temp_buffer)
        return bytes_buffer

    def remote_start_prime_command_bytes(self, sequence_id, product_id, prime):

        typeof_bytes = ctypes.c_byte * self.dict_command_bytes_buffer_length[CommandID.ERemoteStartPrime]
        temp_buffer = typeof_bytes()
        length = self.func_start_prime_bytes(sequence_id, product_id, prime,
                                             self.dict_command_bytes_buffer_length[CommandID.ERemoteStartPrime],
                                             temp_buffer)
        if length != self.dict_command_bytes_buffer_length[CommandID.ERemoteStartPrime]:
            return None
        bytes_buffer = bytes(temp_buffer)
        return bytes_buffer

    def remote_start_bolus_command_bytes(self, sequence_id, product_id, bolus):

        typeof_bytes = ctypes.c_byte * self.dict_command_bytes_buffer_length[CommandID.ERemoteStartBolus]
        temp_buffer = typeof_bytes()
        length = self.func_start_bolus_bytes(sequence_id, product_id, bolus,
                                             self.dict_command_bytes_buffer_length[CommandID.ERemoteStartBolus],
                                             temp_buffer)
        if length != self.dict_command_bytes_buffer_length[CommandID.ERemoteStartBolus]:
            return None
        bytes_buffer = bytes(temp_buffer)
        return bytes_buffer

    def remote_set_bolus_parameter_command_bytes(self, sequence_id, product_id, bolus_rate, bolus_volume):

        typeof_bytes = ctypes.c_byte * self.dict_command_bytes_buffer_length[CommandID.ERemoteSetBolusParameter]
        temp_buffer = typeof_bytes()
        length = self.func_set_bolus_parameter_bytes(sequence_id, product_id, bolus_rate, bolus_volume,
                                                     self.dict_command_bytes_buffer_length[
                                                         CommandID.ERemoteSetBolusParameter],
                                                     temp_buffer)
        if length != self.dict_command_bytes_buffer_length[CommandID.ERemoteSetBolusParameter]:
            return None
        bytes_buffer = bytes(temp_buffer)
        return bytes_buffer

    # def verify_passcode_command_bytes(self, sequence_id, product_id, screen_type, length, passcode):
    #     typeof_bytes = ctypes.c_byte * self.dict_command_bytes_buffer_length[CommandID.EVerifyPasscode]
    #     temp_buffer = typeof_bytes()
    #     p = ctypes.c_byte(passcode)
    #     pointer = ctypes.byref(p)
    #     length = self.func_verify_passcode_bytes(sequence_id, product_id, screen_type, length, pointer,
    #                                              self.dict_command_bytes_buffer_length[
    #                                                  CommandID.EVerifyPasscode], temp_buffer)
    #     if length != self.dict_command_bytes_buffer_length[CommandID.EVerifyPasscode]:
    #         return None
    #     bytes_buffer = bytes(temp_buffer)
    #     print(bytes_buffer)
    #     print(bytes_to_hex_string(bytes_buffer))
    #     return bytes_buffer
    #
    #
    #
    # def verify_passcode_command_bytes1(self, sequence_id, product_id, screen_type, length, passcode):
    #     typeof_bytes = ctypes.c_byte * self.dict_command_bytes_buffer_length[CommandID.EVerifyPasscode]
    #     temp_buffer = typeof_bytes()
    #     typeof_bytes1 = ctypes.c_byte * 4
    #     temp_buffer1 = typeof_bytes1(passcode)
    #     # temp_buffer1.
    #     length = self.func_verify_passcode_bytes(sequence_id, product_id, screen_type, length, temp_buffer1,
    #                                              self.dict_command_bytes_buffer_length[
    #                                                  CommandID.EVerifyPasscode], temp_buffer)
    #     if length != self.dict_command_bytes_buffer_length[CommandID.EVerifyPasscode]:
    #         return None
    #     bytes_buffer = bytes(temp_buffer)
    #     print(bytes_to_hex_string(bytes_buffer))
    #     return bytes_buffer


def bytes_to_hex_string(buffer):
    # hex_str = ''
    # for item in bs:
    #     hex_str += str(hex(item))[2:].zfill(2).upper() + " "
    # return hex_str
    return ''.join(['%02X ' % b for b in buffer])


if __name__ == '__main__':
    a = ProtocolParserInvoker(r'C:/Users/mshacxiang/PumpLibrary/ParserProtocol/ProtocolParser_x64.dll')
    b = a.get_infusion_mode_command_bytes(1, 2)
    c = bytes_to_hex_string(b)
    print(c)
