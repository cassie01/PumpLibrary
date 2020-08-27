import os
import csv
import logging
import datetime
from logging import handlers
from global_attributes import lvp_project_path


class WriteCSV():

    def __init__(self, request_command=None, response_command=None):

        self.path = lvp_project_path + "TestLog/commands_log.csv"

        # Initialize response commands
        if response_command == None:
            pass
        else:
            self.Start_of_message = '0B1C'
            self.Sequence_id = '00'
            self.Response = '01'
            self.Product_id = '02'
            self.raw_string = response_command
            self.string = self.raw_string.split()
            self.response_start_of_message = "".join(self.string[:2])
            self.response_sequence_id = self.string[2]
            self.response_id = self.string[3]
            self.response_product_id = self.string[4]
            self.response_message_id = "".join(self.string[5:7])

            self.response_command = "response_command"
            self.time_str = datetime.datetime.strftime(datetime.datetime.now(), '%Y-%m-%d %H:%M:%S')
            if self.response_start_of_message == self.Start_of_message and self.response_sequence_id == self.Sequence_id:
                if self.response_id == self.Response and self.response_product_id == self.Product_id:
                    self.response_list = [self.time_str, self.response_command, self.raw_string]
                else:
                    print("response or product_id Error!")
                    self.response_list = [self.time_str, self.response_command, "response or product_id Error",
                                          self.raw_string]
                    return
            else:
                print("start_of_message or sequence_id Error!")
                self.response_list = [self.time_str, self.response_command, "start_of_message or sequence_id Error",
                                      self.raw_string]
                return

        # self.sub_string = self.string[4:16]
        #
        # self.first_4_bytes = self.sub_string[0:4]
        # self.second_6_8_bytes = self.sub_string[5:8]
        # self.left_3_bytes = self.sub_string[9:12]
        #
        # self.reverse_4 = "".join(self.first_4_bytes[::-1])
        # self.reverse_6_8 = "".join(self.second_6_8_bytes[::-1])
        # self.reverse_left_3 = "".join(self.left_3_bytes[::-1])
        #
        # self.hex_to_int_4 = int(self.reverse_4, 16)
        # self.hex_to_int_6_8 = int(self.reverse_6_8, 16)
        # self.hex_to_int_3 = int(self.reverse_left_3, 16)
        #
        # # self.data_list = []

        # # self.data_list.append(self.time_str, self.raw_string, self.hex_to_int_4,self.hex_to_int_6_8,self.hex_to_int_3)
        # self.response_list = [self.time_str, self.raw_string, self.hex_to_int_4, self.hex_to_int_6_8, self.hex_to_int_3]

        # Initialize request commands
        if request_command == None:
            pass
        else:
            self.request_string = request_command
            self.request_command = "request_command"
            self.time_str = datetime.datetime.strftime(datetime.datetime.now(), '%Y-%m-%d %H:%M:%S')
            self.request_list = [self.time_str, self.request_command, self.request_string]

    def response_write_csv(self):
        with open(self.path, 'a+', newline='') as f:
            csv_write = csv.writer(f)
            csv_write.writerow(self.response_list)
            print("Response data written successfully！")

    def request_write_csv(self):
        with open(self.path, 'a+', newline='') as f:
            csv_write = csv.writer(f)
            csv_write.writerow(self.request_list)
            print("Request data written successfully！")


class Logger(object):
    level_relations = {
        'debug': logging.DEBUG,
        'info': logging.INFO,
        'warning': logging.WARNING,
        'error': logging.ERROR,
        'crit': logging.CRITICAL
    }  # Log level relationship mapping

    def __init__(self, filename, level='info', when='D', backCount=3,
                 fmt='%(asctime)s - %(pathname)s[line:%(lineno)d] - %(levelname)s: %(message)s'):
        self.logger = logging.getLogger(filename)
        format_str = logging.Formatter(fmt)  # Format log
        self.logger.setLevel(self.level_relations.get(level))  # Set log level
        sh = logging.StreamHandler()  # Output to screen
        sh.setFormatter(format_str)  # Format the display on the screen
        th = handlers.TimedRotatingFileHandler(filename=filename, when=when, backupCount=backCount,
                                               encoding='utf-8')  # Write to file the processor that automatically generates the file at a specified interval
        # instantiate TimedRotatingFileHandler
        # interval is time duration，backupCount is number of backup files，If it exceeds this number, it will be deleted automatically，When is the time unit of the interval, and the units are as follows:
        # S second、
        # M minute、
        # H hour、
        # D day、
        # W every week (interval = = 0 for Monday)
        # midnight
        th.setFormatter(format_str)  # Set the format written in the file
        self.logger.addHandler(sh)  # Add object to logger
        self.logger.addHandler(th)


if __name__ == '__main__':
    pass
    # log = Logger('./TestLog/all.csv', level='debug')
    # log.logger.debug('debug')
    # log.logger.info('info')
    # log.logger.warning('warning')
    # log.logger.error('error')
    # log.logger.critical('critical')
    # Logger('./TestLog/error.csv', level='error').logger.error('error')

    # curr_time = datetime.datetime.now()
    # time_str = datetime.datetime.strftime(curr_time, '%Y-%m-%d %H:%M:%S')
    # data = ['123', '234', '345']
    # data.insert(0,time_str)
    # WriteExcel.write_csv(data)

    # data = "0B 1C 05 00 01 09 90 13 0B 15 10 35 18 2B 00 02 00 00 CB 56 CA E1 "
    # request_data = "0B 1C 00 00 02 0A 20 13 0B 1B 0D 18 08 2B 00 02 15 00 01 00 11 00 10 66 66 E6 41 14 00 00 00 00 00 00 00 00 00 00 00 38 D1 2A CE"
    # response_data = "0B 1C 00 01 02 0A 20 00 00 00 00 00 00 00 00 00 00 00 94 EF"
    # we_request = WriteCSV(request_data, None)
    # we_request.request_write_csv()
    # we_response = WriteCSV(None, response_data)
    # we_response.response_write_csv()
