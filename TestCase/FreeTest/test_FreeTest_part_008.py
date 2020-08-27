from TestCase.check_pump_status import *


class TestFreeTest(unittest.TestCase):
    """
    FreeTest Part 8 test case
    """

    """
    Part 8
    1.获取累计量A；
    2.执行排气操作，使排气量达到最大值6mL后停止；
    3.获取累计量B。
    获取的累计量A与B数值一致。
    """

    def test_FreeTest_part_008(self):
        #  获取累计量
        checkPumpStatus()
        time.sleep(7)
        lvp.start_bolus()
        lvp.start_prime()
        time.sleep(6 / 1200 * 3600)
        lvp.stop_prime()
