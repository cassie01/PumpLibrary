#coding：utf-8

from TestCase.check_pump_status import *


class TestSmokeTest():
    """
    SmokeTest test case
    """

    def test_smoke_test(self):
        """

        :return:
        """

        """
        1.2.3.1 基本模式	N/A
        1.2.3.1.1 功能配置	N/A
        进入菜单下的输注设置，设置输注模式为基本模式。	设置成功。
        设置延时输注功能为开，并且打开KVO速率运行。	设置成功。
        设置药物库功能为开。	设置成功。
        返回菜单界面进入安全设置，设置运行时编辑参数功能为开。	设置成功。
        设置即将输注完成报警的触发条件为时间，剩时间参数设置为3min。	设置成功。
        设置按键锁功能为开。	设置成功。
        """
        checkPumpStatus()
        lvp.set_infusion_mode("basic")
        assert lvp.get_infusion_mode() == "basic"
        lvp.set_delayed_start_switch_status("On")
        assert lvp.get_delayed_start_switch_status() == "On"
        lvp.set_kvo(5)
        assert lvp.get_kvo() == 5
        lvp.set_drug_library_switch_status("On")
        assert lvp.get_drug_library_switch_status() == "On"
        lvp.set_edit_rate_at_run_time_switch_status("On")
        assert lvp.get_edit_rate_at_run_time_switch_status() == "On"
        lvp.set_infusion_near_complete_criteria("ByTime", 3)
        assert lvp.get_infusion_near_complete_criteria() == ("ByTime", 3)
        lvp.set_keypad_lock_switch_status("On")
        assert lvp.get_keypad_lock_switch_status() == "On"

        """
        1.2.3.1.2 输注运行	N/A
        1.2.3.1.2.1 仅设置速率
        基本模式主界面，正确安装管路，设置如下参数：
        1.仅设置速率，确保速率超范围（Rate<0.10mL/h）
        2.延时输注时间不设置
        3.设置任意药物
        按开始/停止键。	设置成功，无法启动输注。提示：速率超范围。
        基本模式主界面，正确安装管路，设置如下参数：
        1.仅设置速率，确保速率正常（0.10mL/h<Rate<1200.00mL/h）
        2.延时输注时间不设置
        3.设置任意药物
        按开始/停止键。	开始输注。
        输注过程中按OK键修改速率为任意有效值后再按OK键确认。	泵继续以新设置的速率运行。
        按开始/停止键。	停止输注。
        """
        lvp.set_infusion_parameter(0.09, 0, 0)
        lvp.set_delayed_start_switch_status("Off")
        assert lvp.get_delayed_start_switch_status() == "Off"
        lvp.set_drug_library_switch_status("On")
        assert lvp.get_drug_library_switch_status() == "On"
        lvp.start_infusion()
        alarm_id = lvp.get_pump_alarm()
        assert 1 in alarm_id
        alarm_id.clear()
        time.sleep(7)
        lvp.set_infusion_parameter(100, 0, 0)
        lvp.set_delayed_start_switch_status("Off")
        assert lvp.get_delayed_start_switch_status() == "Off"
        lvp.set_drug_library_switch_status("On")
        assert lvp.get_drug_library_switch_status() == "On"
        lvp.start_infusion()
        current_system_status = lvp.get_system_status()
        assert current_system_status == SystemStatus.ERunStatus
        time.sleep(7)

        lvp.stop_infusion()
        current_system_status = lvp.get_system_status()
        assert current_system_status == SystemStatus.EStopStatus

        """
        1.2.3.1.2.2 先设置时间再设置输液量
        基本模式主界面，正确安装管路，设置如下参数：
        1.设置时间参数为有效的任意值
        2.设置输液量参数为有效的任意值.
        3.速率（自动计算）
        4.延时输注时间不设置
        5.设置任意药物
        按开始/停止键。
        输注过程中按OK键修改时间为任意有效值后按OK键确认。
        按开始/停止键。
        1.2.3.1.2.3 先设置速率再设置输液量
        基本模式主界面，正确安装管路，设置如下参数：
        1.设置速率，确保速率正常（0.10mL/h<Rate<1200.00mL/h）
        2.设置输液量参数为有效的任意值.
        3.时间（自动计算）
        4.延时输注时间不设置
        5.设置任意药物
        按开始/停止键。
        输注过程中按OK键修改速率为任意有效值后按OK键确认。
        按开始/停止键。
        """

