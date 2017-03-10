__all__ = ["get_latest_news"]

import tushare as ts
from flask import json


def get_latest_news():
    try:
        df = ts.get_latest_news(top=5,show_content=True)
        del df["url"]
        rsl = [df.loc[i].to_dict() for i,trial in df.iterrows()]
        result = {"result": rsl}
    except Exception as e:
        result = {"error": "true", "message": str(e)}

    print("result")
    print(result)
    return result
