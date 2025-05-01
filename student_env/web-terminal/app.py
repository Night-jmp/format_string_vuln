from flask import Flask, render_template, send_from_directory
from flask_socketio import SocketIO
import pty
import os
import select
import threading

app = Flask(__name__, static_url_path="", static_folder="static")
socketio = SocketIO(app)

@app.route('/')
def index():
    return send_from_directory('static', 'index.html')

def read_and_forward_pty(fd):
    """Read from PTY and send to client"""
    while True:
        data, _, _ = select.select([fd], [], [], 0.1)
        if fd in data:
            output = os.read(fd, 1024).decode()
            socketio.emit('terminal_output', output)

@socketio.on('terminal_input')
def handle_input(data):
    os.write(app.pty_fd, data.encode())

@socketio.on('connect')
def connect():
    pid, fd = pty.fork()
    if pid == 0:
        os.execvp("bash", ["bash"])
    else:
        app.pty_fd = fd
        thread = threading.Thread(target=read_and_forward_pty, args=(fd,))
        thread.daemon = True
        thread.start()

if __name__ == '__main__':
    socketio.run(app, host='0.0.0.0', port=5000)

