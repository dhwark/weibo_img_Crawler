import aiohttp
import asyncio
from tqdm import tqdm


async def downloadImg(pidList, downloadDir):
    # 协程任务的入口函数
    failList = []

    # 创建总进度条
    with tqdm(total=len(pidList), desc="下载中") as pbar:
        tasks = [loadImg(pid, downloadDir, pbar) for pid in pidList]

        # 通过pid遍历列表生成tasks
        results = await asyncio.gather(*tasks)
        
        for i, has_error in enumerate(results):
            if has_error:
                failList.append(pidList[i])
    
    print('\n------ 下载完成 ------')
    if failList:
        print('\n下载错误列表:', failList)


async def loadImg(pid, downloadDir, pbar):
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
                    pbar.update(1)  # 更新子进度条
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
                        pbar.update(1)
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
                            pbar.update(1)
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
                                pbar.update(1)
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
                                    pbar.update(1)
                                else:
                                    has_error = True
                    except Exception:
                        print('Download', pid, 'failed!')

    return has_error
