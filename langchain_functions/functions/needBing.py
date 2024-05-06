def needBing(db_confidence: int):
    CONFIDENCE_THRESHOLD = 70

    return True if db_confidence > CONFIDENCE_THRESHOLD else False
