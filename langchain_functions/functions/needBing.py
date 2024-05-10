def need_bing(db_confidence: int) -> bool:
    CONFIDENCE_THRESHOLD = 0.80

    return True if db_confidence > CONFIDENCE_THRESHOLD else False
