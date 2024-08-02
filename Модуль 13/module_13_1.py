import asyncio


async def start_strongman(name: str, power: int):
    print(f'Силач {name} начал соревнования.')
    [(await asyncio.sleep(1 / power), print(f'Силач {name} поднял {ball} шар.')) for ball in range(1, 6)]
    print(f'Силач {name} закончил соревнования.')


async def start_tournament():
    [await task for task in [asyncio.create_task(start_strongman(*strongman))
                             for strongman in (('Pasha', 3), ('Denis', 4), ('Apollon', 5))]]


asyncio.run(start_tournament())
