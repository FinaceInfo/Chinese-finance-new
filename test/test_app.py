from . import wsapp,socketio
import json
wsapp.testing = True

class TestFinanceNewsApp(object):

    def test_get_news_keywords(self):
        client = socketio.test_client(wsapp, namespace='/finance_news')
        client.emit('news_keywords', {"query":"ok"}, namespace='/finance_news')
        received = client.get_received('/finance_news')
        assert len(received) == 1
        assert len(received[0]['args']) == 1
        assert received[0]['name'] == 'news_keywords'
        assert type(received[0]['args'][0]) == dict
        assert len(received[0]['args'][0]["result"])==10

    def test_latest_news(self):
        client = socketio.test_client(wsapp, namespace='/finance_news')
        client.emit('latest_news', {"query":"ok"}, namespace='/finance_news')
        received = client.get_received('/finance_news')
        assert len(received) == 1
        assert len(received[0]['args']) == 1
        assert received[0]['name'] == 'latest_news'
        assert type(received[0]['args'][0]) == dict
        assert len(received[0]['args'][0]["result"])==5
