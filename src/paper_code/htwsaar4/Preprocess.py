#!/usr/bin/env python3

import json
import re
from elasticsearch import Elasticsearch

# file path
DataPath = "D:/Download/Projects/TREC2019/WashingtonPost.v2/data/"

WashingtonPost = "TREC_Washington_Post_collection.v2.jl"

topics = "newsir18-topics.txt"
bqrels = "bqrels.exp-gains.txt"

entities = "newsir18-entities.txt"
eqrels = "eqrels.txt"


def process_topics(filename):
    return


def process_washington_post(filename):
    with open(filename, 'r', encoding='utf-8') as f:
        cnt = 0
        for line in f:
            if cnt == 1:
                break
            obj = json.loads(line)
            # for key in obj.keys():
            #     print(key, ':', obj[key])
            # print()
            contents = obj['contents']
            text = ""
            for li in contents:
                if li['type'] == 'sanitized_html':
                    content = li['content']
                    # remove html tags, lowercase
                    content = re.sub(r'<.*?>', '', content)
                    text += content.lower()
            obj['text'] = text
            doc = json.dumps(obj)
            cnt += 1


# put all the news into elasticsearch
def init_es():
    es = Elasticsearch()
    # to be continue
    process_washington_post(DataPath + WashingtonPost)


