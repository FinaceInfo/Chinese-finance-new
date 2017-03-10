from flask_script import Manager, Server
from server import TestWsServer,WsServer
from app import app as wsapp
from app import socketio


manager = Manager(wsapp)

SERVER = {
    "testws": TestWsServer(app=wsapp,socketio=socketio),
    "ws": WsServer(app=wsapp,socketio=socketio)
}


@manager.command
def server(choise):
    """can choose from test gevent"""
    print("server start")
    SERVER.get(choise, lambda x, y: print("unknow server"))(
        host="0.0.0.0", port=5001)

if __name__ == "__main__":
    manager.run()
