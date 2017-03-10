def WsServer(app,socketio):
    def _WsServer(host, port):
        print("ws server started at {host}:{port}".format(
            host=host, port=port))
        socketio.run(app,host=host, port=port)
    return _WsServer
