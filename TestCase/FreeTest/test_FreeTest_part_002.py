from TestCase.check_pump_status import *


class TestFreeTest(unittest.TestCase):
    """
    FreeTest Part 2 test case
    """

    """
    Part 2
    1.仅设置速率参数为A，启动输注；
    2.输注中修改速率参数为B，保存继续以B输注；
    3.修改速率参数为C，保存继续以C输注；
    4.停止输注。
    获取输注中界面的速率参数，分别为A-B-C-C。
    """

    def test_FreeTest_part_002(self):
        A = 100
        B = 70
        C = 120
        checkPumpStatus()
        lvp.set_infusion_parameter(A, 0, 0)
        lvp.start_infusion()
        system_status = lvp.get_system_status()
        assert system_status == SystemStatus.ERunStatus
        #  输注中修改参数
        time.sleep(7)
        lvp.stop_infusion()
        system_status = lvp.get_system_status()
        assert system_status == SystemStatus.EStopStatus
