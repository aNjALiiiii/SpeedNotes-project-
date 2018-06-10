from tkinter import *
from tkinter import ttk
import winspeech
import sys

root = Tk()
winspeech.initialize_recognizer(winspeech.INPROC_RECOGNIZER)

root.title('SpeedNotes')
label = ttk.Label
root.resizable(10,0)
lable = ttk.Label(root,text='File name:')
lable.grid(column=0,row=0)
def SpeechRecognized(result,Listener):
	print('You said: %s'%(result))
	if result == "stop":
		print('Thank you')
		winspeech.stop_listening()
		sys.exit(0)
def f():
    listener = winspeech.listen_for_anything(SpeechRecognized)
    while listener.is_listening():
        text = input()
        if (text == 'stop'):
            listener.stop_listening()
        else:
            continue
button1 = ttk.Button(root,text='speak',command=f)
button1.grid(column=1,row=0)
root.mainloop()

