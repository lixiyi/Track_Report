#!/usr/bin/env python3

import json
import re
from elasticsearch import Elasticsearch
from xmlhandler import get_topics

# file path
# DataPath = "D:/Download/Projects/TREC2019/WashingtonPost.v2/data/"
DataPath = "E:/Track/WashingtonPost.v2/data/"

WashingtonPost = "TREC_Washington_Post_collection.v2.jl"

topics = "newsir18-topics.txt"
bqrels = "bqrels.exp-gains.txt"

entities = "newsir18-entities.txt"
eqrels = "eqrels.txt"

es = Elasticsearch()


def process_topics():
	return
