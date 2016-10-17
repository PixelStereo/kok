#! /usr/bin/env python
# -*- coding: utf-8 -*-

"""
Kok application launcher
Kok is an inventory application based on pykok framework
pykok is a framework for managing items in locations
"""

# import from python standard libs
import os
import sys
import signal
import getopt
import textwrap
from time import sleep
from random import randrange

# import from PyQt5 libs
from PyQt5.QtGui import QIcon, QKeySequence
from PyQt5.QtCore import Qt, QVariant, QModelIndex, QFileInfo
from PyQt5.QtWidgets import QApplication, QVBoxLayout, QCheckBox, QMainWindow, \
                            QAction, QListView, QPushButton, QToolBar, QFrame

# import from current module
sys.path.append(os.path.abspath('./../pykok'))
from pprint import pprint
from pykok.settings import __dbug__
from pykok.api import new_item


class MainWindow(QMainWindow):
    """
    This is the main window
    """
    def __init__(self):
        super(MainWindow, self).__init__()
		# create a vertical layout in a frame to add widgets
        frame = QFrame()
        self.vbox = QVBoxLayout(frame)
        self.setCentralWidget(frame)
        # create actions
        self.create_actions()
        # create a ToolBar
        self.create_toolBar()
		# set up the window
        self.setWindowTitle("KoK - Koi Ou Kan")
        self.setFixedWidth(1086)
        self.setFixedHeight(480)
        self.move(0, 0)
        # initialize pykok database
        self.db = None
        # creating pykok
        if __dbug__:
            print 'pykok framework imported'
        if __dbug__:
            print 'main window created'
        # Show the current main window
        self.show()
        # display a message to say init is over
        self.status("Ready", 0)

    def status(self, message, timeout=2000):
        """
        Display a message on the Status bar
        """
        if timeout == 0:
            timeout = 999999999
        self.statusBar().showMessage(message, timeout)

    def create_actions(self):
    	"""
    	Create actions of the main window
    	"""
        self.new_item = QAction("New", self,
                              shortcut=QKeySequence.New, statusTip="Create a new item",
                              triggered=self.new_item)
        self.view_patch = QAction("Patch", self,
                              shortcut=QKeySequence.New, statusTip="Patch in/out ports",
                              triggered=self.switch2patch)
        self.record_universe = QAction("RegisterUniverse", self,
                              shortcut=QKeySequence.New, statusTip="Register the new universe",
                              triggered=self.register_universe)

    def create_toolBar(self):
        """
        create the toolbar of the app
        it contains __dbug__ toggle, ola_connection toggle and universes_list
        """
        mytoolbar = QToolBar()
        # DMX values view
        mytoolbar.addAction(self.new_item)
        self.new_item.setVisible(True)
        # patch ports view
        mytoolbar.addAction(self.view_patch)
        self.view_patch.setVisible(True)
        self.view_patch.setEnabled(False)
        # register universe action
        mytoolbar.addAction(self.record_universe)
        self.record_universe.setVisible(True)
        """
        self.devices = QPushButton('Devices')
        self.devices.setCheckable(True)
        self.devices.toggled.connect(self.switch_view)
        self.devices.setEnabled(False)
        self.record_universe = QPushButton('Save this new universe')
        self.record_universe.hide()
        self.record_universe.released.connect(self.register_universe)
        # create a button to add a new universe
        self.new_universe = QPushButton('new universe')
        self.new_universe.released.connect(self.create_universe)
        mytoolbar.addSeparator()
        mytoolbar.addWidget(self.devices)
        mytoolbar.addWidget(self.new_universe)
        mytoolbar.addWidget(self.record_universe)"""
        mytoolbar.setMovable(False)
        mytoolbar.setFixedWidth(110)
        self.addToolBar(Qt.LeftToolBarArea, mytoolbar)
        self.toolbar = mytoolbar

    def register_universe(self):
        """
        Record a new universe (button pressed)
        """
        if __dbug__:
            print 'universe recorded'
        self.universe.id.setReadOnly(True)
        self.record_universe.setVisible(False)
        self.new_universe.setVisible(True)

    def create_settings(self):
        self.settings = PatchPanel(self)
        self.universe.grid.addWidget(self.settings,2, 0, 18, 10)
        self.ola.devicesList.connect(self.settings.devices_model.layoutChanged.emit)
        self.ola.inPortsList.connect(self.settings.inputs_model.layoutChanged.emit)
        self.ola.outPortsList.connect(self.settings.outputs_model.layoutChanged.emit)
        self.settings.setVisible(False)

    def switch2patch(self):
        """
        switch the view between universe view or devices view
        • universe view displays universe attributes (name, id and merge_mode) and DMX values
        • devices view displays devices attached to the universes (input and ouput ports)
        """
        self.universe.view.setVisible(False)
        self.settings.setVisible(True)
        self.settings.display_ports(self.universe_selected)
        self.new_item.setVisible(True)
        self.view_patch.setVisible(False)

    def closeEvent(self, event):
        """
        Call when the app is about to be closed
        """
        # why this is happenning twice?
        if self.db:
            if self.db.stop():
                event.accept()
            else:
                event.ignore()
        else:
            event.accept()

    def new_item(self):
    	"""
    	create a new item in the database
    	"""
    	pass
    	# TODO : make a view of a form 


if __name__ == "__main__":
    # create the current App
    app = QApplication(sys.argv)
    root = QFileInfo(__file__).absolutePath()
    path = root+'/icon/icon.png'
    app.setWindowIcon(QIcon(path))
    # create the Main Window and display it
    window = MainWindow()
    sys.exit(app.exec_())
