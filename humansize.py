suffixes=["KB","MB","GB","TB","PB","EB","ZB","YB"]

def approssimate_size(size=1000):
    """random comment"""
    #multiline not working
    if(size<0):
        raise ValueError("number must be non-negative")
    multiple=1024
    for suffix in suffixes:
        size/=suffixes[multiple]
        if(size<multiple):
            return f'{size}{suffix}'
    raise ValueError("to large penis")