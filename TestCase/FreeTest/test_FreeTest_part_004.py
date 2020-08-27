from TestCase.check_pump_status import *


class TestFreeTest(unittest.TestCase):
    """
    FreeTest Part 4 test case
    """

    """
    Part 4
    1.分别设置速率A，输液量B和时间参数C；
    2.切换界面（菜单界面/排气界面/待机模式界面）；
    3.再返回至主界面，检查界面参数。
    获取的速率、输液量、时间参数仍为A,B,C。
    """

    def test_FreeTest_part_004(self):
        A = 100
        B = 3600
        C = 100
        checkPumpStatus()
        lvp.set_infusion_parameter(A, B, C)
        lvp.start_bolus()
        lvp.stop_prime()
        #  获取速率，输液量，时间
