from TestCase.check_pump_status import *


class TestFreeTest(unittest.TestCase):
    """
    FreeTest Part 10 test case
    """

    """
    Part 10
    1.仅设置速率参数；
    2.输注一段时间后触发高优先级报警；
    3.停止后返回主界面；
    4.再次重新开始输注；
    5.停止输注。
    可以重新开始输注，无异常。
    """

    def test_FreeTest_part_010(self):
        rate = 70
        checkPumpStatus()
        lvp.set_infusion_parameter(rate, 0, 0)
        lvp.start_infusion()
        system_status = lvp.get_system_status()
        assert system_status == SystemStatus.ERunStatus
        #  触发高优先级报警
        time.sleep(7)
        lvp.stop_infusion()
        system_status = lvp.get_system_status()
        assert system_status == SystemStatus.EStopStatus
        lvp.start_infusion()
        system_status = lvp.get_system_status()
        assert system_status == SystemStatus.ERunStatus
        time.sleep(7)
        lvp.stop_infusion()
        system_status = lvp.get_system_status()
        assert system_status == SystemStatus.EStopStatus
