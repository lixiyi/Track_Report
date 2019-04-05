News Track
=====================
## BackGround Linking
#### 1. htw saar @ TREC 2018 News Track(https://trec.nist.gov/pubs/trec27/papers/htwsaar-N.pdf) 
	* Method 1:(nDCG@5: 0.4150) 
		* proprocessing: remove same id doc (but different id, same content doc still exits)
		* indexing: Elasticsearch (all word lowercased but not stemmed)
		* tf-idf: top 20 terms as query
		* date filter: before input doc's date 
		* re-rank: add date factor
		* filter same title, author and date doc, as well as some sections
	* Method 2:(nDCG@5: 0.1957) 
		* Standford CoreNLP: analyze the title, spot entities as query
		* other process the same as Method 1
	* Method 3:(nDCG@5: 0.4609) 
		* preprocessing: heuristic to remove suspected duplicates and some sections
		* indexing: Apache Lucene
		* two step:
			query construction: Text-Rank(key words), CoreNLP(entities) --> rank them(using 4 weighted list)
			re-rank: meta date(same author, same week likely to be related)
	* Method 4:(nDCG@5: 0.4619) 
		* indexing and removing duplicates as Method 2
		* not apply any re-ranking
		* concatenating the title and doc --> Lucene


#### 2. Paragraph as Lead - Finding Background Documents for News Articles (https://trec.nist.gov/pubs/trec27/papers/udel_fang-N.pdf)




## Entity Ranking
#### 1. Signal at TREC 2018 News Track (https://trec.nist.gov/pubs/trec27/papers/signal.N.pdf)

#### 2. TREMA-UNH at TREC 2018: Complex Answer Retrieval and News Track (https://trec.nist.gov/pubs/trec27/papers/TREMA-UNH-CAR-N.pdf)




Core Track
=====================
## Paper 2017
#### 1. ICTNET at TREC 2017 Common Core Track (https://trec.nist.gov/pubs/trec26/papers/ICTNET-CC.pdf)

## Paper 2018
To be continue...

