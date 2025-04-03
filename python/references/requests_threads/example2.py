from time import time
from requests_threads import AsyncSession

N=100
url = 'http://httpbin.org/get' #'https://catfact.ninja/'
session = AsyncSession(n=N)
rs = []

async def main():
    for _ in range(N):
        rs.append(await session.get(url))
    

if __name__ == '__main__':
    start_time = time()
    try:
        session.run(main)
    except Exception as err:
        raise err
    finally:
        task_time = round(time() - start_time, 2)
        rps = round(task_time / N, 3)
        print(f'Requests: {N}; Total time: {task_time} s; RPS: {rps}. |\n')
        print(rs)