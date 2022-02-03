def allow_cors(func):
    def wrapper():
        response = func()
        response.headers.add('Access-Control-Allow-Origin', '*')
        return response

    wrapper.__name__ = func.__name__
    return wrapper
