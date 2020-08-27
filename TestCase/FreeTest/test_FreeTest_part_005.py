from TestCase.check_pump_status import *


class TestFreeTest(unittest.TestCase):
    """
    FreeTest Part 5 test case
    """

    """
    Part 5
    1.累计量清零，设置速率，输液量，时间参数C（大于5分钟），启动输注；
    2.获取累计量A；
    3.进行快速输注1分钟，然后停止快速输注，返回输注中界面；
    4.获取累计量B和剩余时间D。
    累计量B大于累计量A（差值视速率而定）；剩余时间D小于时间C（差值另计算）。
    """

    def test_FreeTest_part_005(self):
        #  累计量清零
        A = 70
        B = 1800
        C = 35
        checkPumpStatus()
        lvp.set_infusion_parameter(A, B, C)
        lvp.start_infusion()
        system_status = lvp.get_system_status()
        assert system_status == SystemStatus.ERunStatus
        #  获取累计量
        time.sleep(7)
        lvp.start_bolus()
        time.sleep(60)
        lvp.stop_bolus()
        system_status = lvp.get_system_status()
        assert system_status == SystemStatus.ERunStatus
        #  获取剩余时间
        time.sleep(7)
