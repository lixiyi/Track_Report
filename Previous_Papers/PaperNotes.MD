Here are some papers notes: 

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
	* `ladder-order` --> ranks the top documents for the results of dierent paragraphs based on their scores.


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
To do ...



Core Track
=====================

Since News Track's topics are the same as Core Track, ...

## Paper 2017
#### 1. ICTNET at TREC 2017 Common Core Track (https://trec.nist.gov/pubs/trec26/papers/ICTNET-CC.pdf)
To do ...


## Paper 2018
To be continue...

