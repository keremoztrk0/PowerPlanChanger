from PowerManager import PowerManager, PowerPlan
from PyQt5.QtGui import *
from PyQt5.QtWidgets import *
from PyQt5 import QtCore, QtGui

from functools import partial

powerManager = PowerManager()
powerPlans = powerManager.getPowerPlans()

app = QApplication([])
app.setQuitOnLastWindowClosed(False)

icon = QIcon("icon.ico")

tray = QSystemTrayIcon()
tray.setIcon(icon)
tray.setVisible(True)

menu = QMenu()


powerPlansMenu = QMenu("Power Plans")

actionGroup = QActionGroup(powerPlansMenu)

menu.addMenu(powerPlansMenu)

for plan in powerPlans:
    action = QAction(plan.Name)
    action.setCheckable(True)
    if plan.Active == True :
        action.setChecked(True)
    action.triggered.connect(partial(powerManager.setPowerPlan, plan.Guid))

    actionGroup.addAction(action)


    powerPlansMenu.addAction(action)

menu.addMenu(powerPlansMenu)

quit = QAction("Quit")
quit.triggered.connect(app.quit)
menu.addAction(quit)

tray.setContextMenu(menu)
app.exec_()
