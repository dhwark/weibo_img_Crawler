项目已改为异步下载方式，需安装依赖

pip install -r ./requirements.txt



使用前需要在userinfo.ini中事先配置

uid在对方主页的url上找到

cookie位置参考图片：![](static/cookie.png)

downloadDirRoot是你要下载保存的路径，默认会自动生成用户同名文件夹



打包命令：

```python
pyinstaller --noconfirm --onedir --console --icon "E:/PythonProject/Weibo_Img_Crawler/static/weibo_icon.ico" --add-data "E:/PythonProject/Weibo_Img_Crawler/static;static/" --add-data "E:/PythonProject/Weibo_Img_Crawler/userinfo.ini;."  "E:/PythonProject/Weibo_Img_Crawler/ttk_main.py"
```

