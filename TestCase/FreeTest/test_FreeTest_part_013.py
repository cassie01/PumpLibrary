from TestCase.check_pump_status import *


class TestFreeTest(unittest.TestCase):
    """
    FreeTest Part 13 test case
    """

    """
    Part 13	
    1.设置KVO值为10；
    2.设置速率，时间参数，启动输注；
    3.等待输注完成进入KVO，获取马达状态；
    4.停止输注。
    马达状态为转动。
    """

    def test_FreeTest_part_013(self):
        kvo = 10
        rate = 70
        duration = 360
        checkPumpStatus()
        lvp.set_kvo(kvo)
        assert lvp.get_kvo() == kvo
        lvp.set_infusion_parameter(rate, duration, 0)
        lvp.start_infusion()
        system_status = lvp.get_system_status()
        assert system_status == SystemStatus.ERunStatus
        time.sleep(360)
        alarm_id = lvp.get_pump_alarm()
        assert 23 in alarm_id
        alarm_id.clear()
        #  获取进入KVO状态后的马达状态
        lvp.stop_infusion()
        system_status = lvp.get_system_status()
        assert system_status == SystemStatus.EStopStatus
