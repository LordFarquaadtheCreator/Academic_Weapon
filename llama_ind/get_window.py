def get_window(obj):
    """returns dictionary of window and score"""
    try:
        meta = {"data": obj[0].metadata.get("window"), "score": obj[0].score}
        return meta
    except Exception as e:
        raise Exception("Error getting window", e)
