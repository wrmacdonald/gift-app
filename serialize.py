def serialize(obj):

    if hasattr(obj, '__iter__'):
        return [serialize(el) for el in obj]

    return obj.to_dict()