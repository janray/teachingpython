import sys

import pyqtgraph as pg
import serial
import numpy as np

import serial.tools.list_ports


from pyqtgraph.Qt import QtCore, QtGui, QtWidgets

import interface as ui_interface


app = pg.mkQApp("TCLAB Inter")

win = QtWidgets.QMainWindow()
win.setWindowTitle("TCLAB Interface by Jan Ray")

pg.setConfigOptions(antialias=True)

ui = ui_interface.Ui_MainWindow()
ui.setupUi(win)


win.show()


availablePorts = []

for port in serial.tools.list_ports.comports():
    availablePorts.append(port[0])


ui.portsComboBox.addItems(availablePorts)

plot1 = ui.plotWindow.addPlot(title="Sine")
plot1.showGrid(x=True, y=True)

signal_1 = plot1.plot(pen="y")

ui.plotWindow.nextRow()

plot2 = ui.plotWindow.addPlot(title="Cosine")
plot2.showGrid(x=True, y=True)


signal_2 = plot2.plot()
signal_2.setPen(color="green", width=3)
i = 0

setPointValue = ui.setPointField.text

amplitude = 0


@QtCore.Slot()
def setAmplitude():
    global amplitude
    amp = 0.0
    try:
        amp = float(ui.setPointField.text())
    except ValueError:
        print("Cannot convert string to float.")

    amplitude = amp


ui.setPointBtn.clicked.connect(setAmplitude)


def update(antialias=pg.getConfigOption("antialias")):
    global i, plot1, plot2, signal_1, signal_2, amplitude
    freq = np.linspace(0, 30, 1000)
    sin1 = np.sin(2 * np.pi * freq + i)
    sig = []
    signal_1.setData(freq, sig)

    cos1 = np.cos(2 * np.pi * freq + i)
    signal_2.setData(freq, cos1)

    i += 0.1


timer = QtCore.QTimer()
timer.timeout.connect(update)
timer.start(150)

if __name__ == "__main__":
    pg.exec()
