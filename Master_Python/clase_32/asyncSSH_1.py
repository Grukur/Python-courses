import asyncssh
import asyncio


async def connect_and_run(host, username, password, commands1):
    async with asyncssh.connect(host=host, username=username, password=password, known_hosts=None) as connection:
        # result = await connection.run(commands1)
        # return result

        # multi commands
        results = []
        for cmd in commands1:
            result = await connection.run(cmd)
            results.append(result)
        return results

commands = ('ls', 'who -a', 'uname -a')
results = asyncio.run(connect_and_run('192.168.0.10', 'tarrok', '1', commands))
for result in results:
    print(f'STDOUT:\n{result.stdout}')
    print(f'STDERR:\n{result.stderr}')
    print('#' * 80)

