def benchmark(func):
    def wrapper():
        import time
        start = time.time()
        func()
        end = time.time()
        print(f'operation takes {end - start} seconds')
    return wrapper


@benchmark
def get_page():
    import requests
    g = requests.get('https://www.google.by/')


get_page()