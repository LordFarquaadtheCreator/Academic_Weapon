def remove_stop_words(input: Document) -> Document:
    import regex as re
    from langchain_core.documents import Document
    
    STOP_WORDS = ['a', 'an', 'and', 'are', 'as', 'at', 'be', 'but', 'by', 'for', 'if', 'in', 'into', 'is', 'it', 'no', 'not', 'of', 'on', 'or', 'such', 'that', 'the', 'their', 'then', 'there', 'these', 'they', 'this', 'to', 'was', 'will', 'with']
    stop_words_pattern = r'\b(?:' + '|'.join(STOP_WORDS) + r')\b'

    for doc in input.lazy_load():
        text = doc.page_content

        new_text = re.sub(stop_words_pattern, '', text)

        doc.page_content = new_text.strip()
    
    return input

