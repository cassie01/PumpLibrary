from TestCase.check_pump_status import *


class TestFreeTest(unittest.TestCase):
    """
    FreeTest Part 1 test case
    """

    """
    Part 1
    1.输注设置---选择管路品牌A；
    2.基本模式，设置任意有效参数；
    3.启动输注，获取输注中界面的管路品牌B；
    4.停止输注。
    获取管路品牌A与B一致。
    """

    def test_FreeTest_part_001(self):
        A = "Weigao"
        checkPumpStatus()
        lvp.set_brand(A)
        assert lvp.get_brand() == A
        lvp.set_infusion_mode("basic")
        assert lvp.get_infusion_mode() == "basic"
        lvp.set_infusion_parameter(100, 3600, 100)
        lvp.start_infusion()
        time.sleep(1)
        system_status = lvp.get_system_status()
        assert system_status == SystemStatus.ERunStatus
        time.sleep(7)
        B = lvp.get_brand()
        time.sleep(7)
        lvp.stop_infusion()
        system_status = lvp.get_system_status()
        assert system_status == SystemStatus.EStopStatus
        assert A == B


if __name__ == '__main__':
    unittest.main()




