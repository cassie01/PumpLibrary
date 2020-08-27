from TestCase.check_pump_status import *


class TestFreeTest(unittest.TestCase):
    """
    FreeTest Part 15 test case
    """

    """
    Part 15
    1.安全设置--即将输注完成--输液量--15；
    2.设置速率1200，输液量1，等待输注完成进入KVO，然后停止输注；
    3.重新开始输注，仅速率1200运行，停止输注。
    重新开始输注时，无异常即将输注完成报警发生，获取Alarm为空。
    """

    def test_FreeTest_part_015(self):
        rate = 1200
        vtbi = 1
        checkPumpStatus()
        lvp.set_infusion_near_complete_criteria("ByVolume", 15)
        assert lvp.get_infusion_near_complete_criteria() == ("ByVolume", 15)
        lvp.set_infusion_parameter(rate, 0, vtbi)
        lvp.start_infusion()
        time.sleep(1)
        system_status = lvp.get_system_status()
        assert system_status == SystemStatus.ERunStatus
        time.sleep(1 / 1200 * 3600)
        alarm_id = lvp.get_pump_alarm()
        assert 23 in alarm_id
        alarm_id.clear()
        lvp.stop_infusion()
        system_status = lvp.get_system_status()
        assert system_status == SystemStatus.EStopStatus
        alarm_id = lvp.get_pump_alarm()
        assert alarm_id == []
        lvp.stop_infusion()
        system_status = lvp.get_system_status()
        assert system_status == SystemStatus.EStopStatus
        lvp.set_infusion_parameter(rate, 0, 0)
        lvp.start_infusion()
        time.sleep(1)
        system_status = lvp.get_system_status()
        assert system_status == SystemStatus.ERunStatus
        time.sleep(7)
        lvp.stop_infusion()
        system_status = lvp.get_system_status()
        assert system_status == SystemStatus.EStopStatus


if __name__ == '__main__':
    unittest.main()
