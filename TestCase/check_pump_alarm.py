# -*- coding: utf-8 -*-

from TestCase import *


def checkPumpAlarm():
    keep_running = True
    matrix = alarm_matrix()
    while keep_running:
        alarm_id = lvp.get_pump_alarm()
        for id in alarm_id[0:len(alarm_id)]:
            if id > 46 and id < 0:
                return

        if 0 in alarm_id:  # None
            time.sleep(3)
            alarm_id.clear()

        elif 1 in alarm_id:  # "Rate Out Of Range"
            time.sleep(3)
            alarm_id.clear()

        elif 2 in alarm_id:  # "Parameter Not Set"
            time.sleep(3)
            alarm_id.clear()

        elif 3 in alarm_id:  # "Invalid Time"
            time.sleep(3)
            alarm_id.clear()

        elif 4 in alarm_id:  # "VTBI Out of Range"
            time.sleep(3)
            alarm_id.clear()

        elif 5 in alarm_id:  # "Time out of range"
            time.sleep(3)
            alarm_id.clear()

        elif 6 in alarm_id:  # "Rate Out Of Range"
            time.sleep(3)
            alarm_id.clear()

        elif 7 in alarm_id:  # "Priming Reach Max"
            time.sleep(3)
            alarm_id.clear()

        elif 8 in alarm_id:  # "Battery Temp. Abnormal"
            time.sleep(3)
            alarm_id.clear()

        elif 9 in alarm_id:  # "Tube Not Calibrated"
            time.sleep(3)
            alarm_id.clear()

        elif 10 in alarm_id:  # "Pressure Sensor Not Calibrated"
            time.sleep(3)
            alarm_id.clear()

        elif 11 in alarm_id:  # "Dose Out Of Range"
            time.sleep(3)
            alarm_id.clear()

        elif 12 in alarm_id:  # "Concentration Out Of Range"
            time.sleep(3)
            alarm_id.clear()

        elif 13 in alarm_id:  # "Secondary Infusion Completed"
            time.sleep(3)
            alarm_id.clear()

        elif 14 in alarm_id:  # "Low Battery"
            time.sleep(3)
            alarm_id.clear()

        elif 15 in alarm_id:  # "Drip Sensor Fall"
            time.sleep(3)
            alarm_id.clear()

        elif 16 in alarm_id:  # "System Idle"
            time.sleep(3)
            alarm_id.clear()

        elif 17 in alarm_id:  # "Infusion Near Complete"
            time.sleep(3)
            alarm_id.clear()

        elif 18 in alarm_id:  # "Standby time End"
            time.sleep(3)
            alarm_id.clear()

        elif 19 in alarm_id:  # "Battery Depleted"
            time.sleep(3)
            alarm_id.clear()

        elif 20 in alarm_id:  # "Occlusion"
            time.sleep(3)
            alarm_id.clear()

        elif 21 in alarm_id:  # "Over Air"
            time.sleep(3)
            alarm_id.clear()

        elif 22 in alarm_id:  # "Infusion Completed"
            time.sleep(3)
            alarm_id.clear()

        elif 23 in alarm_id:  # "Secondary Infusion Completed"
            time.sleep(3)
            alarm_id.clear()

        elif 24 in alarm_id:  # "Door Opened"
            time.sleep(3)
            alarm_id.clear()

        elif 25 in alarm_id:  # "Tube Not install"
            time.sleep(3)
            alarm_id.clear()

        else:
            if len(alarm_id) > 0:
                pass


if __name__ == '__main__':
    checkPumpAlarm()
