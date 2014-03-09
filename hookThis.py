#Everything is awesome.
#editing this to see how github works
import time
import pyHook
import pythoncom

def uMad(event):
	return False

def uHappy(event):
	return True
time.sleep(5)
print "going to lock this shit up son!"
hm = pyHook.HookManager()
hm.MouseAll = uMad
hm.KeyAll = uMad
hm.HookMouse()
hm.HookKeyboard()
print ""
pythoncom.PumpMessages()
time.sleep(30)
print "30 more seconds"
time.sleep(30)
hm.MouseAll = uHappy
hm.KeyAll = uHappy
hm.HookMouse()
hm.HookKeyboard()
print "take a deep breath it works"
