from TestCase.check_pump_status import *


class TestFreeTest(unittest.TestCase):
    """
    FreeTest Part 11 test case
    """

    """
    Part 11
    1.先设置时间参数，再设置输液量参数，速率自动计算；
    2.开始输注；
    3.停止输注。
    正常启动输注。
    """

    def test_FreeTest_part_011(self):
        duration = 3600
        vtbi = 100
        checkPumpStatus()
        lvp.set_infusion_parameter(0, duration, vtbi)
        lvp.start_infusion()
        system_status = lvp.get_system_status()
        assert system_status == SystemStatus.ERunStatus
        time.sleep(7)
        lvp.stop_infusion()
        system_status = lvp.get_system_status()
        assert system_status == SystemStatus.EStopStatus


if __name__ == '__main__':
    unittest.main()
