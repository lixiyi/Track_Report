News Track
=====================
## BackGround Linking
#### 1. htw saar @ TREC 2018 News Track(https://trec.nist.gov/pubs/trec27/papers/htwsaar-N.pdf) 
	(1) Indexing: Apache Lucene
	(2) Proprocessing: remove same id doc (but different id, same content doc still exits)
	(3) Method 1:
		a. indexing: Elasticsearch (all word lowercased but not stemmed)
		b. tf-idf: top 20 terms as query
		c. date filter: before input doc's date 
		d. re-rank: add date factor ![](http://latex.codecogs.com/gif.latex?\\e^{-\\lambda(|t_q - t|)})



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

