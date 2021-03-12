import asyncio
import functools
import time


async def sleeping(sec):
    loop = asyncio.get_event_loop()
    func = functools.partial(time.sleep, sec)
    print(f'start:  {sec}秒待つよ')
    await loop.run_in_executor(None, func)
    print(f'finish: {sec}秒待ったよ')


async def limited_parallel_call(sec_list, limit):
    sem = asyncio.Semaphore(limit)

    async def call(sec):
        with await sem:
            return await sleeping(sec)

    return await asyncio.gather(*[call(x) for x in sec_list])


def main():
    loop = asyncio.get_event_loop()
    options = [5, 1, 8, 3, 4]

    print('=== 並列実行数制限なし ===')
    loop.run_until_complete(asyncio.gather(*[sleeping(x) for x in options]))

    print('=== 2並列に制限 ===')
    loop.run_until_complete(limited_parallel_call(options, 2))
    print('=== finish ===')


if __name__ == '__main__':
    main()