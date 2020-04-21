# uia-tester

Explore Windows UIA by clicking on elements

## Develop

py -3.8 -m venv env\
env\scripts\activate\
py -m pip install --upgrade pip\
pip install -r requirements.txt\
pip list --outdated\
code .

## Package

pip install pyinstaller\
pyinstaller --name uia-tester --paths ".\env\Lib\site-packages\PyQt5\Qt\bin" --onefile --windowed application.py
