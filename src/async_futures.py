import os
import time
import datetime
import threading
import concurrent.futures
from concurrent.futures import ThreadPoolExecutor
# https://www.haya-programming.com/entry/2020/05/01/075309

def f(t):
    today = datetime.datetime.fromtimestamp(time.time())
    print(f"{t:2} start {threading.get_ident()} {today.strftime('%Y/%m/%d %H:%M:%S.%f')}")
    time.sleep(t)
    today = datetime.datetime.fromtimestamp(time.time())
    print(f"{t:2} end   {threading.get_ident()} {today.strftime('%Y/%m/%d %H:%M:%S.%f')}")
    return t

# system_profiler SPHardwareDataType 
print(f"os.cpu_count: {os.cpu_count()}")
# max_workers: None, os.cpu_count()
with ThreadPoolExecutor(max_workers=None) as executor:
    futures = [executor.submit(f, t) for t in [20, 10, 1, 2, 3, 4]]
    #time.sleep(5)
    result = [f.result() for f in futures]
    today = datetime.datetime.fromtimestamp(time.time())
    print(result, today.strftime('%Y/%m/%d %H:%M:%S.%f'))
    # 呼び出し順に拾う
    print("-------")
    for future in futures:
        print(future.result())
    # 終わったやつから拾う
    print("-------")
    for future in concurrent.futures.as_completed(futures):
        print(future.result())