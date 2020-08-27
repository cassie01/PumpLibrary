# -*-coding:utf-8 -*-

from Keywords.keywordgroup import KeywordGroup


class InfusionSetting(KeywordGroup):
    """
    This class is used to define all related methods with infusion setting.
    """

    def get_infusion_mode(self):
        """
        This method is used to get infusion mode.
        :return: infusion mode
        """
        request_command = self.parser_invoker.get_infusion_mode_command_bytes(self.sequence_id, self.product_id)
        response_command_content = self.connectObj.send_receive_command(request_command)
        return response_command_content

    def set_infusion_mode(self, mode):
        """
        This method is used to set pump infusion mode.
        :param mode:
                    basic    0x10
                    weight    0x11
                    multirate    0x12
                    taper    0x13
                    step    0x14
        :return: None
        """

        # mode = hex(mode)

        if mode == "basic":
            mode = 0x10
        elif mode == "weight":
            mode = 0x11
        elif mode == "multirate":
            mode = 0x12
        elif mode == "taper":
            mode = 0x13
        elif mode == "step":
            mode = 0x14
        else:
            print("Invalid parameter!")
            return
        request_command = self.parser_invoker.set_infusion_mode_command_bytes(self.sequence_id, self.product_id, mode)
        response_command_content = self.connectObj.send_receive_command(request_command)
        return response_command_content

    def get_dose_unit(self):
        """
        This method is used to get dose unit.
        :return: dose unit
        """
        request_command = self.parser_invoker.get_dose_uint_command_bytes(self.sequence_id, self.product_id)
        response_command_content = self.connectObj.send_receive_command(request_command)
        return response_command_content

    def set_dose_unit(self, dose_unit):
        """
        This method is used to set dose unit.
        :param dose_unit:
                         mcg/kg/h    0x00
                         mg/kg/h    0x01
                         mcg/kg/min    0x02
                         mg/kg/min    0x03
        :return: None
        """
        if dose_unit == "mcg/kg/h":
            dose_unit = 0x00
        elif dose_unit == "mg/kg/h":
            dose_unit = 0x01
        elif dose_unit == "mcg/kg/min":
            dose_unit = 0x02
        elif dose_unit == "mg/kg/min":
            dose_unit = 0x03
        else:
            print("Invalid parameter!")
            return
        request_command = self.parser_invoker.set_dose_unit_command_bytes(self.sequence_id, self.product_id, dose_unit)
        response_command_content = self.connectObj.send_receive_command(request_command)
        return response_command_content

    def get_drug_mass_unit(self):
        """
        This method is used to get drug mass unit.
        :return: drug mass unit
        """
        request_command = self.parser_invoker.get_drug_mass_uint_command_bytes(self.sequence_id, self.product_id)
        response_command_content = self.connectObj.send_receive_command(request_command)
        return response_command_content

    def set_drug_mass_unit(self, drug_mass_unit):
        """
        This method is used to set drug mass unit.
        :param drug_mass_unit:
                              g    0x00
                              mg    0x01
                              ug    0x02
        :return: None
        """
        if drug_mass_unit == "g":
            drug_mass_unit = 0x00
        elif drug_mass_unit == "mg":
            drug_mass_unit = 0x01
        elif drug_mass_unit == "ug":
            drug_mass_unit = 0x02
        else:
            print("Invalid parameter!")
            return
        request_command = self.parser_invoker.set_drug_mass_unit_command_bytes(self.sequence_id, self.product_id,
                                                                               drug_mass_unit)
        response_command_content = self.connectObj.send_receive_command(request_command)
        return response_command_content

    def get_brand(self):
        """
        This method is used to get brand.
        :return: brand
        """
        request_command = self.parser_invoker.get_brand_command_bytes(self.sequence_id, self.product_id)
        response_command_content = self.connectObj.send_receive_command(request_command)
        return response_command_content

    def set_brand(self, brand):
        """
        This method is used to set brand.
        :param brand:
                    Brand1	0x00
                    Brand2	0x01
                    Brand3	0x02
                    Brand4	0x03
                    Brand5	0x04
                    Brand6	0x05
                    Brand7	0x06
                    Brand8	0x07
                    Brand9	0x08
                    Brand10	0x09
                    Brand11	0x0A
                    Brand12	0x0B
                    Brand13	0x0C
                    CustomBrand1	0x80
                    CustomBrand2	0x81
                    CustomBrand3	0x82
                    CustomBrand4	0x83
                    CustomBrand5	0x84
        :return: None
        """
        if brand == "Weigao":
            brand = 0x00
        elif brand == "Yusheng":
            brand = 0x01
        elif brand == "Xinhua":
            brand = 0x02
        elif brand == "B.Brand":
            brand = 0x03
        elif brand == "":
            brand = 0x04
        elif brand == "":
            brand = 0x05
        elif brand == "":
            brand = 0x06
        elif brand == "":
            brand = 0x07
        elif brand == "":
            brand = 0x08
        elif brand == "":
            brand = 0x09
        elif brand == "":
            brand = 0x0A
        elif brand == "":
            brand = 0x0B
        elif brand == "":
            brand = 0x0C
        elif brand == "Define 1":
            brand = 0x80
        elif brand == "Define 2":
            brand = 0x81
        elif brand == "Define 3":
            brand = 0x82
        elif brand == "Define 4":
            brand = 0x83
        elif brand == "Define 5":
            brand = 0x84
        elif brand == "Define 6":
            brand = 0x85
        else:
            print("Invalid Parameter!")
            return
        request_command = self.parser_invoker.set_brand_command_bytes(self.sequence_id, self.product_id, brand)
        response_command_content = self.connectObj.send_receive_command(request_command)
        return response_command_content

    def get_delayed_start_switch_status(self):
        """
        This method is used to get delayed start switch status.
        :return: switch status
        """
        request_command = self.parser_invoker.get_switch_status_command_bytes(self.sequence_id, self.product_id,
                                                                              0x200)
        response_command_content = self.connectObj.send_receive_command(request_command)
        return response_command_content

    def set_delayed_start_switch_status(self, switch_status):
        """
        This method is used to set delayed start switch status.
        :param switch_status:
                             Off    0x00
                             On    0x200
        :return: None
        """
        if switch_status == "Off":
            switch_status = 0x00
        elif switch_status == "On":
            switch_status = 0x200
        else:
            print("Invalid parameter!")
            return
        request_command = self.parser_invoker.set_switch_status_command_bytes(self.sequence_id, self.product_id,
                                                                              0x200,
                                                                              switch_status)
        response_command_content = self.connectObj.send_receive_command(request_command)
        return response_command_content

    def get_kvo(self):
        """
        This method is used to get kvo.
        :return: kvo
        """
        request_command = self.parser_invoker.get_kvo_command_bytes(self.sequence_id, self.product_id)
        response_command_content = self.connectObj.send_receive_command(request_command)
        return response_command_content

    def set_kvo(self, kvo):
        """
        This method is used to set kvo.
        :param kvo: (1~10)
        :return: None
        """
        request_command = self.parser_invoker.set_kvo_command_bytes(self.sequence_id, self.product_id, kvo)
        response_command_content = self.connectObj.send_receive_command(request_command)
        return response_command_content

    def get_drug_library_switch_status(self):
        """
        This method is used to get drug library switch status.
        :return: switch status
        """
        request_command = self.parser_invoker.get_switch_status_command_bytes(self.sequence_id, self.product_id,
                                                                              0x20)
        response_command_content = self.connectObj.send_receive_command(request_command)
        return response_command_content

    def set_drug_library_switch_status(self, switch_status):
        """
        This method is used to set drug library switch status.
        :param switch_status:
                             Off    0x00
                             On    0x20
        :return: None
        """
        if switch_status == "Off":
            switch_status = 0x00
        elif switch_status == "On":
            switch_status = 0x20
        else:
            print("Invalid parameter!")
            return

        request_command = self.parser_invoker.set_switch_status_command_bytes(self.sequence_id, self.product_id,
                                                                              0x20,
                                                                              switch_status)
        response_command_content = self.connectObj.send_receive_command(request_command)
        return response_command_content

    def get_occlusion_level(self):
        """
        This method is used to get occlusion level.
        :return: occlusion level
        """
        request_command = self.parser_invoker.get_occlusion_level_command_bytes(self.sequence_id, self.product_id)
        response_command_content = self.connectObj.send_receive_command(request_command)
        return response_command_content

    def set_occlusion_level(self, level):
        """
        This method is used to set occlusion level.
        :param level:
                    Level1	0x00
                    Level2	0x01
                    Level3	0x02
                    Level4	0x03
                    Level5	0x04
        :return: None
        """
        request_command = self.parser_invoker.set_occlusion_level_command_bytes(self.sequence_id, self.product_id,
                                                                                level)
        response_command_content = self.connectObj.send_receive_command(request_command)
        return response_command_content

    def get_save_last_program_switch_status(self):
        """
        This method is used to get save last program switch status.
        :return: switch status
        """
        request_command = self.parser_invoker.get_switch_status_command_bytes(self.sequence_id, self.product_id,
                                                                              0x04)
        response_command_content = self.connectObj.send_receive_command(request_command)
        return response_command_content

    def set_save_last_program_switch_status(self, switch_status):
        """
        This method is used to set save last program switch status.
        :param switch_status:
                             Off    0x00
                             On    0x04
        :return: None
        """
        request_command = self.parser_invoker.set_switch_status_command_bytes(self.sequence_id, self.product_id,
                                                                              0x04,
                                                                              switch_status)
        response_command_content = self.connectObj.send_receive_command(request_command)
        return response_command_content

    # def set_basic_mode_rate_unit(self, basic_mode_rate_unit):
    #     """
    #     This method is used to set rate unit on basic mode.
    #     :param basic_mode_rate_unit:
    #                                 mL/h    0x00
    #                                 drops/min    0x01
    #     :return: None
    #     """
    #     if basic_mode_rate_unit == "mL/h":
    #         basic_mode_rate_unit = 0x00
    #     elif basic_mode_rate_unit == "drops/min":
    #         basic_mode_rate_unit = 0x01
    #     else:
    #         print("Invalid parameter!")
    #         return
    #     request_command = self.parser_invoker.set_basic_mode_rate_unit_command_bytes(self.sequence_id, self.product_id,
    #                                                                                  basic_mode_rate_unit)
    #     response_command_content = self.connectObj.send_receive_command(request_command)
    #     return response_command_content

    # def set_occlusion_level(self, level):
    #     """
    #     This method is used to set occlusion level.
    #     :param level:
    #                  Level1    0x00
    #                  Level2    0x01
    #                  Level3    0x02
    #                  Level4    0x03
    #                  Level5    0x04
    #     :return: None
    #     """
    #     if level == "Level1":
    #         level = 0x00
    #     elif level == "Level2":
    #         level = 0x01
    #     elif level == "Level3":
    #         level = 0x02
    #     elif level == "Level4":
    #         level = 0x03
    #     elif level == "Level5":
    #         level = 0x04
    #     else:
    #         print("Invalid parameter!")
    #         return
    #     request_command = self.parser_invoker.set_occlusion_level_command_bytes(self.sequence_id, self.product_id,
    #                                                                             level)
    #     response_command_content = self.connectObj.send_receive_command(request_command)
    #     return response_command_content
