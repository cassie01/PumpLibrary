# -*-coding:utf-8 -*-

from Keywords.keywordgroup import KeywordGroup


class Alarm(KeywordGroup):
    """
    This class is used to define all related methods with alarm.
    """

    def get_pump_alarm(self):
        """
        This method is used to get pump alarm id.
        :return: alarm id
        """
        request_command = self.parser_invoker.get_pump_alarm_command_bytes(self.sequence_id, self.product_id)
        response_command_content = self.connectObj.send_receive_command(request_command)
        return response_command_content

    def get_alarm_name(self, alarm_index):
        """
        This method is used to get pump alarm name.
        Notice: Only for English language on pump.
        :param alarm_index: (0~46)
        :return: alarm name
        """
        request_command = self.parser_invoker.get_alarm_name_command_bytes(self.sequence_id, self.product_id,
                                                                           alarm_index)
        response_command_content = self.connectObj.send_receive_command(request_command)
        return response_command_content

    def get_alarm_count(self):
        """
        This method is used to get pump alarm count.
        :return: alarm count
        """
        request_command = self.parser_invoker.get_alarm_count_command_bytes(self.sequence_id, self.product_id)
        response_command_content = self.connectObj.send_receive_command(request_command)
        return response_command_content
