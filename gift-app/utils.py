
def serialize_list(objs: list) -> list:
    return [obj.serialize() for obj in objs]
