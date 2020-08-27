from TestCase.check_pump_status import *


class TestFreeTest(unittest.TestCase):
    """
    FreeTest Part 16 test case
    """

    """
    Part 16
    1.进行排气操作；
    2.仅设置速率参数，启动输注；
    3.触发门打开报警。
    4.停止输注。
    获取报警ID，为门打开；
    获取马达状态为停止。
    """

    def test_FreeTest_part_016(self):
        rate = 70
        checkPumpStatus()
        lvp.start_bolus()
        lvp.start_prime()
        time.sleep(6 / 1200 * 3600)
        lvp.stop_prime()
        lvp.set_infusion_parameter(rate, 0, 0)
        lvp.start_infusion()
        system_status = lvp.get_system_status()
        assert system_status == SystemStatus.ERunStatus
        #  触发门打开报警
        time.sleep(7)
        alarm_id = lvp.get_pump_alarm()
        assert 25 in alarm_id
        alarm_id.clear()
        lvp.stop_infusion()
        system_status = lvp.get_system_status()
        assert system_status == SystemStatus.EStopStatus

