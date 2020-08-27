import os
import time
import pytest
import unittest

from global_attributes import lvp_project_path
from html_report_generator import HTMLTestRunner


def discover():
    '''Get the test case script that needs to be executed'''
    suite = unittest.defaultTestLoader.discover(
        start_dir=os.path.join(
            os.path.dirname(__name__),
            'FreeTest'),  # This is the directory of pending use cases
        pattern='test_*',  # This is the rule that matches the script name
        top_level_dir=None  # This is the name of the top-level directory, which is usually equal to None by default.
    )
    return suite


def get_time():
    '''Returns the current time format information'''
    # now = time.strftime('%Y-%m-%d %H_%M_%S')  # Get the current time and format it as a string
    now = time.strftime('%Y_%m_%d_%H_%M_%S')  # Get the current time and format it as a string
    return now


def unittest_main():
    '''Define test reports and execute test case scripts'''
    # The os.path.join () function is used to concatenate file paths, which is commonly used in the mainstream.
    # The method's internal code is perfectly encapsulated, as long as the correct two paths are passed in.
    filename = os.path.join(
        os.path.dirname(__name__),
        'FreeTest',
        lvp_project_path + "TestReport/" + get_time() + '_test_result_report.html')
    fp = open(filename, 'wb')
    runner = HTMLTestRunner(stream=fp,
                            title='Automated test report',
                            description='Test case execution details')
    runner.run(discover())
    fp.close()


def pytest_main(single_case_path='', run_count=1):
    report_name = lvp_project_path + "TestReport/" + get_time() + '_test_result_report.html'
    log_name = lvp_project_path + "TestLog/" + get_time() + '_test_result_log.csv'
    pytest.main(
        [single_case_path, '--count={}'.format(run_count), '--html={}'.format(report_name),
         '--self-contained-html', '--resultlog={}'.format(log_name)])


if __name__ == '__main__':
    pytest_main('./SmokeTest/test_SmokeTest_part_001.py', 3)
    # pytest_main()
    # report_name = lvp_project_path + "TestReport/" + get_time() + '_test_result_report.html'
    # os.system("py.test ./SmokeTest/test_SmokeTest_part_001.py --count=5 --html={}".format(report_name))


"""
report_name = lvp_project_path + "TestReport/" + get_time() + '_test_result_report.html'
pytest.main(["-s", "./SmokeTest/test_case2.py", "--html={}".format(report_name)])


# os.system("py.test -q test_case.py --html={}".format(report_name))


report_name = lvp_project_path + "TestReport/" + get_time() + '_test_result_report.html'
pytest.main(["-s", "test_case.py", "--html={}".format(report_name)])


# 我们指定运行test_测试模块1.py（pytest - v 测试用例目录1 / test_测试模块1.py ）
"""