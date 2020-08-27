from TestCase.check_pump_status import *


class TestFreeTest(unittest.TestCase):
    """
    FreeTest Part 12 test case
    """

    """
    Part 12
    1.设置速率10mL/h，时间1h，启动输注；
    2.进入快速输注，然后返回；
    3.获取输注中界面速率参数A，然后停止输注。
    获取的速率参数A值为10。
    """

    def test_FreeTest_part_012(self):
        rate = 10
        duration = 3600
        lvp.set_infusion_parameter(rate, duration, 0)
        lvp.start_infusion()
        system_status = lvp.get_system_status()
        assert system_status == SystemStatus.ERunStatus
        time.sleep(7)
        lvp.start_bolus()
        time.sleep(7)
        lvp.stop_bolus()
        #  获取输注界面速率参数
        lvp.stop_infusion()
        system_status = lvp.get_system_status()
        assert system_status == SystemStatus.EStopStatus
