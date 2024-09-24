import sounddevice as sd
from tkinter import *
from tkinter import ttk,filedialog
import numpy as np
import wavio
import threading

root=Tk()
root.title("Sound Recorder")
root.geometry("260x260")
root.resizable(False,False)

recording = False
audio_data = []
file_path = "recording.wav"

def start_record():
    global recording,audio_data
    recording=True
    record_button.config(state=DISABLED)
    audio_data.clear()
    threading.Thread(target=audio_recording).start()

def audio_recording():
    global recording
    with sd.InputStream(samplerate=44100, channels=2, callback=callback):
        while recording:
            sd.sleep(100)
    
def callback(indata, frames, time, status):
    global audio_data
    audio_data.append(indata.copy())
    
def stop_record():
    global recording,audio_data
    recording=False
    stop_button.config(state=DISABLED)
    record_button.config(state=NORMAL)
    threading.Event().wait(0.1)
    if audio_data:
        single_audio_data=np.concatenate(audio_data, axis=0)
        wavio.write("recording.wav", single_audio_data, 44100, sampwidth=2)
def path():
    global file_path
    file_path = filedialog.asksaveasfilename(defaultextension=".wav", filetypes=[("WAV files", "*.wav")])
    path_button.config(text=f"Path: {file_path}")
    
label1=ttk.Label(root,text="Sound Recorder",font=("Behnschrift Light",15))
label1.pack()

button_frame=ttk.Frame(root)
button_frame.pack(pady=20)

record_button=ttk.Button(button_frame,text="Record",command=start_record)
record_button.grid(row=0,column=0,padx=20)

stop_button=ttk.Button(button_frame,text="Stop",command=stop_record)
stop_button.grid(row=0,column=1,padx=20)

path_button=ttk.Button(root,text="Change Path", command=path)
path_button.pack()

root.mainloop()
