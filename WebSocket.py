from flask import Flask, render_template
from flask_socketio import SocketIO, emit

app = Flask(__name__)
socketio = SocketIO(app)

# Sample data (replace with your game data)
game_data = {"score": 0, "level": 1}

@app.route('/')
def index():
    return render_template('index.html')  # Create an HTML file for your client

@socketio.on('connect')
def handle_connect():
    emit('game_data', game_data)

@socketio.on('update_game_data')
def handle_update(data):
    game_data.update(data)
    emit('game_data', game_data, broadcast=True)

if __name__ == '__main__':
    socketio.run(app, debug=True)  # Run the server with Socket.IO support
