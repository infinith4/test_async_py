import asyncio
from tqdm import tqdm

async def hello(name: str, wait_time: int = 2):
    """ サンプルのコルーチン """
    print('Hello ...')
    await asyncio.sleep(wait_time)
    print(f'{name}!')
    return name  # 戻り値に name を返す

async def main():
    tasks = [hello("Taro", wait_time=3),
             hello("Jiro", wait_time=2),
             hello("Saburo", wait_time=1)]

    for f in tqdm(asyncio.as_completed(tasks)):
        result = await f
        print(result)

if __name__ == "__main__":
    asyncio.run(main())