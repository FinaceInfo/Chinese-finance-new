__all__ = ["get_news_keywords"]

import tushare as ts
from flask import json
import jieba.analyse

def get_news_keywords():

    try:
        df = ts.get_latest_news(top=10,show_content=True)
        df["keywords"]=df["content"].apply(
            lambda i:  jieba.analyse.extract_tags(
                i, topK=5, withWeight=False, allowPOS=()) if i else [])
        del df["content"]
        rsl = [df.loc[i].to_dict() for i,trial in df.iterrows()]
        result = {"result": rsl}
    except Exception as e:
        result = {"error": "true", "message": str(e)}

    print("result")
    print(result)
    return result
