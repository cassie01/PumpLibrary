# -*-coding:utf-8 -*-

from Keywords.keywordgroup import KeywordGroup


class Priming(KeywordGroup):
    """
    This class is used to define all related methods with priming.
    """

    def start_prime(self):
        """
        This method is used to start prime.
        :return: None
        """
        request_command = self.parser_invoker.remote_start_prime_command_bytes(self.sequence_id,
                                                                                       self.product_id, 1)
        response_command_content = self.connectObj.send_receive_command(request_command)
        return response_command_content

    def stop_prime(self):
        """
        This method is used to stop prime.
        :return: None
        """
        request_command = self.parser_invoker.remote_start_prime_command_bytes(self.sequence_id,
                                                                                       self.product_id, 0)
        response_command_content = self.connectObj.send_receive_command(request_command)
        return response_command_content

