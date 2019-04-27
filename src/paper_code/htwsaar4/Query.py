#!/usr/bin/env python3

import json
import re
from elasticsearch import Elasticsearch
import src.paper_code.htwsaar4.xmlhandler as xh

# file path
DataPath = "D:/Download/Projects/TREC2019/WashingtonPost.v2/data/"
# DataPath = "E:/Track/WashingtonPost.v2/data/"

WashingtonPost = "TREC_Washington_Post_collection.v2.jl"

topics = "newsir18-topics.txt"
bqrels = "bqrels.exp-gains.txt"

entities = "newsir18-entities.txt"
eqrels = "eqrels.txt"

es = Elasticsearch()


def process_topics():
	tps = xh.get_topics(DataPath + topics)
	for mp in tps:
		print(mp['docid'])
	return

process_topics()
