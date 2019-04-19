Here are some papers notes: 

Contents
=====================
- [News Track](#news-track)
	- [BackGround Linking](#BackGround-Linking)
		- [1. htw saar @ TREC 2018 News Track](#1-htw-saar--trec-2018-news-trackhttpstrecnistgovpubstrec27papershtwsaar-npdf)
		- [2. Paragraph as Lead - Finding Background Documents for News Articles](#2-paragraph-as-lead---finding-background-documents-for-news-articles-httpstrecnistgovpubstrec27papersudel_fang-npdf)
	- [Entity Ranking](#Entity-Ranking)
		- [1. Signal at TREC 2018 News Track](#1-signal-at-trec-2018-news-track-httpstrecnistgovpubstrec27paperssignalnpdf)
		- [2. TREMA-UNH at TREC 2018: Complex Answer Retrieval and News Track](#2-trema-unh-at-trec-2018-complex-answer-retrieval-and-news-track-httpstrecnistgovpubstrec27paperstrema-unh-car-npdf) 
- [Core Track](#core-track)
- [CAR Track](#car-track)


News Track
=====================
## BackGround Linking
#### 1. htw saar @ TREC 2018 News Track(https://trec.nist.gov/pubs/trec27/papers/htwsaar-N.pdf) 
* Method 1:(nDCG@5: 0.4150) 
	* proprocessing: remove same id doc (but different id, same content doc still exits)
	* indexing: `Elasticsearch` (all word lowercased but not stemmed)
	* tf-idf: top 20 terms as query
	* date filter: before input doc's date 
	* re-rank: add date factor
	* filter same title, author and date doc, as well as some sections
* Method 2:(nDCG@5: 0.1957) 
	* `Standford CoreNLP`: analyze the title, spot entities as query
	* other process the same as Method 1
* Method 3:(nDCG@5: 0.4609) 
	* preprocessing: heuristic to remove suspected duplicates and some sections
	* indexing: `Apache Lucene`
	* two step:
		* query construction: `Text-Rank`(key words), `CoreNLP`(entities) --> rank them(using 4 weighted list)
		* re-rank: meta date(same author, same week likely to be related)
* Method 4:(nDCG@5: 0.4619) 
	* indexing and removing duplicates as Method 2
	* not apply any re-ranking
	* concatenating the title and doc --> Lucene

- ![#f03c15](https://placehold.it/15/f03c15/000000?text=+) `verbose query seems better` 



#### 2. Paragraph as Lead - Finding Background Documents for News Articles (https://trec.nist.gov/pubs/trec27/papers/udel_fang-N.pdf)
* Core idea : use paragraphs as leads to and background articles.
Two steps for Paragraph-Based Background Article Discovery:
* span the main story into multiple paragraphs
	* According to the Fox, a news article has its logical breaks.
	* We use the physical breaks between paragraphs to serve as the logic breaks.
* how should the paragraphs be used?
	* We argue that the idea of relatedness between a paragraph and a background article is similar as the relevance concept in IR. 	* We need a way to find keywords, which are the words that are most representative of the meaning of the paragraphs.
	* We define keywords as the words that maximize the probability of `P(p|w)` in which `p` is a paragraph and `w` is a word in the paragraph.
	
	$$ P(p \mid w) = \frac{P(w \mid p) P(p)}{p(w)} \propto P(w \mid p) = \sum_{w_i \in p} P(w \mid w_i)$$
* result merging
	* `score-order` ---> use the maximum score a document receives among difierent paragraphs to rank the documents.
	* `vote-order` ----> use the \voting" of the paragraphs. A document that appears in more paragraphs' results is ranked higher.
	* `ladder-order` --> ranks the top documents for the results of different paragraphs based on their scores.


## Entity Ranking
#### 1. Signal at TREC 2018 News Track (https://trec.nist.gov/pubs/trec27/papers/signal.N.pdf)
* Overview :
	* `Salient Entity Linking (SEL)`:  a unified algorithm for entity linking and salience ranking
	* Assumption: entity salience ranking would reflect directly the entity ranking, assume a perfect entity linking performance
* Adaptation SEL:
	* Efficient Salient Feature: sorted featrue by estimated `Info Gain` and it's avg running time, select top features
	* Using Sentiment Analysis for Sailence: sentiment polarity around the entities may indicate how salient they are to the topic of the article
* Three runs:
	* sel: original SEL (nDCG@5 0.6071)
	* eff: apply sorted by Info Gain (nDCG@5 0.6084) `less feature seems better`
	* slst: sentiment-based (nDCG@5 0.5772) 
* ![#f03c15](https://placehold.it/15/f03c15/000000?text=+) `Dataset`: (`supervised!`) 
	* `Dexter Entity Salience` dataset (https://github.com/dexter/dexter-datasets/tree/master/entity-saliency)
	* difference between this dataset and Washington Post dataset: far shorter in length



#### 2. TREMA-UNH at TREC 2018: Complex Answer Retrieval and News Track (https://trec.nist.gov/pubs/trec27/papers/TREMA-UNH-CAR-N.pdf)
* Overview :
	* Focus on `passage retrieval`, `entity-aware passage retrieval`, and `entity retrieval` (rank both the passages and the entities) 
* Low-level Retrival Features:
	* Indexes:
		* paragraph index ---> paragraphCorpus
		* page index ---> allButBenchmark
		* entity index ---> allButBenchmark
	* Query Models:  tree-shaped outline of headings ---> form Query
	* Retrivals Models: BM25, Query likeelihood with Dirichlet smoothing
	* Expension Models: No, RM3(relevence model), ECM(bag-of-entity-linktargets), ECM-psg(expands the keywords using top 100 entities)
	* `Process`: BM25 --> bag-of-entity-linktargets --> RM calc P(E|Q) ---> ECM-psg or ECM (two variants)
	* Toolkits: `RankLib`
* Joint Entity-Passage Methods:
	* Some what like `Hits Algorithm`:
		* Passage retrieval using entity features (sum of entities) 
		* Entity retrieval using passage features (sum of passages)
* Support Passage for Entity Rankings:
	* The entity ranking is augmented with support passages
* In News Track:
	* use `a part of` the given news article(`title or first paragraph`) to construct a query
	* retrive pages depends on entities indexes
	* use BM25 with a whitelist to retrieve a re-ranking Wiki pages
	* rank the set of given entities according to their pages
* `Performance`: the best UNH-ParaBm25 (NDCG@5 :  0.74 ± 0.03) 
* ![#f03c15](https://placehold.it/15/f03c15/000000?text=+) Core ideas:
	* use the context in which an entity occurs in a passage as a means of indicating the relevance of an entity with respect to a query



Core Track
=====================

Since News Track's topics are the same as Core Track, ...

## Paper 2017
#### 1. ICTNET at TREC 2017 Common Core Track (https://trec.nist.gov/pubs/trec26/papers/ICTNET-CC.pdf)
* Overview: The primary goal of Common Core Track is to get the relative documents from the corpus with the given topics. Given that most of the topics contain less than three word and some include even one word, the author has an exploration on the topics. Then they select the apache Solr as their retrieve frame in order to improve the effectiveness on the automatic query expansion.
* Query Preprocess
	* train a model to convert words into vectors by CBOW.
	* extend the query words following an incremental procedure based on word embedding.
		* Pre-retrieval kNN based approach: select the nearest `k` neighbors of given query word set by computing the
mean cosine similarity between each candidate word and all the query words.
		* Pre-retrieval incremental kNN based approach: repeat the process for ݈`l` times ----> prune the `K` least similar neighbors in the new list to obtain list and add the first word to the expansion word set. 
	* use the TextRank algorithm to obtain the keywords from the description of the topic.
* Evaluation
	* make six submissions. In the second submission, query word is manually expanded. While in other submissions the expansion is automatic.
	* Best result ----> MAP 0.5377, NDCG 0.7699, P@10T 0.9160
	* Median result --> MAP 0.2280, NDCG 0.6787, P@10T 0.5480
## Paper 2018
To do ...



CAR Track
====================

Wikipedia dump & entity ranking.

## Paper 2017
#### 1. ICTNET at TREC2017 Complex Answer Retrieval Track (https://trec.nist.gov/pubs/trec26/papers/ICTNET-CAR.pdf)
* Overview:  Complex Answer Retrieval Track focuses on developing systems that are capable of answering complex information needs by collating relevant information from an entire corpus.
* Implementation pricinple
	* preprocess the query ----> remove the identifier `/`, don't remove stop words.
	* use `Solr` to set up an inverted index on all the documents in the test set to speed up the query.
	* use `BM25` model to calculate the score for all the documents and sorted them.
* Use `Solr` to retrieve the document
	* split the data into many copies, each with one thousand text data.
	* set up inverted index on each copies.
	*  use http to retrieve documents and we will receive an XML/JSON response which contained 1000 results for a query.
* Analysis:  separate different documents into groups by their corresponding queries and then calculate mean, minimum, maximum, average and standard deviation respectively, and we discover:
	* for each query, the mean of relevance scores is very different, ranging from 12.356 to 102.254.
	* the relevance scores of documents with the length of the queries is positively correlated.
	* for each query, the variance of the relevance scores is very small.75% are less than 3.474 and only 25% range from 3.474 to 13.784.
	* for each query, the mean of relevance scores and the median of relevance scores is very close, indicating that the distribution of relevance scores are relatively uniform.
## Paper 2018
To do ...




