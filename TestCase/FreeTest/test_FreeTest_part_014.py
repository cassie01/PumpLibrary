from TestCase.check_pump_status import *


class TestFreeTest(unittest.TestCase):
    """
    FreeTest Part 14 test case
    """

    """
    Part 14
    1.设置即将输注完成报警为输液量5mL,排气，使排气量达到最大6mL；
    2.全参数设置，启动输注；
    3.执行Bolus操作;
    4.等待触发即将输注完成和输注完成报警，停止输注。
    输注正常。
    """

    def test_FreeTest_part_014(self):
        rate = 100
        duration = 360
        vtbi = 10
        checkPumpStatus()
        lvp.set_infusion_near_complete_criteria("ByVolume", 5)
        assert lvp.get_infusion_near_complete_criteria() == ("ByVolume", 5)
        lvp.start_bolus()
        lvp.start_prime()
        time.sleep(6 / 1200 * 3600)
        lvp.stop_prime()
        lvp.set_infusion_parameter(rate, duration, vtbi)
        lvp.start_infusion()
        system_status = lvp.get_system_status()
        assert system_status == SystemStatus.ERunStatus
        time.sleep(7)
        lvp.start_bolus()
        time.sleep(7)
        lvp.stop_bolus()
        time.sleep(duration)
        alarm_id = lvp.get_pump_alarm()
        assert 23 in alarm_id
        alarm_id.clear()
        lvp.stop_infusion()
        system_status = lvp.get_system_status()
        assert system_status == SystemStatus.EStopStatus


if __name__ == '__main__':
    unittest.main()
