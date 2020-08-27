# -*-coding:utf-8 -*-

from Keywords.keywordgroup import KeywordGroup


class Sensor(KeywordGroup):
    """
    This class is used to define all related methods with sensor.
    """

    def get_sensor_status(self, sensor_mask):
        """
        This method is used to get the sensor status.
        :param sensor_mask:
                            Sensor	    Value	pump
                            压力传感器	0x01	C9
                            尺寸传感器	0x02	C9
                            门传感器	    0x04	LVP
                            滴速传感器	0x08	LVP
                            气泡传感器	0x10	LVP
                            速度传感器	0x20	LVP
                            WIFI	    0x40	LVP
                                        0x80
        :return: sensor mask and sensor status(NOT INSTALL	0x00/INSTALL	0x01)
        """
        request_command = self.parser_invoker.get_sensor_status_command_bytes(self.sequence_id, self.product_id,
                                                                              sensor_mask)
        response_command_content = self.connectObj.send_receive_command(request_command)
        return response_command_content

    def get_pressure_sensor_status(self):
        """
        This method is used to get the pressure sensor status.
        :return: sensor mask and sensor status(NOT INSTALL	0x00/INSTALL	0x01)
        """
        request_command = self.parser_invoker.get_sensor_status_command_bytes(self.sequence_id, self.product_id, 0x01)
        response_command_content = self.connectObj.send_receive_command(request_command)
        return response_command_content

    def get_size_sensor_status(self):
        """
        This method is used to get the size sensor status.
        :return: sensor mask and sensor status(NOT INSTALL	0x00/INSTALL	0x02)
        """
        request_command = self.parser_invoker.get_sensor_status_command_bytes(self.sequence_id, self.product_id, 0x02)
        response_command_content = self.connectObj.send_receive_command(request_command)
        return response_command_content

    def get_door_sensor_status(self):
        """
        This method is used to get the door sensor status.
        :return: sensor mask and sensor status(NOT INSTALL	0x00/INSTALL	0x04)
        """
        request_command = self.parser_invoker.get_sensor_status_command_bytes(self.sequence_id, self.product_id, 0x04)
        response_command_content = self.connectObj.send_receive_command(request_command)
        return response_command_content

    def get_drip_speed_sensor_status(self):
        """
        This method is used to get the drip speed sensor status.
        :return: sensor mask and sensor status(NOT INSTALL	0x00/INSTALL	0x08)
        """
        request_command = self.parser_invoker.get_sensor_status_command_bytes(self.sequence_id, self.product_id, 0x08)
        response_command_content = self.connectObj.send_receive_command(request_command)
        return response_command_content

    def get_bubble_sensor_status(self):
        """
        This method is used to get the bubble sensor status.
        :return: sensor mask and sensor status(NOT INSTALL	0x00/INSTALL	0x10)
        """
        request_command = self.parser_invoker.get_sensor_status_command_bytes(self.sequence_id, self.product_id, 0x10)
        response_command_content = self.connectObj.send_receive_command(request_command)
        return response_command_content

    def get_speed_sensor_status(self):
        """
        This method is used to get the speed sensor status.
        :return: sensor mask and sensor status(NOT INSTALL	0x00/INSTALL	0x20)
        """
        request_command = self.parser_invoker.get_sensor_status_command_bytes(self.sequence_id, self.product_id, 0x20)
        response_command_content = self.connectObj.send_receive_command(request_command)
        return response_command_content

