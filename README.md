# uia-tester

Explore Windows UIA by clicking on elements

## Develop

```console
py -3.8 -m venv env
env\scripts\activate
py -m pip install --upgrade pip
pip install -r requirements.txt
pip list --outdated
code .
```

## Package

```console
pip install pyinstaller
pyinstaller --name uia-tester --paths ".\env\Lib\site-packages\PyQt5\Qt\bin" --hidden-import comtypes.gen.UIAutomationClient --hidden-import comtypes --hidden-import comtypes.gen --hidden-import comtypes.patcher --hidden-import comtypes.GUID --hidden-import pywinauto --hidden-import pywinauto.CUIAutomation --hidden-import pywinauto.findwindows --hidden-import pywinauto.findwindow application.py --clean --onefile --windowed
```
