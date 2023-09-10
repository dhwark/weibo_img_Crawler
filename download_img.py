import aiohttp
import asyncio


async def downloadImg(pidList, downloadDir):
    # 协程任务的入口函数
    failList = []

    tasks = [loadImg(pid, downloadDir, i) for i, pid in enumerate(pidList)]
    # 通过pid遍历列表生成tasks
    results = await asyncio.gather(*tasks)
    
    for i, has_error in enumerate(results):
        if has_error:
            failList.append(pidList[i])
    
    print('------ 完成 ------\n下载错误列表:', failList)


async def loadImg(pid, downloadDir, i):
    # 使用aiohttp下载文件
    has_error = False
    try:
        url = 'https://wx3.sinaimg.cn/large/' + pid + '.jpg'
        async with aiohttp.ClientSession(connector=aiohttp.TCPConnector(verify_ssl=False)) as session:
            async with session.get(url) as response:
                if response.status == 200:
                    content = await response.read()
                    with open(downloadDir + '/' + pid + '.jpg', 'wb') as f:
                        f.write(content)
                    print(f'{i}:', pid, 'OK!')
                else:
                    has_error = True
    except Exception:
        try:
            url = 'https://wx3.sinaimg.cn/large/' + pid + '.bmp'
            async with aiohttp.ClientSession(connector=aiohttp.TCPConnector(verify_ssl=False)) as session:
                async with session.get(url) as response:
                    if response.status == 200:
                        content = await response.read()
                        with open(downloadDir + '/' + pid + '.bmp', 'wb') as f:
                            f.write(content)
                        print(f'{i}:', pid, 'OK!')
                    else:
                        has_error = True
        except Exception:
            try:
                url = 'https://wx3.sinaimg.cn/large/' + pid + '.gif'
                async with aiohttp.ClientSession(connector=aiohttp.TCPConnector(verify_ssl=False)) as session:
                    async with session.get(url) as response:
                        if response.status == 200:
                            content = await response.read()
                            with open(downloadDir + '/' + pid + '.gif', 'wb') as f:
                                f.write(content)
                            print(f'{i}:', pid, 'OK!')
                        else:
                            has_error = True
            except Exception:
                try:
                    url = 'https://wx3.sinaimg.cn/large/' + pid + '.png'
                    async with aiohttp.ClientSession(connector=aiohttp.TCPConnector(verify_ssl=False)) as session:
                        async with session.get(url) as response:
                            if response.status == 200:
                                content = await response.read()
                                with open(downloadDir + '/' + pid + '.png', 'wb') as f:
                                    f.write(content)
                                print(f'{i}:', pid, 'OK!')
                            else:
                                has_error = True
                except Exception:
                    try:
                        url = 'https://wx3.sinaimg.cn/large/' + pid + '.jpg'
                        async with aiohttp.ClientSession(connector=aiohttp.TCPConnector(verify_ssl=False)) as session:
                            async with session.get(url) as response:
                                if response.status == 200:
                                    content = await response.read()
                                    with open(downloadDir + '/' + pid + '.jpg', 'wb') as f:
                                        f.write(content)
                                    print(f'{i}:', pid, 'OK!')
                                else:
                                    has_error = True
                    except Exception:
                        print('Download', pid, 'failed!')

    return has_error
