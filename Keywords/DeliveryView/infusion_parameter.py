# -*-coding:utf-8 -*-

from Keywords.keywordgroup import KeywordGroup
from ParserProtocol.struct_define import StructInfusionParameter, SetInfusionParameter


class InfusionParameter(KeywordGroup):
    """
    This class is used to define all related methods with infusion parameter.
    """

    def set_infusion_parameter(self, rate, infusion_time, vtbi):
        """
        This method is used to set infusion parameter.
        :param rate: valid value
        :param infusion time: valid value
        :param vtbi: valid value
        :return: None
        """
        # if (0.1 <= rate <= 1200.00) and (0 <= infusion_time <= 99 * 3600 + 59 * 60 + 59) and (0 <= vtbi <= 9999.99):
        #     if rate * infusion_time / 3600 == vtbi:
        #         pass
        #     # elif vtbi / rate == infusion_time / 3600:
        #     #     pass
        #     # elif vtbi / infusion_time / 3600 == rate:
        #     #     pass
        #     else:
        #         print("Parameters is invalid!")
        #         return
        # else:
        #     print("The parameter is out of range!")
        #     return
        struct1 = SetInfusionParameter()
        struct1.fill_basic_mode_parameter(rate, infusion_time, vtbi)
        struct2 = StructInfusionParameter()
        struct2.copy(struct1)
        request_command = self.parser_invoker.set_infusion_parameter_command_bytes(self.sequence_id, self.product_id,
                                                                                   struct2)
        response_command_content = self.connectObj.send_receive_command(request_command)
        return response_command_content

    # TODO 泵端不支持此命令
    def get_current_drug(self):
        """
        This method is used to get current drug index.
        :return: drug_index
        """
        request_command = self.parser_invoker.get_current_drug_command_bytes(self.sequence_id, self.product_id)
        response_command_content = self.connectObj.send_receive_command(request_command)
        return response_command_content

    # TODO 泵端不支持此命令
    def set_current_drug(self, drug_index):
        """
        This method is used to set current drug.
        :param drug_index: number
        :return: None
        """
        request_command = self.parser_invoker.set_current_drug_command_bytes(self.sequence_id, self.product_id,
                                                                             drug_index)
        response_command_content = self.connectObj.send_receive_command(request_command)
        return response_command_content
