# Voice Chat

## Description
Voice Chat is a simple VoIP (Voice over IP) application built using Python. It utilizes the `socket` module for network communication, `sounddevice` for audio handling, and `tkinter` for the graphical user interface.

## Features
- Uses UDP sockets for low-latency voice transmission.
- Streams incoming audio using the `sounddevice` library.
- Simple GUI using `tkinter`.

## Requirements
Make sure you have the following dependencies installed before running the application:

```sh
pip install sounddevice

git clone https://github.com/yourusername/repository-name.git
cd repository-name
python voip_app.py


Functions:

# Plays received audio
def play_audio(outdata, frames, time, status):
    data, _ = sock.recvfrom(1024)
    outdata[:] = sd.decode(data, channels=2, dtype='int16')

# Listens for incoming audio
def receive_audio():
    while True:
        data, _ = sock.recvfrom(1024)
        stream.write(data)


 🚀

