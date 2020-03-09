import win32api
import win32con
import os
import time
import keyboard
z=0
c=0
state_left = win32api.GetKeyState(0x01)  # Left button down = 0 or 1. Button up = -127 or -128
fa=open("code.txt","w")
fa.write("import win32api\n")
fa.write("import win32con\n")
fa.write("import time\n")
fa.write("s=float(input('Enter a speed between(0 to 36)(slow to fast)(0 or 18 for normal speed) : '))\n")
fa.write("if s==0:\n")
fa.write("  s=0.05555555555555555\n")
fa.write("else:\n")
fa.write("  s=1/s\n")
fa.write("def click(x,y):\n")
fa.write("  win32api.SetCursorPos((x,y))\n")
fa.write("  win32api.mouse_event(win32con.MOUSEEVENTF_LEFTDOWN,x,y,0,0)\n")
fa.write("  win32api.mouse_event(win32con.MOUSEEVENTF_LEFTUP,x,y,0,0)\n")
fa.write("def kb(a):\n")
fa.write("  win32api.keybd_event(a,0,0,0)\n")
fa.write("  time.sleep(0.1)\n")
fa.write("  win32api.keybd_event(a,0,win32con.KEYEVENTF_KEYUP,0)\n")
fa.write("  time.sleep(0.1)\n")
t=int(input("Enter the recording length in seconds: "))
tl=18*t
while c<tl:
  a=win32api.GetCursorPos()
  x=a[0]
  y=a[1]
  cmnd="win32api.SetCursorPos(["+str(x)+","+str(y)+"])\n"
  fa.write(cmnd)
  fa.write("time.sleep(s)\n")
  a = win32api.GetKeyState(0x01)
  if a != state_left:  # Button state changed
    state_left = a
    if a < 0:
      fa.write("click("+str(x)+","+str(y)+")\n")
  if keyboard.is_pressed('a'):
    fa.write("kb(0x41)\n")
    time.sleep(0.1)
  if keyboard.is_pressed('b'):
    fa.write("kb(0x42)\n")
    time.sleep(0.1)
  if keyboard.is_pressed('c'):
    fa.write("kb(0x43)\n")
    time.sleep(0.1)
  if keyboard.is_pressed('d'):
    fa.write("kb(0x44)\n")
    time.sleep(0.1)
  if keyboard.is_pressed('e'):
    fa.write("kb(0x45)\n")
    time.sleep(0.1)
  if keyboard.is_pressed('f'):
    fa.write("kb(0x46)\n")
    time.sleep(0.1)
  if keyboard.is_pressed('g'):
    fa.write("kb(0x47)\n")
    time.sleep(0.1)
  if keyboard.is_pressed('h'):
    fa.write("kb(0x48)\n")
    time.sleep(0.1)
  if keyboard.is_pressed('i'):
    fa.write("kb(0x49)\n")
    time.sleep(0.1)
  if keyboard.is_pressed('j'):
    fa.write("kb(0x4A)\n")
    time.sleep(0.1)
  if keyboard.is_pressed('k'):
    fa.write("kb(0x4B)\n")
    time.sleep(0.1)
  if keyboard.is_pressed('l'):
    fa.write("kb(0x4C)\n")
    time.sleep(0.1)
  if keyboard.is_pressed('m'):
    fa.write("kb(0x4D)\n")
    time.sleep(0.1)
  if keyboard.is_pressed('n'):
    fa.write("kb(0x4E)\n")
    time.sleep(0.1)
  if keyboard.is_pressed('o'):
    fa.write("kb(0x4F)\n")
    time.sleep(0.1)
  if keyboard.is_pressed('p'):
    fa.write("kb(0x50)\n")
    time.sleep(0.1)
  if keyboard.is_pressed('q'):
    fa.write("kb(0x51)\n")
    time.sleep(0.1)
  if keyboard.is_pressed('r'):
    fa.write("kb(0x52)\n")
    time.sleep(0.1)
  if keyboard.is_pressed('s'):
    fa.write("kb(0x53)\n")
    time.sleep(0.1)
  if keyboard.is_pressed('t'):
    fa.write("kb(0x54)\n")
    time.sleep(0.1)
  if keyboard.is_pressed('u'):
    fa.write("kb(0x55)\n")
    time.sleep(0.1)
  if keyboard.is_pressed('v'):
    fa.write("kb(0x56)\n")
    time.sleep(0.1)
  if keyboard.is_pressed('w'):
    fa.write("kb(0x57)\n")
    time.sleep(0.1)
  if keyboard.is_pressed('x'):
    fa.write("kb(0x58)\n")
    time.sleep(0.1)
  if keyboard.is_pressed('y'):
    fa.write("kb(0x59)\n")
    time.sleep(0.1)
  if keyboard.is_pressed('z'):
    fa.write("kb(0x5A)\n")
    time.sleep(0.1)
  if keyboard.is_pressed('1'):
    fa.write("kb(0x31)\n")
    time.sleep(0.1)
  if keyboard.is_pressed('2'):
    fa.write("kb(0x32)\n")
    time.sleep(0.1)
  if keyboard.is_pressed('3'):
    fa.write("kb(0x33)\n")
    time.sleep(0.1)
  if keyboard.is_pressed('4'):
    fa.write("kb(0x34)\n")
    time.sleep(0.1)
  if keyboard.is_pressed('5'):
    fa.write("kb(0x35)\n")
    time.sleep(0.1)
  if keyboard.is_pressed('6'):
    fa.write("kb(0x36)\n")
    time.sleep(0.1)
  if keyboard.is_pressed('7'):
    fa.write("kb(0x37)\n")
    time.sleep(0.1)
  if keyboard.is_pressed('8'):
    fa.write("kb(0x38)\n")
    time.sleep(0.1)
  if keyboard.is_pressed('9'):
    fa.write("kb(0x39)\n")
    time.sleep(0.1)
  if keyboard.is_pressed('0'):
    fa.write("kb(0x30)\n")
    time.sleep(0.1)
  if keyboard.is_pressed(' '):
    fa.write("kb(0x20)\n")
    time.sleep(0.1)
  if keyboard.is_pressed('\n'):
    fa.write("kb(0x0D)\n")
    time.sleep(0.1)
  if keyboard.is_pressed('\b'):
    fa.write("kb(0x08)\n")
    time.sleep(0.1)
  if keyboard.is_pressed('.'):
    fa.write("kb(0xBE)\n")
    time.sleep(0.1)
  if keyboard.is_pressed('/'):
    fa.write("kb(0xBF)\n")
    time.sleep(0.1)
  if keyboard.is_pressed(';'):
    fa.write("kb(0xBA)\n")
    time.sleep(0.1)
  if keyboard.is_pressed(','):
    fa.write("kb(0xBC)\n")
    time.sleep(0.1)
  if keyboard.is_pressed('esc'):
    z=1
    break
  time.sleep(0.05555555555555555)
  c+=1
if z==1:
  print("Recording stopped by the user.")
else:
  print("Completed",t,"second recording!")
fa.write("print('Completed Playing! Developed by Abhay Maurya and Akshay Maurya.')")
fa.close()
nm=input("Enter a name for your code : ")
nam=nm+".py"
os.rename("code.txt",nam)
time.sleep(1)
