"""获取各个股票的基本数据
新闻事件接口主要提供国内财经、证券、港股和期货方面的滚动新闻，
"""
__all__ = ["FinanceNews"]
from .latest_news import *
from .news_keywords import *

from flask_socketio import Namespace, emit

class FinanceNews(Namespace):

    def on_latest_news(self,date):
        ok = date.get("query")
        if ok == "ok":
            emit('latest_news', get_latest_news())

    def on_news_keywords(self,date):
        ok = date.get("query")
        if ok == "ok":
            emit('news_keywords', get_news_keywords())
