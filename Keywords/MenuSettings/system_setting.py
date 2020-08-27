# -*-coding:utf-8 -*-

from Keywords.keywordgroup import KeywordGroup


class SystemSetting(KeywordGroup):
    """
    This class is used to define all related methods with system setting.
    """

    def get_date_time(self):
        """
        This method is used to get date time.
        :return: date time
        """
        request_command = self.parser_invoker.get_date_time_command_bytes(self.sequence_id, self.product_id)
        response_command_content = self.connectObj.send_receive_command(request_command)
        return response_command_content

    def set_date_time(self, year, month, day, hour, minute, second):
        """
        This method is used to set pump date time.
        :param: year, month, day, hour, minute, second: number
        :return: None
        """
        request_command = self.parser_invoker.set_date_time_command_bytes(self.sequence_id, self.product_id, year,
                                                                          month, day,
                                                                          hour, minute, second)
        response_command_content = self.connectObj.send_receive_command(request_command)
        return response_command_content

    def get_brightness(self):
        """
        This method is used to get brightness.
        :return: brightness
        """
        request_command = self.parser_invoker.get_brightness_command_bytes(self.sequence_id, self.product_id)
        response_command_content = self.connectObj.send_receive_command(request_command)
        return response_command_content

    def set_brightness(self, brightness_value):
        """
        This method is used to set pump brightness.
        :param brightness_value: (1~10)
        :return: None
        """
        request_command = self.parser_invoker.set_brightness_command_bytes(self.sequence_id, self.product_id,
                                                                           brightness_value)
        response_command_content = self.connectObj.send_receive_command(request_command)
        return response_command_content

    def get_night_mode_switch_status(self):
        """
        This method is used to get night mode switch status.
        :return: switch status
        """
        request_command = self.parser_invoker.get_switch_status_command_bytes(self.sequence_id, self.product_id,
                                                                              0x08)
        response_command_content = self.connectObj.send_receive_command(request_command)
        return response_command_content

    def set_night_mode_switch_status(self, switch_status):
        """
        This method is used to set night mode switch status.
        :param switch_status:
                             Off    0x00
                             On    0x08
        :return: None
        """
        if switch_status == "Off":
            switch_status = 0x00
        elif switch_status == "On":
            switch_status = 0x08
        else:
            print("Invalid parameter!")
            return
        request_command = self.parser_invoker.set_switch_status_command_bytes(self.sequence_id, self.product_id,
                                                                              0x08,
                                                                              switch_status)
        response_command_content = self.connectObj.send_receive_command(request_command)
        return response_command_content

    def get_night_mode_period(self):
        """
        This method is used to get night mode period.
        :return: time
        """
        request_command = self.parser_invoker.get_night_mode_period_command_bytes(self.sequence_id, self.product_id)
        response_command_content = self.connectObj.send_receive_command(request_command)
        return response_command_content

    def set_night_mode_period(self, begin_hour, begin_minute, end_hour, end_minute):
        """
        This method is used to set night mode period.
        :param  begin_hour, begin_minute, end_hour, end_minute: number
        :return: None
        """
        request_command = self.parser_invoker.set_night_mode_period_command_bytes(self.sequence_id, self.product_id,
                                                                                  begin_hour,
                                                                                  begin_minute, end_hour, end_minute)
        response_command_content = self.connectObj.send_receive_command(request_command)
        return response_command_content

    def get_night_mode_alarm_volume(self):
        """
        This method is used to get night mode alarm volume.
        :return: alarm volume
        """
        request_command = self.parser_invoker.get_night_mode_alarm_volume_command_bytes(self.sequence_id,
                                                                                        self.product_id)
        response_command_content = self.connectObj.send_receive_command(request_command)
        return response_command_content

    def set_night_mode_alarm_volume(self, volume):
        """
        This method is used to set night mode alarm volume.
        :param volume: (1~5)
        :return: None
        """
        request_command = self.parser_invoker.set_night_mode_alarm_volume_command_bytes(self.sequence_id,
                                                                                        self.product_id,
                                                                                        volume)
        response_command_content = self.connectObj.send_receive_command(request_command)
        return response_command_content

    def get_night_mode_brightness(self):
        """
        This method is used to get night mode brightness.
        :return: brightness
        """
        request_command = self.parser_invoker.get_night_mode_brightness_command_bytes(self.sequence_id, self.product_id)
        response_command_content = self.connectObj.send_receive_command(request_command)
        return response_command_content

    def set_night_mode_brightness(self, brightness):
        """
        This method is used to set night mode brightness.
        :param brightness: (1~10)
        :return: None
        """
        request_command = self.parser_invoker.set_night_mode_brightness_command_bytes(self.sequence_id, self.product_id,
                                                                                      brightness)
        response_command_content = self.connectObj.send_receive_command(request_command)
        return response_command_content

    def get_touch_tone_switch_status(self):
        """
        This method is used to get touch tone switch status.
        :return: switch status
        """
        request_command = self.parser_invoker.get_switch_status_command_bytes(self.sequence_id, self.product_id,
                                                                              0x40)
        response_command_content = self.connectObj.send_receive_command(request_command)
        return response_command_content

    def set_touch_tone_switch_status(self, switch_status):
        """
        This method is used to set touch tone switch status.
        :param switch_status:
                             Off    0x00
                             On    64
        :return: None
        """
        if switch_status == "Off":
            switch_status = 0x00
        elif switch_status == "On":
            switch_status = 64
        else:
            print("Invalid parameter!")
            return
        request_command = self.parser_invoker.set_switch_status_command_bytes(self.sequence_id, self.product_id,
                                                                              0x40,
                                                                              switch_status)
        response_command_content = self.connectObj.send_receive_command(request_command)
        return response_command_content
