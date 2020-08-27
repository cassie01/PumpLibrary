# -*-coding:utf-8 -*-

from Keywords.keywordgroup import KeywordGroup


class SafetySetting(KeywordGroup):
    """
    This class is used to define all related methods with safety setting.
    """

    def get_edit_rate_at_run_time_switch_status(self):
        """
        This method is used to get edit rate at run time switch status.
        :return: switch status
        """
        request_command = self.parser_invoker.get_switch_status_command_bytes(self.sequence_id, self.product_id,
                                                                              0x01)
        response_command_content = self.connectObj.send_receive_command(request_command)
        return response_command_content

    def set_edit_rate_at_run_time_switch_status(self, switch_status):
        """
        This method is used to set edit rate at run time switch status.
        :param switch_status:
                             Off    0x00
                             On    0x01
        :return: None
        """
        if switch_status == "Off":
            switch_status = 0x00
        elif switch_status == "On":
            switch_status = 0x01
        else:
            print("Invalid parameter!")
            return

        request_command = self.parser_invoker.set_switch_status_command_bytes(self.sequence_id, self.product_id,
                                                                              0x01,
                                                                              switch_status)
        response_command_content = self.connectObj.send_receive_command(request_command)
        return response_command_content

    def get_keypad_lock_switch_status(self):
        """
        This method is used to get keypad lock switch status.
        :return: switch status
        """
        request_command = self.parser_invoker.get_switch_status_command_bytes(self.sequence_id, self.product_id,
                                                                              0x02)
        response_command_content = self.connectObj.send_receive_command(request_command)
        return response_command_content

    def set_keypad_lock_switch_status(self, switch_status):
        """
        This method is used to set keypad lock switch status.
        :param switch_status:
                             Off    0x00
                             On    0x02
        :return: None
        """
        if switch_status == "Off":
            switch_status = 0x00
        elif switch_status == "On":
            switch_status = 0x02
        else:
            print("Invalid parameter!")
            return
        request_command = self.parser_invoker.set_switch_status_command_bytes(self.sequence_id, self.product_id,
                                                                              0x02,
                                                                              switch_status)
        response_command_content = self.connectObj.send_receive_command(request_command)
        return response_command_content

    def get_alarm_volume(self):
        """
        This method is used to get pump alarm volume.
        :return: alarm volume
        """
        request_command = self.parser_invoker.get_alarm_volume_command_bytes(self.sequence_id, self.product_id)
        response_command_content = self.connectObj.send_receive_command(request_command)
        return response_command_content

    def set_alarm_volume(self, alarm_volume):
        """
        This method is used to set pump alarm volume.
        :param alarm_volume: (1~5)
        :return: None
        """
        request_command = self.parser_invoker.set_alarm_volume_command_bytes(self.sequence_id, self.product_id,
                                                                             alarm_volume)
        response_command_content = self.connectObj.send_receive_command(request_command)
        return response_command_content

    def get_infusion_near_complete_criteria(self):
        """
        This method is used to get infusion near complete criteria.
        :return: Infusion Near Complete Criteria/Parameters for Criteria(uint,4 byte)
        """
        request_command = self.parser_invoker.get_infusion_near_complete_criteria_command_bytes(self.sequence_id,
                                                                                                self.product_id,
                                                                                                )
        response_command_content = self.connectObj.send_receive_command(request_command)
        return response_command_content

    def set_infusion_near_complete_criteria(self, infusion_near_complete_criteria, parameters_for_criteria):
        """
        This method is used to set infusion near complete criteria.
        :param infusion_near_complete_criteria: By Time	0x00
                                                By Volume	0x01
                                                Off	0x02
               parameters_for_criteria: value
        :return: None
        """
        if infusion_near_complete_criteria == "ByTime":
            infusion_near_complete_criteria = 0x00
        elif infusion_near_complete_criteria == "ByVolume":
            infusion_near_complete_criteria = 0x01
        elif infusion_near_complete_criteria == "Off":
            infusion_near_complete_criteria = 0x02
        else:
            print("Invalid parameter!")
            return
        request_command = self.parser_invoker.set_infusion_near_complete_criteria_command_bytes(self.sequence_id,
                                                                                                self.product_id,
                                                                                                infusion_near_complete_criteria,
                                                                                                parameters_for_criteria
                                                                                                )
        response_command_content = self.connectObj.send_receive_command(request_command)
        return response_command_content

    def get_bubble_sensitivity(self, air_detection_option):
        """
        This method is used to get bubble sensitivity.
        :param air_detection_option:
                                    Both	0x00
                                    Single bubble	0x01
                                    Multiple bubble	0x02
        :return: Air Detection Option & Bubble Sensitivity
        """
        request_command = self.parser_invoker.get_bubble_sensitivity_command_bytes(self.sequence_id, self.product_id,
                                                                                   air_detection_option)
        response_command_content = self.connectObj.send_receive_command(request_command)
        return response_command_content

    def set_bubble_sensitivity(self, air_detection_option, bubble_sensitivity):
        """
        This method is used to set bubble sensitivity.
        :param air_detection_option:
                                    Both	0x00
                                    Single bubble	0x01
                                    Multiple bubble	0x02
        :param bubble_sensitivity:
                                 Low	0x00
                                 Medium	 0x01
                                 High	 0x02
        :return: None
        """
        request_command = self.parser_invoker.set_bubble_sensitivity_command_bytes(self.sequence_id, self.product_id,
                                                                                   air_detection_option,
                                                                                   bubble_sensitivity
                                                                                   )
        response_command_content = self.connectObj.send_receive_command(request_command)
        return response_command_content

    def get_drip_sensor_switch_status(self):
        """
        This method is used to get drip sensor switch status.
        :return: switch status
        """
        request_command = self.parser_invoker.get_switch_status_command_bytes(self.sequence_id, self.product_id,
                                                                              0x80)
        response_command_content = self.connectObj.send_receive_command(request_command)
        return response_command_content

    def set_drip_sensor_switch_status(self, switch_status):
        """
        This method is used to set drip sensor switch status.
        :param switch_status:
                             Off    0x00
                             On    0x80
        :return: None
        """
        request_command = self.parser_invoker.set_switch_status_command_bytes(self.sequence_id, self.product_id,
                                                                              0x80,
                                                                              switch_status)
        response_command_content = self.connectObj.send_receive_command(request_command)
        return response_command_content
