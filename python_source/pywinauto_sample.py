from pywinauto.application import Application
from subprocess import Popen
from pywinauto import Desktop
import time

app = Application(backend="uia").start('notepad.exe')
#app = Application.start('notepad.exe')

dlg_spec = app['無題 - メモ帳']

#print( dlg_spec )
#print(dlg_spec.wrapper_object())  #uiawrapper.UIAWrapper - '無題 - メモ帳', Dialog



# 完全に動作するまで待つ
actionable_dlg = dlg_spec.wait('visible')
app.Notepad.edit.TypeKeys("Hello")
#app.Properties.child_window(title="Contains:", auto_id="13087", control_type="Edit").set_text('bbbbb')


'''
# 完全に動作しないと表示しない
dlg_spec.draw_outline()
dlg_spec.window(title_re='.* - メモ帳$').window(class_name=u'編集(E)')
#dlg_spec.Properties.print_control_identifiers()
#app.Properties.print_control_identifiers()
dlg_spec.Edit.set_text('aaa')
#dlg_spec[u"編集(E)"].Properties.print_control_identifiers()
print(dlg_spec[u"編集(E)"].wrapper_object())


# 
Popen('calc.exe', shell=True)
dlg = Desktop(backend="uia")[u"電卓"]
dlg.wait('visible')
dlg.draw_outline()
#print(dlg.wrapper_object().minimize())  #uiawrapper.UIAWrapper - '電卓', Dialog
#print(dlg_spec.minimize())
dlg.window(auto_id='num8Button', control_type='Button').click()
'''
