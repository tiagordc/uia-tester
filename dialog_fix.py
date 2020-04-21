import os, subprocess, re, time

# Run this script after editing UI file on Qt Designer
pyuic = 'C:\\Program Files\\Python37\\Scripts\\pyuic5.exe'

if __name__ == '__main__':
    
    wd = os.getcwd()
    ui_file = os.path.join(wd, 'dialog.ui')
    py_file = os.path.join(wd, 'dialog.py')

    with open(ui_file, 'r') as f:
        lines = f.read()
        
    lines = re.sub("<pointsize>-1</pointsize>", "<pointsize>1</pointsize>", lines)

    with open(ui_file, "w") as f:
        f.write(lines)

    subprocess.Popen([pyuic, '-x', 'dialog.ui', '-o', 'dialog.py'], cwd=wd)
    time.sleep(2)

    with open(py_file, 'r') as f:
        lines = f.read()

    # replaces

    with open(py_file, "w") as f:
        f.write(lines)
