#!/usr/bin/env python3

import os
import json
import re
import random
from elasticsearch import Elasticsearch
import src.paper_code.htwsaar4.xmlhandler as xh

# get file path conf
path_mp = {}
with open(os.getcwd()+'/../../path.cfg', 'r', encoding='utf-8') as f:
	for line in f:
		li = line[:-1].split('=')
		path_mp[li[0]] = li[1]

es = Elasticsearch()

topics = xh.get_topics(path_mp['DataPath'] + path_mp['topics'])


def test_backgound_linking():
	with open('bresults.test', 'w', encoding='utf-8') as f1:
		for mp in topics:
			print(mp['docid'])
			# search by docid to get the query
			dsl = {
				'query': {
					'match': {
						'id': mp['docid']
					}
				}
			}
			res = es.search(index='news', body=dsl)
			print(res)
			# doc = res['hits']['hits'][0]['_source']
			# construct query by title+text
			dsl = {
				'query': {
					'match_all': {
						'query': ['title', 'text'],
						'field': ['title', 'text']
					}
				}
			}
			# res = es.search(index='news', body=dsl)
			# generate result.test file
			# out = []
			# out.append(li[0])
			# out.append('Q0')
			# out.append(li[2])
			# out.append(str(random.randint(1, 10)))
			# out.append(str(random.random()))
			# out.append('ICTNET')
			# ans = "\t".join(out) + "\n"
			# f1.write(ans)
	return


test_backgound_linking()
