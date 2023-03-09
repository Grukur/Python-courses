import asyncio


async def run(cmd):
    proc = await asyncio.create_subprocess_shell(cmd, stdout=asyncio.subprocess.PIPE, stderr=asyncio.subprocess.PIPE)
    stdout, stderr = await proc.communicate()

    print(f'{cmd} exited with status code: {proc.returncode}')

    if stdout:
        print(f'STDOUT: {stdout.decode("UTF-8")}')

    if stderr:
        print(f'STDERR: {stderr.decode()}')


async def main(commands):
    tasks = [(run(cmd)) for cmd in commands]
    await asyncio.gather(*tasks)

commands_l = ['ipconfig', 'dir']
asyncio.run(main(commands_l))
