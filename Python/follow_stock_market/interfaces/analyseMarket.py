"""
For more details with canvas and PySide2:
https://www.pythonguis.com/tutorials/pyside-plotting-matplotlib/
"""

from interfaces.basicInterface import BasicInterface
from interfaces.canvas import MplCanvas
from PySide2.QtWidgets import QVBoxLayout, QWidget, QPushButton, QComboBox, QRadioButton
from PySide2.QtCore import Qt
from support.api_alpha_vantage import TimeSeriesData
import numpy as np
import matplotlib.pyplot as plt
from matplotlib.backends.backend_qt5agg import NavigationToolbar2QT as NavigationToolbar


class AnalyseMarket(BasicInterface):
    def __init__(self):
        super().__init__()

        # Creating elements for the interface
        # Plot objects
        self.canvas = MplCanvas()
        self.toolbar = NavigationToolbar(self.canvas, self)

        # Interface objects
        self.add_button = QPushButton("add")
        self.confirm_button = QPushButton("confirm")
        self.symbols_list = QComboBox()

        # Widgets Initial Settings
        self.symbols_list.addItem("None")

        # Layout
        mainLayout = QVBoxLayout()
        mainLayout.setAlignment(Qt.AlignTop)
        mainLayout.addWidget(self.canvas)
        mainLayout.addWidget(self.toolbar)

        # Widget
        widget = QWidget()
        widget.setLayout(mainLayout)
        self.setCentralWidget(widget)

        self.show()


if __name__ == '__main__':
    import sys
    from PySide2.QtWidgets import QApplication

    app = QApplication(sys.argv)
    window = AnalyseMarket()
    window.show()
    app.exec_()
