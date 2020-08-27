# -*-coding:utf-8 -*-

from Keywords.keywordgroup import KeywordGroup


class DeviceReport(KeywordGroup):
    """
    This class is used to define all related methods with device report.
    """

    def get_maintenance_date_time(self):
        """
        This method is used to get maintenance date time.
        :return: date time
        """
        request_command = self.parser_invoker.get_maintenance_date_time_command_bytes(self.sequence_id, self.product_id)
        response_command_content = self.connectObj.send_receive_command(request_command)
        return response_command_content

    def get_maintenance_period(self):
        """
        This method is used to get maintenance period.
        :return: maintenance period(unit:month)
        """
        request_command = self.parser_invoker.get_maintenance_period_command_bytes(self.sequence_id, self.product_id)
        response_command_content = self.connectObj.send_receive_command(request_command)
        return response_command_content

    def get_firmware_version(self):
        """
        This method is used to get firmware version.
        :return: (MainFirmware, UIFirmware, MainBootloader, UIBootloader, SafetyFirmware, SafetyBootloaderFirmware)
        """
        request_command = self.parser_invoker.get_firmware_version_command_bytes(self.sequence_id, self.product_id)
        response_command_content = self.connectObj.send_receive_command(request_command)
        return response_command_content

    def get_firmware_data_version(self, firmware_type):
        """
        This method is used to get firmware data version.
        :param firmware_type:
                            UI/Master Flash Data	0x04
                            Drug Library	0x06
                            Voice Image	0x08
        :return: (Firmware Type、Major Version、Minor Version、Revision Version、Build Number Version)
        """
        request_command = self.parser_invoker.get_firmware_data_version_command_bytes(self.sequence_id, self.product_id,
                                                                                      firmware_type)
        response_command_content = self.connectObj.send_receive_command(request_command)
        return response_command_content

    def get_serial_number(self):
        """
        This method is used to get pump serial number.
        :return: serial number
        """
        request_command = self.parser_invoker.get_serial_number_command_bytes(self.sequence_id, self.product_id)
        response_command_content = self.connectObj.send_receive_command(request_command)
        return response_command_content
