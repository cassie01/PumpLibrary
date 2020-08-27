from TestCase.check_pump_status import *


class TestFreeTest(unittest.TestCase):
    """
    FreeTest Part 17 test case
    """

    """
    Part 17
    1.不安装管路；
    2.设置速率参数，启动输注；
    3.停止输注。
    获取AlarmID，无法正常输注运行。
    """

    def test_FreeTest_part_017(self):
        #  不安装管路
        rate = 70
        checkPumpStatus()
        lvp.set_infusion_parameter(rate, 0, 0)
        lvp.start_infusion()
        time.sleep(2)
        alarm_id = lvp.get_pump_alarm()
        assert 26 in alarm_id
        alarm_id.clear()
        lvp.stop_infusion()
        system_status = lvp.get_system_status()
        assert system_status == SystemStatus.EStopStatus


if __name__ == '__main__':
    unittest.main()
