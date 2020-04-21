import sys, warnings

warnings.simplefilter("ignore", UserWarning)
sys.coinit_flags = 2

import os, ctypes, socket, datetime, pywinauto, pynput, json, traceback, inspect, pyperclip
from PyQt5 import QtWidgets, QtGui, QtCore
from dialog import Ui_Dialog
from ctypes.wintypes import tagPOINT

class Dialog(QtWidgets.QDialog, Ui_Dialog):

    def __init__(self, parent=None):
        super(Dialog, self).__init__(parent)
        self.initUI()
        self.listener = None
        self.data = None

    def initUI(self):
        self.setupUi(self)
        self.setWindowFlags(QtCore.Qt.WindowStaysOnTopHint)
        self.setFixedSize(640, 120)
        self.detect.setCheckable(True)
        self.detect.setEnabled(True)
        self.detect.clicked.connect(self.start_detection)
        self.copy.clicked.connect(self.copy_to_clipboard)
        self.copy.setVisible(False)

    def start_detection(self):
        if self.listener is None and self.detect.isCheckable() and self.detect.isEnabled():
            self.detect.setCheckable(False)
            self.detect.setEnabled(False)
            self.data = None
            self.listener = pynput.mouse.Listener(on_click=self.on_click)
            self.listener.start()

    def on_click(self, x, y, button, pressed):
        self.listener.stop()
        self.data = self.getDataAt(x, y)
        val = self.data['value'].replace('\n', ' ')
        if len(val) > 30: val = val[0:30] + '...'
        self.label.setText(f'Value: {val}')
        self.copy_to_clipboard()
        self.detect.setCheckable(True)
        self.detect.setEnabled(True)
        self.listener = None
    
    def copy_to_clipboard(self):
        if self.data is not None:
            text = json.dumps(self.data, default=lambda o: None, indent=4)
            pyperclip.copy(text)

    def getDataAt(self, x, y):
        result = { 'value': '' }
        try:
            point = tagPOINT(x, y)
            elem = pywinauto.uia_defines.IUIA().iuia.ElementFromPoint(point)
            element = pywinauto.uia_element_info.UIAElementInfo(elem)
            wrapper = pywinauto.controls.uiawrapper.UIAWrapper(element)
            result = self.get_dict(wrapper.element_info)
            result['value'] = ''
            result['value_method'] = None
            method = getattr(wrapper, 'get_value', None)
            if callable(method): 
                result['value'] = method()
                result['value_method'] = 'get_value'
            if not any(result['value']):
                method = getattr(wrapper, 'window_text', None)
                if callable(method): 
                    result['value'] = method()
                    result['value_method'] = 'window_text'
            if not any(result['value']):
                method = getattr(wrapper, 'texts', None)
                if callable(method): 
                    texts = method()
                    if texts is not None and isinstance(texts, list) and len(texts) > 0:
                        result['value'] = texts[0]
                        result['value_method'] = 'texts'
            if not any(result['value']):
                result['value_method'] = None
        except:
            traceback.print_exc()
        return result
    
    def get_dict(self, obj):
        result = {}
        for prop in dir(obj):
            try:
                val = getattr(obj, prop, None)
                if not prop.startswith('_') and val is not None:
                    if prop == 'parent':
                        result[prop] = self.get_dict(val)
                    elif hasattr(val, '__dict__'):
                        val_str = str(val)
                        if val_str.startswith('<'):
                            pass
                        else:
                            result[prop] = val_str    
                    else:
                        result[prop] = val
            except: pass
        return result
    
if __name__ == '__main__':
    app = QtWidgets.QApplication(sys.argv)
    win = Dialog()
    win.show()
    sys.exit(app.exec())
