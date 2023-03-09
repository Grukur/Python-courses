import asyncio
import time


# modo synchronus
def sync_f():
    print('one ', end='')
    time.sleep(1)
    print('two ', end='')

# modo asynchronus
async def async_f():
    print('one ', end='')
    await asyncio.sleep(1)
    print('two ', end='')
    
    
async def main():
    # task = [async_f(), async_f(), asyncio]
    tasks = [async_f() for _ in range(3)]
    
    await asyncio.gather(*tasks)

start = time.time()
asyncio.run(main())
end = time.time()
print(f'Time it take Async: {end - start}')

print('\n')
start = time.time()
for _ in range(3):
    sync_f()
end = time.time()
print(f'Time it take Sync: {end - start}')

