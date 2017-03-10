
def TestWsServer(app,socketio):
    def _TestServer(host, port):
        print("test ws server started at {host}:{port}".format(
            host=host, port=port))
        socketio.run(app,host=host, port=port,debug=True)

    return _TestServer
