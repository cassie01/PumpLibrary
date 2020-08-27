# -*- coding:utf8 -*-

"""
Part 1	N/A
打开输液泵并插入电源，等待自检完成。	LCD屏幕亮起，泵进入停止状态。
选择输注模式为基本模式。	设置成功。
设置基本模式基本速率单位为‘mL/h’。	设置成功。
手动灌注和加载管路。	执行排气操作，当排气量达到6.00mL时，排气完成。
打开药物库。	设置成功。
选择药物为盐酸氨溴索注射液。	设置成功。
设置速率为80ml / h，输液量为100mL。	设置成功。
按开始键开始输注。	泵处于运行状态。
输注完成。	屏幕出现输注完成警报。
按停止键停止输注。	警报清除成功，泵处于停止状态。
设置速率为80ml / h，输液量为100mL。	设置成功。
按开始键开始输注。	泵处于运行状态。
如果由于管路中的空气导致泵报警，屏幕出现管路阻塞警报，按停止键停止。	警报消除成功，泵处于停止状态。
按快进键后进行排气。	执行排气操作，当排气量达到6.00mL时，排气完成。
按开始键开始输注。	泵处于运行状态。
输注完成。	屏幕出现输注完成警报。
按停止键停止输注。	警报消除，泵处于停止状态。
设置药物为前列地尔。	设置成功。
设置速率为120ml / h，输液量为100mL。	设置成功。
按开始键开始输注。	泵处于运行状态。
输注完成。	屏幕出现输注完成警报。
按停止键停止输注。	警报消除，泵处于停止状态。
调整药物为脂肪乳氨基酸(17)葡萄糖(11%)注射液。	设置成功。
输入速率80 ml / h，输液量为100mL。	设置成功。
按开始键开始输注。	泵处于运行状态。
输注完成。	屏幕出现输注完成警报。
按停止键停止输注。	警报消除，泵处于停止状态。
将药物改为阿莫西林。	设置成功。
设置速率为80 ml / h，输液量为100mL。	设置成功。
按开始键开始输注。	泵处于运行状态。
输注完成。	屏幕出现输注完成警报。
按停止键停止输注。	警报消除，泵处于停止状态。
调整药物为脂肪乳氨基酸(17)葡萄糖(11%)注射液。	设置成功。
输入速率80 ml / h，输液量为100mL。	设置成功。
按开始键开始输注。	泵处于运行状态。
输注完成。	屏幕出现输注完成警报。
按停止键停止输注。	警报消除，泵处于停止状态。
"""

from TestCase.check_pump_status import *


