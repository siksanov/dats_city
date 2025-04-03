from time import time
from requests import Session

N=1000
url = 'http://httpbin.org/get' #'https://catfact.ninja/'
session = Session()
rs = []

def main():
    for _ in range(N):
        rs.append(session.get(url))
    

if __name__ == '__main__':
    start_time = time()
    try:
        main()
    except Exception as err:
        raise err
    finally:
        task_time = round(time() - start_time, 2)
        rps = round(task_time / N, 3)
        print(f'Requests: {N}; Total time: {task_time} s; RPS: {rps}. |\n')