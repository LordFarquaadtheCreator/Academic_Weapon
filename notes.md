# How to Build a Better RAG 101
- min/maxing chunk size
    - larger chunks -> better data BUT longer load times for LLMs & could have irrelevant info
    - smaller chunks -> less data BUT shorter load times for LLMs
    - High-level tasks like summarization requires bigger chunk size and low-level tasks like coding requires smaller chunks
- pre-processing
    - before data is fed into the database, it must be stripped of 'stop' words & special characters
        - html tags, 'the', 'a', general rubbish
    - improve quality of indexed data
    - replace pronouns with names if possible (increases sementic search results)
    - metadata
        - allows for future optimizations of time & data source in retrevial
- buckets
    - store different topics into different DBs - aka 'buckets'
- "Sentence-Window Retrival"
    - using metadata, we extract the parent chunk of the chunk that embedding search results us with
    - ![alt text](<1 8BPJwafQBe0K3SEGGgarfA.webp>)
- Query Rewritting
    - use LLM to rephrase a user's layered, multi-use question to n-queries
    - Multi-Query Retrival
        - using n-queries generated from user's one query - we gather appropiate sources for all of the data they request
        ![alt text](<1 oNLmZtyWeFdqqctJQs461A.webp>)
        ![alt text](<1 sbBnisuzLw72-YpQMWhQDw.webp>)
    - Step-Back Prompting
        - rewriting original question to first gather context on topic, nessary information not specified in original query
        ![alt text](<1 taEg4D3vxI_nuXZdsvDFwQ.webp>)
- Hybrid Search Exploration
    - include alternate methods of searching
    - keyword search, semantic search, vector search, etc.
    - use a "[sparse retriever](https://en.wikipedia.org/wiki/Okapi_BM25)" like BM25 or [TF-IDF](https://en.wikipedia.org/wiki/Tf%E2%80%93idf) with a dense retriever (embedding)
- Re-Rank & Filter Documents before sending to LLM 
    - despite having a high score in db, does not mean its a good match
    - rerank using smth like [Cohere](https://cohere.com/rerank) & filter out those that you dont need
- Document Compressors
    - small LLMs that remove noise from retrieved documents
    - returning only what is important in the context of the given query
    - can also straight up remove a document
    ![alt text](<0 T4w136ONR8lmJikh.webp>)