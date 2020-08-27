from TestCase.check_pump_status import *


class TestFreeTest(unittest.TestCase):
    """
    FreeTest Part 6 test case
    """

    """
    Part 6
    1.获取主界面累计量A（非零）；
    2.切换界面（菜单界面/排气界面），返回；
    3.获取累计量B。
    获取的累计量A与B一致。
    """

    def test_FreeTest_part_006(self):
        #  获取主界面累计量
        checkPumpStatus()
        time.sleep(7)
        lvp.start_bolus()
        lvp.stop_prime()