class TestClinicScenario(unittest.TestCase):

    def test_ClinicScenario_part_001(self):

        keep_running = True
        checkPumpStatus()
        # 打开输液泵并插入电源，等待自检完成。
        # LCD屏幕亮起，泵进入停止状态。
        log.logger.info("This test is started!")
        system_status = lvp.get_system_status()
        log.logger.info("The current system status is %s!" % system_status)
        assert system_status == SystemStatus.EStopStatus
        # 设置为基本模式。
        # 设置成功。
        lvp.set_infusion_mode('basic')
        infusion_mode = lvp.get_infusion_mode()
        log.logger.info("The current infusion mode is %s!" % infusion_mode)
        assert infusion_mode == 'basic'
        # 手动灌注和加载管路。
        # 执行排气操作，当排气量达到6.00mL时，排气完成。
        lvp.start_bolus()
        time.sleep(1)
        lvp.start_prime()
        system_status = lvp.get_system_status()
        log.logger.info("The current system status is %s before priming!" % system_status)
        assert system_status == SystemStatus.ERunStatus
        time.sleep(6 / 1200 * 3600)
        lvp.stop_prime()
        system_status = lvp.get_system_status()
        log.logger.info("The current system status is %s after priming!" % system_status)
        assert system_status == SystemStatus.EStopStatus
        # 打开药物库。
        # 设置成功。
        lvp.set_drug_library_switch_status('On')
        drug_library_switch = lvp.get_drug_library_switch_status()
        assert drug_library_switch == 'On'
        # 选择药物为盐酸氨溴索注射液。
        # 设置成功。
        # lvp.set_current_drug() # 泵端未实现
        # lvp.get_current_drug() # 泵端未实现
        # 输入输液速度80mL/h，输液量为100mL。
        # 设置成功。
        lvp.set_infusion_parameter(80, 0, 100)
        # 按开始键开始输注。
        # 泵处于运行状态。
        lvp.start_infusion()
        system_status = lvp.get_system_status()
        log.logger.info("The current system status is %s after starting infusion!" % system_status)
        assert system_status == SystemStatus.ERunStatus
        alarm_handler_time1 = 0
        mark_time = datetime.datetime.now()
        while keep_running:
            duration_time = (datetime.datetime.now() - mark_time).seconds
            if duration_time - alarm_handler_time1 < 100 / 80 * 3600:
                log.logger.info("The remain time is %s!" % (100 / 80 * 3600 - duration_time))
                alarm_mark_time1 = datetime.datetime.now()
                alarm_id = lvp.get_pump_alarm()
                if type(alarm_id) == list():
                    pass
                else:
                    continue
                if 22 in alarm_id:
                    log.logger.info("The occurred alarm is %s!" % alarmMatrix()[22])
                    lvp.stop_infusion()
                    system_status = lvp.get_system_status()
                    log.logger.info("The current system status is %s!" % system_status)
                    assert system_status == SystemStatus.EStopStatus
                    lvp.start_bolus()
                    lvp.start_prime()
                    system_status = lvp.get_system_status()
                    log.logger.info("The current system status is %s before priming!" % system_status)
                    assert system_status == SystemStatus.ERunStatus
                    time.sleep(6 / 1200 * 3600)
                    lvp.stop_prime()
                    system_status = lvp.get_system_status()
                    log.logger.info("The current system status is %s after priming!" % system_status)
                    assert system_status == SystemStatus.EStopStatus
                    alarm_id.clear()
                    lvp.start_infusion()
                    system_status = lvp.get_system_status()
                    log.logger.info("The current system status is %s after starting infusion!" % system_status)
                    assert system_status == SystemStatus.ERunStatus
                    alarm_handler_time1 = (datetime.datetime.now() - alarm_mark_time1).seconds
            else:
                log.logger.info("Completing infusion!")
                break
        # 输注完成。
        # 屏幕出现输注完成警报。
        alarm_id = lvp.get_pump_alarm()
        log.logger.info("The occurred alarm is %s!" % alarmMatrix()[alarm_id[0]])
        assert 23 in alarm_id
        alarm_id.clear()
        # 按停止键消除警报。
        # 警报清除成功，泵处于停止状态。
        lvp.stop_infusion()
        alarm_id = lvp.get_pump_alarm()
        assert 23 not in alarm_id
        system_status = lvp.get_system_status()
        log.logger.info("The current system status is %s after completing infusion!" % system_status)
        assert system_status == SystemStatus.EStopStatus
        # 改变药物为盐酸氨溴索注射液。
        # 设置成功。
        drug_library_switch = lvp.get_drug_library_switch_status()
        assert drug_library_switch == 'On'
        # lvp.set_current_drug() # 泵端未实现
        # lvp.get_current_drug() # 泵端未实现
        # 输入速率80 ml / h，输液量为100mL。
        # 设置成功。
        lvp.set_infusion_parameter(80, 0, 100)
        # 　按开始键开始输注。
        # 泵处于运行状态。
        lvp.start_infusion()
        system_status = lvp.get_system_status()
        log.logger.info("The current system status is %s after starting infusion!" % system_status)
        assert system_status == SystemStatus.ERunStatus
        # 如果由于管路中的空气导致泵报警，屏幕出现管路阻塞警报，按停止键停止。
        # 警报消除成功，泵处于停止状态。
        # 按快进键后进行排气。
        # 执行排气操作，当排气量达到6.00mL时，排气完成。
        alarm_handler_time2 = 0
        mark_time = datetime.datetime.now()
        while keep_running:
            duration_time = (datetime.datetime.now() - mark_time).seconds
            if duration_time - alarm_handler_time2 < 100 / 80 * 3600:
                log.logger.info("The remain time is %s!" % (100 / 80 * 3600 - duration_time))
                alarm_mark_time2 = datetime.datetime.now()
                alarm_id = lvp.get_pump_alarm()
                if type(alarm_id) == list():
                    pass
                else:
                    continue
                if 22 in alarm_id:
                    log.logger.info("The occurred alarm is %s!" % alarmMatrix()[22])
                    lvp.stop_infusion()
                    system_status = lvp.get_system_status()
                    log.logger.info("The current system status is %s!" % system_status)
                    assert system_status == SystemStatus.EStopStatus
                    lvp.start_bolus()
                    lvp.start_prime()
                    system_status = lvp.get_system_status()
                    log.logger.info("The current system status is %s before priming!" % system_status)
                    assert system_status == SystemStatus.ERunStatus
                    time.sleep(6 / 1200 * 3600)
                    lvp.stop_prime()
                    system_status = lvp.get_system_status()
                    log.logger.info("The current system status is %s after priming!" % system_status)
                    assert system_status == SystemStatus.EStopStatus
                    alarm_id.clear()
                    lvp.start_infusion()
                    system_status = lvp.get_system_status()
                    log.logger.info("The current system status is %s after starting infusion!" % system_status)
                    assert system_status == SystemStatus.ERunStatus
                    alarm_handler_time2 = (datetime.datetime.now() - alarm_mark_time2).seconds
            else:
                log.logger.info("Completing infusion!")
                break
        # 输注完成。
        # 屏幕出现输注完成警报。
        alarm_id = lvp.get_pump_alarm()
        log.logger.info("The occurred alarm is %s!" % alarmMatrix()[alarm_id[0]])
        assert 23 in alarm_id
        alarm_id.clear()
        # 按停止键。
        # 警报消除，泵处于停止状态。
        lvp.stop_infusion()
        alarm_id = lvp.get_pump_alarm()
        assert 23 not in alarm_id
        system_status = lvp.get_system_status()
        log.logger.info("The current system status is %s after completing infusion!" % system_status)
        assert system_status == SystemStatus.EStopStatus
        # 改变药物为前列地尔。
        # 设置成功。
        drug_library_switch = lvp.get_drug_library_switch_status()
        assert drug_library_switch == 'On'
        # lvp.set_current_drug() # 泵端未实现
        # lvp.get_current_drug() # 泵端未实现
        # 将速度调整为120ml / h，输液量为100mL。
        # 设置成功。
        lvp.set_infusion_parameter(120, 0, 100)
        # 按开始键开始输注。
        # 泵处于运行状态。
        lvp.start_infusion()
        system_status = lvp.get_system_status()
        log.logger.info("The current system status is %s after starting infusion!" % system_status)
        assert system_status == SystemStatus.ERunStatus
        # time.sleep(100 / 120 * 3600)
        alarm_handler_time3 = 0
        mark_time = datetime.datetime.now()
        while keep_running:
            duration_time = (datetime.datetime.now() - mark_time).seconds
            if duration_time - alarm_handler_time3 < 100 / 120 * 3600:
                log.logger.info("The remain time is %s!" % (100 / 120 * 3600 - duration_time))
                alarm_mark_time3 = datetime.datetime.now()
                alarm_id = lvp.get_pump_alarm()
                if type(alarm_id) == list():
                    pass
                else:
                    continue
                if 22 in alarm_id:
                    log.logger.info("The occurred alarm is %s!" % alarmMatrix()[22])
                    lvp.stop_infusion()
                    system_status = lvp.get_system_status()
                    log.logger.info("The current system status is %s!" % system_status)
                    assert system_status == SystemStatus.EStopStatus
                    lvp.start_bolus()
                    lvp.start_prime()
                    system_status = lvp.get_system_status()
                    log.logger.info("The current system status is %s before priming!" % system_status)
                    assert system_status == SystemStatus.ERunStatus
                    time.sleep(6 / 1200 * 3600)
                    lvp.stop_prime()
                    system_status = lvp.get_system_status()
                    log.logger.info("The current system status is %s after priming!" % system_status)
                    assert system_status == SystemStatus.EStopStatus
                    alarm_id.clear()
                    lvp.start_infusion()
                    system_status = lvp.get_system_status()
                    log.logger.info("The current system status is %s after starting infusion!" % system_status)
                    assert system_status == SystemStatus.ERunStatus
                    alarm_handler_time3 = (datetime.datetime.now() - alarm_mark_time3).seconds
            else:
                log.logger.info("Completing infusion!")
                break
        # 输注完成。
        # 屏幕出现输注完成警报。
        alarm_id = lvp.get_pump_alarm()
        log.logger.info("The occurred alarm is %s!" % alarmMatrix()[alarm_id[0]])
        assert 23 in alarm_id
        alarm_id.clear()
        # 按停止键。
        # 警报消除，泵处于停止状态。
        lvp.stop_infusion()
        alarm_id = lvp.get_pump_alarm()
        assert 23 not in alarm_id
        system_status = lvp.get_system_status()
        log.logger.info("The current system status is %s after completing infusion!" % system_status)
        assert system_status == SystemStatus.EStopStatus
        # 调整药物为Kabiven TM PI。
        # 设置成功。
        drug_library_switch = lvp.get_drug_library_switch_status()
        assert drug_library_switch == 'On'
        # lvp.set_current_drug() # 泵端未实现
        # lvp.get_current_drug() # 泵端未实现
        # 运行速度为80ml / h，输液量为100mL。
        # 设置成功。
        lvp.set_infusion_parameter(80, 0, 100)
        # 将药物改为阿莫西林。
        # 设置成功。
        drug_library_switch = lvp.get_drug_library_switch_status()
        assert drug_library_switch == 'On'
        # lvp.set_current_drug() # 泵端未实现
        # lvp.get_current_drug() # 泵端未实现
        # 运行速度为80ml / h，输液量为100mL。
        # 设置成功。
        lvp.set_infusion_parameter(80, 0, 100)
        # 按开始键开始输注。
        # 泵处于运行状态。
        lvp.start_infusion()
        system_status = lvp.get_system_status()
        log.logger.info("The current system status is %s after starting infusion!" % system_status)
        assert system_status == SystemStatus.ERunStatus
        alarm_handler_time4 = 0
        mark_time = datetime.datetime.now()
        while keep_running:
            duration_time = (datetime.datetime.now() - mark_time).seconds
            if duration_time - alarm_handler_time4 < 100 / 80 * 3600:
                log.logger.info("The remain time is %s!" % (100 / 80 * 3600 - duration_time))
                alarm_mark_time4 = datetime.datetime.now()
                alarm_id = lvp.get_pump_alarm()
                if type(alarm_id) == list():
                    pass
                else:
                    continue
                if 22 in alarm_id:
                    log.logger.info("The occurred alarm is %s!" % alarmMatrix()[22])
                    lvp.stop_infusion()
                    system_status = lvp.get_system_status()
                    log.logger.info("The current system status is %s!" % system_status)
                    assert system_status == SystemStatus.EStopStatus
                    lvp.start_bolus()
                    lvp.start_prime()
                    system_status = lvp.get_system_status()
                    log.logger.info("The current system status is %s before priming!" % system_status)
                    assert system_status == SystemStatus.ERunStatus
                    time.sleep(6 / 1200 * 3600)
                    lvp.stop_prime()
                    system_status = lvp.get_system_status()
                    log.logger.info("The current system status is %s after priming!" % system_status)
                    assert system_status == SystemStatus.EStopStatus
                    alarm_id.clear()
                    lvp.start_infusion()
                    system_status = lvp.get_system_status()
                    log.logger.info("The current system status is %s after starting infusion!" % system_status)
                    assert system_status == SystemStatus.ERunStatus
                    alarm_handler_time4 = (datetime.datetime.now() - alarm_mark_time4).seconds
            else:
                log.logger.info("Completing infusion!")
                break
        # 输注完成。
        # 屏幕出现输注完成警报。
        alarm_id = lvp.get_pump_alarm()
        log.logger.info("The occurred alarm is %s!" % alarmMatrix()[alarm_id[0]])
        assert 23 in alarm_id
        alarm_id.clear()
        # 按停止键。
        # 警报消除，泵处于停止状态。
        lvp.stop_infusion()
        alarm_id = lvp.get_pump_alarm()
        assert 23 not in alarm_id
        system_status = lvp.get_system_status()
        log.logger.info("The current system status is %s after completing infusion!" % system_status)
        assert system_status == SystemStatus.EStopStatus
        # 调整药物为Kabiven TM PI。
        # 设置成功。
        drug_library_switch = lvp.get_drug_library_switch_status()
        assert drug_library_switch == 'On'
        # lvp.set_current_drug() # 泵端未实现
        # lvp.get_current_drug() # 泵端未实现
        # 运行速度为80ml / h，输液量为100mL。
        # 设置成功。
        lvp.set_infusion_parameter(80, 0, 100)
        # 按开始键开始输注。
        # 泵处于运行状态。
        lvp.start_infusion()
        system_status = lvp.get_system_status()
        log.logger.info("The current system status is %s after starting infusion!" % system_status)
        assert system_status == SystemStatus.ERunStatus
        alarm_handler_time5 = 0
        mark_time = datetime.datetime.now()
        while keep_running:
            duration_time = (datetime.datetime.now() - mark_time).seconds
            if duration_time - alarm_handler_time5 < 100 / 80 * 3600:
                log.logger.info("The remain time is %s!" % (100 / 80 * 3600 - duration_time))
                alarm_mark_time5 = datetime.datetime.now()
                alarm_id = lvp.get_pump_alarm()
                if type(alarm_id) == list():
                    pass
                else:
                    continue
                if 22 in alarm_id:
                    log.logger.info("The occurred alarm is %s!" % alarmMatrix()[22])
                    lvp.stop_infusion()
                    system_status = lvp.get_system_status()
                    log.logger.info("The current system status is %s!" % system_status)
                    assert system_status == SystemStatus.EStopStatus
                    lvp.start_bolus()
                    lvp.start_prime()
                    system_status = lvp.get_system_status()
                    log.logger.info("The current system status is %s before priming!" % system_status)
                    assert system_status == SystemStatus.ERunStatus
                    time.sleep(6 / 1200 * 3600)
                    lvp.stop_prime()
                    system_status = lvp.get_system_status()
                    log.logger.info("The current system status is %s after priming!" % system_status)
                    assert system_status == SystemStatus.EStopStatus
                    alarm_id.clear()
                    lvp.start_infusion()
                    system_status = lvp.get_system_status()
                    log.logger.info("The current system status is %s after starting infusion!" % system_status)
                    assert system_status == SystemStatus.ERunStatus
                    alarm_handler_time5 = (datetime.datetime.now() - alarm_mark_time5).seconds
            else:
                log.logger.info("Completing infusion!")
                break
        # 输注完成。
        # 屏幕出现输注完成警报。
        alarm_id = lvp.get_pump_alarm()
        log.logger.info("The occurred alarm is %s!" % alarmMatrix()[alarm_id[0]])
        assert 23 in alarm_id
        alarm_id.clear()
        # 按停止键。
        # 警报消除，泵处于停止状态。
        lvp.stop_infusion()
        alarm_id = lvp.get_pump_alarm()
        assert 23 not in alarm_id
        system_status = lvp.get_system_status()
        log.logger.info("The current system status is %s after completing infusion!" % system_status)
        assert system_status == SystemStatus.EStopStatus


if __name__ == '__main__':
    # from TestCase.run_test import *
    # pytest_main()
    unittest.main()
