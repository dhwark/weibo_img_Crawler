from load_info import loadImgInfo,get_district,load_userName
from download_img import downloadImg
import os
import asyncio


def loadUserInfo():
    # 从文件中读取配置项
    file = open('userinfo.ini','r',encoding='utf-8')
    for line in file.readlines():
        if line.startswith('uid='): # 对字符串进行筛选切片
            uid = line.strip()[4:]
        if line.startswith('cookie='):
            cookie = line.strip()[7:]
        if line.startswith('downloadDirRoot='):
            downloadDirRoot = line.strip()[16:]
    print('\nuid:',uid,'\ncookie:',cookie,'\ndownloadDirRoot:',downloadDirRoot)
    return (uid,cookie,downloadDirRoot)


(uid,cookie,downloadDirRoot)=loadUserInfo() # 调用函数，获取返回值元组，多元素的元组解包


async def main():
    userName = await load_userName(uid,cookie)
    downloadDir = downloadDirRoot+'/'+userName
    if not os.path.isdir(downloadDir):
        os.makedirs(downloadDir)
    pidList, since_id = await get_district(await loadImgInfo(uid,cookie,'0&has_album=true'))
    while since_id != 0:
        pidList, since_id = await get_district(await loadImgInfo(uid,cookie,since_id),pidList)
    print('数量:',len(pidList))
    return (pidList, downloadDir)


if __name__ == "__main__":
    (pidList, downloadDir) = asyncio.run(main())
    asyncio.run(downloadImg(pidList, downloadDir))