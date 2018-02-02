#-*- coding:utf-8 -*-
from monitoringsystem import MonitoringSystem
from contextlib import suppress
from user import User
import time


def run():
    monitoringSystem = MonitoringSystem()
    while True:
        for user in monitoringSystem.Users:
            monitoringSystem.alarmOnTag(user)
            monitoringSystem.alarmOnTargetAuthors(user)
        print('I am working..')
        time.sleep(monitoringSystem.period_sec)
        if monitoringSystem.isFirstLoopPass == 1:
            monitoringSystem.isFirstLoopPass = 0

if __name__ == '__main__':
    with suppress(KeyboardInterrupt):
        run()
