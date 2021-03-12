import asyncio

# 1 から max までの数をコルーチンで数える。名前付き。
async def counter_coroutine(name, max):
    count = 0
    while count < max:
        count += 1
        print(f'{name}: {count}')
        await asyncio.sleep(0.01) # asyncio.sleep は coroutine。await で完了を待つ。
    return f'{name} 数え終わりました'

# カウンターを3つ同時にスケジュール。
counters = asyncio.gather(
    counter_coroutine('A', 10),
    counter_coroutine('B', 20),
    counter_coroutine('C', 30),
)
print(f'counters is {counters}') # asynio.gather の返り値は future

loop = asyncio.get_event_loop()
result = loop.run_until_complete(counters) # コルーチン関数の return で返した物は loop.run_until_complete の返り値になる。
print(result)
loop.close()