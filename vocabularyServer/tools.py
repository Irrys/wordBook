

def format_response(f):
    async def wrap(*args, **kwargs):
        result = await f(*args, **kwargs)
        if isinstance(result, dict):
            if result.get("_id"):
                result["_id"] = str(result["_id"])
        if isinstance(result, list):
            for dic in result:
                if dic.get("_id"):
                    dic["_id"] = str(dic["_id"])
        response = {"data": result}
        return response
    return wrap

