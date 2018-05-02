# -*- coding: utf-8 -*-
from __future__ import unicode_literals
import json

dict = {"hello": "日本語"}
text = json.dumps(dict, sort_keys=True, ensure_ascii=False, indent=2)
with open("utf8.json", "w") as fh:
    fh.write(text.encode("utf-8")) # error: need str, not bytes