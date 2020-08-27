# -*-coding:utf-8 -*-

from Keywords.keywordgroup import KeywordGroup


class Bolus(KeywordGroup):
    """
    This class is used to define all related methods with bolus.
    """

    def start_bolus(self):
        """
        This method is used to start bolus.
        :return: None
        """
        request_command = self.parser_invoker.remote_start_bolus_command_bytes(self.sequence_id,
                                                                               self.product_id, 1)
        response_command_content = self.connectObj.send_receive_command(request_command)
        return response_command_content

    def stop_bolus(self):
        """
        This method is used to stop bolus.
        :return: None
        """
        request_command = self.parser_invoker.remote_start_bolus_command_bytes(self.sequence_id,
                                                                               self.product_id, 0)
        response_command_content = self.connectObj.send_receive_command(request_command)
        return response_command_content

    def set_bolus_parameter(self, bolus_rate, bolus_volume):
        """
        This method is used to set bolus parameter.
        :return: None
        """
        request_command = self.parser_invoker.remote_set_bolus_parameter_command_bytes(self.sequence_id,
                                                                               self.product_id, bolus_rate, bolus_volume)
        response_command_content = self.connectObj.send_receive_command(request_command)
        return response_command_content

