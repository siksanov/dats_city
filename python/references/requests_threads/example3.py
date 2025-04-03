from threading import Thread, Lock
from requests import Session
from time import time

session = Session()

conf = {'url': 'https://httpbin.org/get'}
responses = []
N=100
lock = Lock()

def requests_run(conf: dict):
    global responses
    res = session.get('https://httpbin.org/get')
    responses.append(res)

def main():
    thrds = [Thread(target=requests_run, args=[conf]) for _ in range(N)]
    start_time = time()
    for thrd in thrds:
        thrd.start()
        thrd.join()
    thrd_time = round(time() - start_time)
    thrd_rps = round(thrd_time / N, 3)
    print(f'Requests: {N}; Total time: {thrd_time} s; RPS: {thrd_rps}. |\n')

if __name__ == '__main__':
    main()
    
