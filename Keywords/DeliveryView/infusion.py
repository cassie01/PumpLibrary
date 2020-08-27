# -*-coding:utf-8 -*-

from Keywords.keywordgroup import KeywordGroup


class Infusion(KeywordGroup):
    """
    This class is used to define all related methods with infusion.
    """

    def start_infusion(self):
        """
        This method is used to start infusion.
        :return: None
        """
        request_command = self.parser_invoker.remote_start_stop_infusion_command_bytes(self.sequence_id,
                                                                                       self.product_id, 1)
        response_command_content = self.connectObj.send_receive_command(request_command)
        return response_command_content

    def stop_infusion(self):
        """
        This method is used to stop infusion.
        :return: None
        """
        request_command = self.parser_invoker.remote_start_stop_infusion_command_bytes(self.sequence_id,
                                                                                       self.product_id, 0)
        response_command_content = self.connectObj.send_receive_command(request_command)
        # return response_command_content
