from TestCase.check_pump_status import *

"""
test 0002848:设置无效的参数泵支持运行
软件版本：...\Sprint58\COLLIN\AUTO_TEST\all_tests
测试日期：2019-03-16
"""
checkPumpStatus()
lvp.set_infusion_parameter(1200, 12 * 60, 2)
lvp.start_infusion()
time.sleep(1)
system_status = lvp.get_system_status()
assert system_status == SystemStatus.ERunStatus
time.sleep(2 / 1200 * 3600)
alarm_id = lvp.get_pump_alarm()
assert 23 in alarm_id
alarm_id.clear()
lvp.stop_infusion()
system_status = lvp.get_system_status()
assert system_status == SystemStatus.EStopStatus
