# System Design
- Input: Query
- Output: LLM chain of relevant documents
 
## Sequence of Events
- extract "topic" from query to figure out which db to use
- extract "query-able" question from query to search for relevant texts within db
    - this is because a question may be multi-layered and complex
    - some parts might be inteded for the AI 
    - by extracting/ generating a string which is easily querable to the db, we can improve
    result accuracy
- using topic and query-able text, extract `k` documents from db
- query relevant information into LLM 


## TODO: 
- [ ] sort incoming data into "bucket"/ new dbs of topics (to reduce cluter within topics)
- [ ] AI fn to chose which bucket to query
- [ ] UI
- [ ] Benchmark lightweight embedding models & test against OpenAI embedding
- [ ] Benchmark lightweight LLMs 

