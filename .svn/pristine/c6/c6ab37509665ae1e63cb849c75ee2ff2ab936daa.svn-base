# -*-coding:utf-8 -*-

from Keywords.keywordgroup import KeywordGroup


class HistoryLog(KeywordGroup):
    """
    This class is used to define all related methods with history log.
    """

    def get_log_total_num(self):
        """
        This method is used to get log total number.
        :return: log total number
        """
        request_command = self.parser_invoker.get_log_total_num_command_bytes(self.sequence_id, self.product_id)
        response_command_content = self.connectObj.send_receive_command(request_command)
        return response_command_content

    def get_log(self, log_number):
        """
        This method is used to get pump log.
        :param log_number: (1~max)
        :return: log information
        """
        request_command = self.parser_invoker.get_log_command_bytes(self.sequence_id, self.product_id, log_number)
        response_command_content = self.connectObj.send_receive_command(request_command)
        return response_command_content

    def write_log(self, log_index):
        """
        This method is used to write log to pump.
        :param log_index: (0~max)
        :return: None
        """
        request_command = self.parser_invoker.write_log_command_bytes(self.sequence_id, self.product_id, log_index)
        response_command_content = self.connectObj.send_receive_command(request_command)
        return response_command_content

    def clear_history_log(self):
        """
        This method is used to clear pump history log.
        :return: None
        """
        request_command = self.parser_invoker.clear_history_command_bytes(self.sequence_id, self.product_id)
        response_command_content = self.connectObj.send_receive_command(request_command)
        return response_command_content
