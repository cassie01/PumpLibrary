from TestCase.check_pump_status import *


class TestFreeTest(unittest.TestCase):
    """
    FreeTest Part 9 test case
    """

    """
    Part 9
    1.设置速率1.5mL/h，输液量24mL，时间自动计算；
    2.开始输注；
    3.直到自动输注完成。	
    获取时间参数为16h；
    输注完成报警触发，无异常。
    """

    def test_FreeTest_part_009(self):
        rate = 1.5
        vtbi = 24
        checkPumpStatus()
        lvp.set_infusion_parameter(rate, 0, vtbi)
        #  获取时间参数
        time.sleep(7)
        lvp.start_infusion()
        system_status = lvp.get_system_status()
        assert system_status == SystemStatus.ERunStatus
        time.sleep(24 / 1.5 * 3600)
        alarm_id = lvp.get_pump_alarm()
        assert 23 in alarm_id
        alarm_id.clear()
        lvp.stop_infusion()
        system_status = lvp.get_system_status()
        assert system_status == SystemStatus.EStopStatus
