
def serialize_list(objs: list) -> list:
    """serialized each element of the list"""
    return [obj.serialize() for obj in objs]
