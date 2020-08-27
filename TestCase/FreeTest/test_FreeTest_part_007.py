from TestCase.check_pump_status import *


class TestFreeTest(unittest.TestCase):
    """
    FreeTest Part 7 test case
    """

    """
    Part 7
    1.设置屏幕亮度为A；
    2.设置夜间模式时间段，确保当前泵端时间在夜间模式时间段内；
    3.设置夜间模式屏幕亮度B，确保B远远小于A，开启夜间模式。
    夜间模式状态下，获取当前屏幕亮度为B。
    """

    def test_FreeTest_part_007(self):
        A = 7
        checkPumpStatus()
        lvp.set_brightness(A)
        assert lvp.get_brightness() == A
        current_time_hour = lvp.get_date_time()[3]
        lvp.set_night_mode_period(current_time_hour, 0, current_time_hour + 6, 0)
        B = 2
        lvp.set_night_mode_brightness(B)
        lvp.set_night_mode_switch_status("On")
        assert lvp.get_brightness() == A
        assert lvp.get_night_mode_brightness() == B


if __name__ == '__main__':
    unittest.main()
