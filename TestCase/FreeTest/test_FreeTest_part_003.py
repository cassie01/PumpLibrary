from TestCase.check_pump_status import *


class TestFreeTest(unittest.TestCase):
    """
    FreeTest Part 3 test case
    """

    """
    Part 3
    1.累计量清零；
    2.设置任意有效参数，启动输注（设置中速率即可）；
    3.获取当前输注中界面累计量为A；
    4.切换至快速输注界面，然后退出；
    5.再次获取输注中界面累计量为B；
    6.停止输注。
    获取的累计量A与B差值不会太大。
    """

    def test_FreeTest_part_003(self):
        checkPumpStatus()
        #  累计量清零
        time.sleep(7)
        lvp.set_infusion_parameter(70, 3600, 70)
        lvp.start_infusion()
        system_status = lvp.get_system_status()
        assert system_status == SystemStatus.ERunStatus
        #  获取累计量
        time.sleep(7)
        lvp.start_bolus()
        time.sleep(7)
        lvp.stop_bolus()
        system_status = lvp.get_system_status()
        assert system_status == SystemStatus.ERunStatus
        time.sleep(7)
        lvp.stop_infusion()
        system_status = lvp.get_system_status()
        assert system_status == SystemStatus.EStopStatus
        assert False
