from pywinauto.application import Application
app = Application(backend="uia").start("Notepad.exe")
# app.UntitledNotepad.type_keys("%FX")


from subprocess import Popen
from pywinauto import Desktop

Popen('calc.exe', shell=True)
dlg = Desktop(backend="uia").Calculator
dlg.wait('visible')

# can be multi-level
app.window(title_re='.* - Notepad$').window(class_name='Edit')

# can combine criteria
dlg = Desktop(backend="uia").Calculator
dlg.window(auto_id='num8Button', control_type='Button')





from pywinauto import Desktop, Application

app = Application(backend="uia").start('calc.exe')

dlg = Desktop(backend="uia").Calculator
dlg.type_keys('2*3=+5+9=')
dlg.print_control_identifiers()

dlg.minimize()
Desktop(backend="uia").window(title='Calculator', visible_only=False).restore()