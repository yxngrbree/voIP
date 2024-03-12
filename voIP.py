import socket
import sounddevice as sd
import threading
import tkinter as tk
from tkinter import ttk

HOST = '127.0.0.1'
PORT = 12345

class VoIPApp:
    def __init__(self, root):
        self.root = root
        self.root.title("Fepo Voice Chat")

        # Create a UDP socket
        self.sock = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)

        # Bind the socket to a specific address and port
        self.sock.bind((HOST, PORT))

        # Create audio playback stream
        self.stream = sd.OutputStream(channels=2, callback=self.play_audio)
        self.stream.start()

        # Create GUI elements with themed styling
        self.style = ttk.Style()
        self.style.theme_use('clam')  # Choose a theme (e.g., 'clam', 'alt', 'vista', etc.)

        self.label = ttk.Label(root, text="Listening on {}:{}".format(HOST, PORT), font=('Helvetica', 14))
        self.label.pack(pady=10)

        self.start_button = ttk.Button(root, text="Start VoIP", command=self.start_voip)
        self.start_button.pack(pady=10)

        self.stop_button = ttk.Button(root, text="Stop VoIP", command=self.stop_voip, state=tk.DISABLED)
        self.stop_button.pack(pady=10)

    def play_audio(self, outdata, frames, time, status):
        data, _ = self.sock.recvfrom(1024)
        outdata[:] = sd.decode(data, channels=2, dtype='int16')

    def receive_audio(self):
        while True:
            data, _ = self.sock.recvfrom(1024)
            self.stream.write(data)

    def start_voip(self):
        # Start the thread for receiving audio
        self.receive_thread = threading.Thread(target=self.receive_audio)
        self.receive_thread.start()

        self.start_button.config(state=tk.DISABLED)
        self.stop_button.config(state=tk.NORMAL)
        self.label.config(text="VoIP in progress...", foreground='green')

    def stop_voip(self):
        # Stop the thread for receiving audio
        self.receive_thread.join()

        self.start_button.config(state=tk.NORMAL)
        self.stop_button.config(state=tk.DISABLED)
        self.label.config(text="Listening on {}:{}".format(HOST, PORT), foreground='black')

    def close_socket(self):
        # Close the socket
        self.sock.close()
        self.stream.stop()

def main():
    root = tk.Tk()
    app = VoIPApp(root)
    root.protocol("WM_DELETE_WINDOW", app.close_socket)
    root.geometry("300x200")  # Set initial window size
    root.resizable(False, False)  # Disable window resizing
    root.mainloop()

if __name__ == "__main__":
    main()
