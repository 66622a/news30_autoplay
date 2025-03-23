# news30_autoplay
自动播放某学校内网的新闻30分
## 如何使用？
### 安装
执行：
```cmd
pip install psutil beautifulsoup4 requests
```
也可使用`Release`提供的已打包程序进行使用（见下）
### 播放
程序运行依赖`Potplayer`进行播放，也可使用其他播放器请自行尝试
请自行至 https://potplayer.daum.net/ 进行下载
下载完毕后，请将：
```
potplayer_path = 'PotPlayer/PotPlayerMini64.exe'  # 替换为你本地的PotPlayer路径
```
替换为本地的PotPlayer路径
后运行`main.py`即可播放
### 关于已打包程序
打包程序默认使用`\PotPlayer/PotPlayerMini64.exe`作为播放器路径，请将打包程序移动至相应路径
### 打包
```cmd
pip install pyinstaller
pyinstaller --onefile main.py
```
