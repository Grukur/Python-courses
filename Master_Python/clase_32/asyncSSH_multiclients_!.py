import asyncssh
import asyncio


async def run_client(host, username, password, command):
    async with asyncssh.connect(host=host, username=username, password=password, known_hosts=None) as connection:
        return await connection.run(command)


async def run_multi_clients(hosts):
    tasks = []
    for host in hosts:
        task = run_client(host['host'], host['username'], host['password'], host['command'])
        tasks.append(task)
    results = await asyncio.gather(*tasks, return_exceptions=True)

    i = 0
    for result in results:
        i += 1
        if isinstance(result, Exception):
            print(f'Task {i} failed: {result}')
        elif result.exit_status != 0:
            print(f'Task {i} existed with status: {result.exit_status}')
            print(result.stderr, end='')
        else:
            print(f'Task {i} succeeded')
            print(result.stdout, end='')
        print('#' * 50)

hosts = [
    {'host': '192.168.0.10', 'username': 'tarrok', 'password': '1', 'command': 'ls'},
    {'host': '192.168.0.10', 'username': 'tarrok', 'password': '1', 'command': 'who -a'},
    {'host': '192.168.0.10', 'username': 'tarrok', 'password': '1', 'command': 'uname -a'}
        ]

asyncio.run(run_multi_clients(hosts))

# run_client('192.168.0.10', 'tarrok', '1', 'ls')