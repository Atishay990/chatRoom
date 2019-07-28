from flask import Flask, render_template
from flask_socketio import SocketIO
import os

app=Flask(__name__,instance_relative_config=True)
socketio = SocketIO(app)

app.config.from_mapping(SECRET_KEY='dev',DATABASE=os.path.join(app.instance_path,'webchat.sqlite'),)




from.import auth
app.register_blueprint(auth.bp)

from.import db
db.init_app(app)

from.import message
app.register_blueprint(message.bp)



def messageReceived(methods=['GET', 'POST']):
    print('message was received!!!')

@socketio.on('my event')
def handle_my_custom_event(json, methods=['GET', 'POST']):

    print('received my event: ' + str(json))
    socketio.emit('my response', json, callback=messageReceived)

#@app.route('/')
#def session():
#    return render_template('session.html')

if __name__ == '__main__':
    socketio.run(app, debug=True)
