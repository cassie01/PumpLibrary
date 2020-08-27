# -*-coding:utf-8 -*-

from Keywords.keywordgroup import KeywordGroup


class Info(KeywordGroup):
    """
    This class is used to define all related methods with information.
    """

    def get_system_status(self):
        """
        This method is used to get system status.
        :return: system status
        """
        request_command = self.parser_invoker.get_system_status_command_bytes(self.sequence_id, self.product_id)
        response_command_content = self.connectObj.send_receive_command(request_command)
        return response_command_content







    def get_basic_mode_rate_unit(self):
        """
        This method is used to get rate unit on basic mode.
        :return: rate unit
        """
        request_command = self.parser_invoker.get_basic_mode_rate_unit_command_bytes(self.sequence_id, self.product_id)
        response_command_content = self.connectObj.send_receive_command(request_command)
        return response_command_content

    def get_switch_status(self, switch_mask):
        """
        This method is used to get switch status.
        :param switch_mask:
                            contain one or more switch:
                            Edit rate at run time    0x01
                            Locked after startup    0x02
                            Save last infusion program    0x04
                            Night mode    0x08
                            Automatic brand recognition    0x10
                            Drug store    0x20
                            Touch-tone    0x40
                            Drop speed sensor    0x80
                            Delayed infusion using KVO rate    0x100
                            Delayed infusion    0x200
        :return: switch status
        """
        # if switch_mask == "savelastinfusionprocedure":
        #     switch_mask = 0x04
        # elif switch_mask == "nightmode":
        #     switch_mask = 0x08
        # elif switch_mask == "keytone":
        #     switch_mask = 0x40
        # elif switch_mask == "delaystart":
        #     switch_mask = 0x200
        # else:
        #     print("Invalid switch_mask!")
        #     return
        request_command = self.parser_invoker.get_switch_status_command_bytes(self.sequence_id, self.product_id,
                                                                              switch_mask)
        response_command_content = self.connectObj.send_receive_command(request_command)
        return response_command_content

    def set_switch_status(self, switch_mask, switch_status):
        """
        This method is used to set switch status.
        :param switch_mask:
                            contain one or more switch:
                            Edit rate at run time    0x01
                            Locked after startup    0x02
                            Save last infusion program    0x04
                            Night mode    0x08
                            Automatic brand recognition    0x10
                            Drug store    0x20
                            Touch-tone    0x40
                            Drop speed sensor    0x80
                            Delayed infusion using KVO rate    0x100
                            Delayed infusion    0x200
        :param switch_status:
                             switch status:
                             Off    0x00
                             On    0x01
        :return: None
        """
        # if switch_mask == "savelastinfusionprocedure":
        #     switch_mask = 0x04
        #     if switch_status == "on":
        #         switch_status = 0x04
        #     elif switch_status == "off":
        #         switch_status = 0x00
        #     else:
        #         print("Unexpected switch_status!")
        #         return
        # elif switch_mask == "nightmode":
        #     switch_mask = 0x08
        #     if switch_status == "on":
        #         switch_status = 0x08
        #     elif switch_status == "off":
        #         switch_status = 0x00
        #     else:
        #         print("Unexpected switch_status!")
        #         return
        # elif switch_mask == "keytone":
        #     switch_mask = 0x40
        #     if switch_status == "on":
        #         switch_status = 0x40
        #     elif switch_status == "off":
        #         switch_status = 0x00
        #     else:
        #         print("Unexpected switch_status!")
        #         return
        # elif switch_mask == "delaystart":
        #     switch_mask = 0x200
        #     if switch_status == "on":
        #         switch_status = 0x200
        #     elif switch_status == "off":
        #         switch_status = 0x00
        #     else:
        #         print("Unexpected switch_status!")
        #         return
        # else:
        #     print("Invalid switch_mask!")
        #     return

        request_command = self.parser_invoker.set_switch_status_command_bytes(self.sequence_id, self.product_id,
                                                                              switch_mask,
                                                                              switch_status)
        response_command_content = self.connectObj.send_receive_command(request_command)
        return response_command_content
