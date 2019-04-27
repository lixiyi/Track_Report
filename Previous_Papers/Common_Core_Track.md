[TOC]

## **Common Core Track**
#### primary goals
  * bring the information retrieval community back into a traditional ad-hoc search task;

  * build one or more new test collections using more recently created documents

  * establish a (new) test collection construction methodology that avoids the pitfalls of depth-k pooling

    * **depth-k pooling** (good collections but relatively high cost):
      * putting together top N retrieval results from a set of n systems (TREC: N = 100)
      * humans manually judge every document in this pool
      * documents outside the pool automatically considered to be irrelevant
    * bandit methods (Bandit methods differ in how they choose next document) : 
    * **MaxMean** (bandit method,MM) ,**Core Track use**:
      *  each run's weight(MM) : $\frac { 1 + \text { num-relevant-retrieved } } { 2 + \text { num-judged } }$;retrieved is the num of documents appear in the top X ranks; use X = 100
      *  start : empty set of judgments , ranked list of documents 
      *  choose the first document to get a (binary) relevance judgment
      *  retrieved that document,update all runs' weight which retrieve this document
      *  re-rank all runs,choose the next document

#### Topics

* 2017 :updated version of the TREC 2004 Robust track
* 2018 :two sets of topics
  *  25 topics from the 2017 Common Core track 
  *  25 new topics to be developed by the NIST assessors

#### Connection with News Track Background Linking

* their topics are the **same** ,but in **different forms**:
  * CC : topic num + title + Description + Narrative -->sketch
  * News :topic num + doc id + doc url --->the whole article
* evaluate metrics differ:
  * CC : MAP , P@10 , recall , NDGG , whether contribute unique relevant documents to the pool
  * News : mainly NDGG@5



## **Paper 2017**



#### [UWaterlooMDS at the TREC 2017 Common Core Track](<https://trec.nist.gov/pubs/trec26/papers/UWaterlooMDS-CC.pdf>)

* objective : high recall , reasonable effort
* prototype system , three levels of relevance
  - Search Model :query and search 
  - CAL[^1] model (trained) : variation pf BMI,changes:
    - seed query  entered by users 
    - each judgment re-rank all documents 
    - store all the document feature vectors in memory 
    - document cache
  - 3 runs ,own judgments
    - TARSv1: tuple<relevance , score>,first ranked by relevance,then relevance scores
    - TARSv2: change sample weights
* user study system (improved system)
  * modefied relevance categories
  * improved CAL model  : paragraph rather than sentence summary
  * 7 runs,own and user study judgements
* 5 different treatments : **para(find most relevant documents,lowest FPR)** , search/para,para/ doc ,search/para/doc,or random order
* 10 runs:
  * prototype system
    * **TARSv1 ** : **highest MAP, NDCG and P@10 scores**,first ranked by relevance,then by the relevance scores,
    * TARSv2 : various weights for each relevance label
  * user study system
    * **BFuse** : **highest recall@1000**,3 classifiers-->3 rank lists -->reciprocal rank fusion ,



## **Paper 2018**



#### [UWaterlooMDS at the TREC 2018 Common Core Track](https://trec.nist.gov/pubs/trec27/papers/UWaterlooMDS-CC.pdf)

* Dynamic sampling (DS):creates a stratified sample of relevance judgments for test collection
  construction,after each stratum,larger,better at finding relevant documents
  * “zeroth” stratum : judged documents found from a mixture of  CAL[^1]
    and  ISJ[^2] ,inclusion probability of 1.0
  * plus unjudged documents viewed as non-relevant--->train classifier
  * rank all documents,select highest B docs--->form next stratum
  * simple random sample n docs for judge(judging paragraphs ,more efficient but equal effect ,than full documents),inclusion probability of n/B
* **relevance judgments(<http://cormack.uwaterloo.ca/sample/>)**:
  * prels : judgments plus inclusion probabilities 
  * topic id , assessed document id , stratum number , the inclusion probability of the
    assessed document 
  * DynEval:use either traditional trec eval qrels or xinfAP irels.
* runs:
  * DS_A : all judged relevant docs,ordered by the final classifier
  * DS_B : all judged relevant docs,in reverse ordered by the final classifier
  * Rank : final classifier to rank all docs
  * SEQ : if a strtum:
    * had all documents sampled:judged relevant documents by the order discovered
    * inclusion probabilities smaller than 1:0, put all documents ordered by the classiffer.



#### [FEUP at TREC 2018 Common Core Track](https://trec.nist.gov/pubs/trec27/papers/FEUP-CC.pdf)

* hypergraph-of-entity：to represent textual documents
  * two types of nodes : 
    * term nodes 
    * entity nodes
    
  * three types of hyperedges:
    * undirected document hyperedges : aggregate all terms and entities within a document
    * undirected related_to hyperedges : link sets of related entities
    * directed contained_in hyperedges : link a set of terms to their corresponding entity
    
  * random walk score(RWS)
    
    * length ℓ and a number of iterations r
    * keyword query -->term nodes -->adjacent entity nodes -->seed nodes
    * multiple random walkers from seed nodes
    * random node of random hyperedge 
    * RWS = number of visits to document hyperedges
* Base runs: 
  
    * term nodes : text-only,consisting of term nodes and document hyperedges
    * entity and term nodes : add DBpedia entities and triples , related_to hyperedges and contained_in hyperedges (first 3 paragraph)
* document profiling:

  * Named Entities (NE): Stanford NER use string-searching and dictionary-matching algorithm
  * Sentiment Analysis (SA): supervised machine learning ,text categorization techniques, and ranking skip-gram techniques ,trained by Twitter posts and movies reviews
  * Emotion Categories(EC) :a part of Sentiment Analysis but obtaining concrete emotions from the text , SVM
  * Reading Complexity (RC): Flesch–Kincaid score through textstat(0~100)
  * Keywords(KW) : RAKE tool
* runs : applying document profile on base runs : not achieve a high retrieval effectiveness

[^1]: Continuous Active Learning
[^2]: interactive searching and judging