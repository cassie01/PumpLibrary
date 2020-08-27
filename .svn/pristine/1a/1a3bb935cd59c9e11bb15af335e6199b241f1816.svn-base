# -*-coding:utf-8 -*-

from Keywords.keywordgroup import KeywordGroup


class Maintenance(KeywordGroup):
    """
    This class is used to define all related methods with device maintenance.
    """

    # TODO unfinished
    def verify_passcode(self, screen_type, length, passcode):
        """
        This method is used to verify passcode.
        :param screen_type: Safety	0x00, Maintenance	0x01
               passcode: custom field
        :return: screen_type: Safety	0x00, Maintenance	0x01
                 Success：1/Fail：0
        """
        request_command = self.parser_invoker.verify_passcode_command_bytes(self.sequence_id, self.product_id,
                                                                            screen_type, length, passcode)
        response_command_content = self.connectObj.send_receive_command(request_command)
        return response_command_content

    def get_alarm_sound_type(self):
        """
        This method is used to get pump alarm sound type.
        :return: alarm sound type
        """
        request_command = self.parser_invoker.get_alarm_sound_type_command_bytes(self.sequence_id, self.product_id)
        response_command_content = self.connectObj.send_receive_command(request_command)
        return response_command_content

    def set_alarm_sound_type(self, alarm_sound_type):
        """
        This method is used to set pump alarm sound type.
        :param alarm_sound_type: (1~3)
        :return: None
        """
        request_command = self.parser_invoker.set_alarm_sound_type_command_bytes(self.sequence_id, self.product_id,
                                                                                 alarm_sound_type)
        response_command_content = self.connectObj.send_receive_command(request_command)
        return response_command_content

    def set_tube_precision_calibration_brand(self, brand):
        """
        This method is used to set tube precision calibration brand.
        :param brand:
                    Brand1	0x00
                    Brand2	0x01
                    Brand3	0x02
                    Brand4	0x03
                    Brand5	0x04
                    Brand6	0x05
                    Brand7	0x06
                    Brand8	0x07
                    Brand9	0x08
                    Brand10	0x09
                    Brand11	0x0A
                    Brand12	0x0B
                    Brand13	0x0C
                    CustomBrand1	0x80
                    CustomBrand2	0x81
                    CustomBrand3	0x82
                    CustomBrand4	0x83
                    CustomBrand5	0x84
        :return: 1:OK/0:Fail
        """
        request_command = self.parser_invoker.set_tube_precision_calibration_brand_command_bytes(self.sequence_id,
                                                                                                 self.product_id, brand)
        response_command_content = self.connectObj.send_receive_command(request_command)
        return response_command_content

    # TODO unfinished
    def set_tube_precision_calibration_parameter(self, sequence_number, vtbi, rate):
        """
        This method is used to set tube precision calibration parameter.
        :param sequence_number: (1~max)
                vtbi: valid number
                rate: valid number
        :return:
                sequence number
                1:OK/0:Fail
        """
        request_command = self.parser_invoker.set_tube_precision_calibration_parameter_command_bytes(self.sequence_id,
                                                                                                     self.product_id,
                                                                                                     sequence_number,
                                                                                                     vtbi,
                                                                                                     rate)
        response_command_content = self.connectObj.send_receive_command(request_command)
        return response_command_content

    def restore_factory_setting(self):
        """
        This method is used to restore factory setting.
        :return: None
        """
        request_command = self.parser_invoker.restore_factory_setting_command_bytes(self.sequence_id, self.product_id)
        response_command_content = self.connectObj.send_receive_command(request_command)
        return response_command_content
