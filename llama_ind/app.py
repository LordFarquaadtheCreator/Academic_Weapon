import torch
from transformers import AutoModelForSequenceClassification, AutoTokenizer
from llama_ind.get_db import get_db_index
from llama_ind.init_db import create_db
from llama_index.core.postprocessor import MetadataReplacementPostProcessor
from llama_ind.query_rewrite import generate_queries

# rerank model 🦅
tokenizer = AutoTokenizer.from_pretrained('BAAI/bge-reranker-large')
model = AutoModelForSequenceClassification.from_pretrained('BAAI/bge-reranker-large')
model.eval()

def extract_features(item):
    # Example for feature extraction logic
    return [item.get('quality_score', 0), item.get('user_interactions', 0), item.get('context_relevance', 0)]

def rerank_items(query, items):
    pairs = [[query, item['text']] for item in items]
    with torch.no_grad():
        inputs = tokenizer(pairs, padding=True, truncation=True, return_tensors='pt', max_length=512)
        scores = model(**inputs, return_dict=True).logits.view(-1, ).float()
    ranked_items = [item for _, item in sorted(zip(scores, items), key=lambda x: x[0], reverse=True)]
    return ranked_items

def search(query):
    db = get_db_index()
    initial_results = db.query(query)

    # Placeholder for future features as this file is just for testing rn 
    for item in initial_results:
        item['quality_score'] = ...  # Compute quality score
        item['user_interactions'] = ...  # Fetch user interactions
        item['context_relevance'] = ...  # Determine context relevance

    reranked_results = rerank_items(query, initial_results)
    return reranked_results

def main():
    try:
        res = generate_queries("What's an LDNUM? How can I write a function to generate them. Who wrote the article?")
        index = get_db_index()
        query_engine = index.as_query_engine(
            similarity_top_k=5,
            node_postprocessors=[
                MetadataReplacementPostProcessor(target_metadata_key="window")
            ],
        )

        query_engine = index.as_query_engine()
        for ques in res:
            response = query_engine.query(ques)
            print(response)

    except Exception as e:
        print(e)
        exit()

if __name__ == "__main__":
    main()
