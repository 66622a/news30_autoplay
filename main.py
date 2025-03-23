import os
import requests
from bs4 import BeautifulSoup
import re
import subprocess
import psutil
import time

# Step 1: 发送 HTTP 请求
url = 'http://10.8.0.1'
response = requests.get(url)
html_content = response.text

# Step 2: 解析 HTML 并找到指定元素
soup = BeautifulSoup(html_content, 'html.parser')
a_tag = soup.select_one('div:nth-of-type(5) > div:nth-of-type(1) > div > div > div > div > div:nth-of-type(2) > div > ul > li:nth-of-type(1) > div:nth-of-type(2) > div > a')

if a_tag:
    video_page_url = a_tag.get('href', None)  # 确保 href 存在
    if video_page_url:
        print("找到的链接: ", video_page_url)

        # Step 3: 提取视频ID (例如：fee8ebbc08a342a5911a890fb6b9d601)
        match = re.search(r'videoplay_(\w+)\.html', video_page_url)
        if match:
            video_id = match.group(1)
            print("提取的视频ID: ", video_id)

            # Step 4: 下载视频
            # 使用更新的 URL 格式: http://10.8.0.1:8080/Upload/Video/{video_id}/HD_{video_id}.mp4
            video_url = 'http://10.8.0.1:8080/Upload/Video/{}/HD_{}.mp4'.format(video_id, video_id)
            video_response = requests.get(video_url)

            video_filename = f'HD_{video_id}.mp4'
            with open(video_filename, 'wb') as video_file:
                video_file.write(video_response.content)
            print(f'视频已下载到: {video_filename}')

            # Step 5: 使用 PotPlayer 播放视频
            potplayer_path = 'PotPlayer/PotPlayerMini64.exe'  # 替换为你本地的PotPlayer路径
            #playback_rate = "1.3"  # 倍速播放，1.3倍速
            potplayer_process = subprocess.Popen([potplayer_path, video_filename])

            # Step 6: 监控 PotPlayer 播放状态
            def is_process_running(process):
                """检查PotPlayer进程是否还在运行"""
                try:
                    proc = psutil.Process(process.pid)
                    return proc.is_running()
                except psutil.NoSuchProcess:
                    return False

            # 等待 PotPlayer 播放完成
            while is_process_running(potplayer_process):
                print("视频正在以 {} 倍速播放中...".format(playback_rate))
                time.sleep(5)  # 每5秒检测一次播放状态

            # Step 7: 播放完成后关闭 PotPlayer 并删除视频文件
            potplayer_process.terminate()  # 尝试关闭PotPlayer
            if os.path.exists(video_filename):
                os.remove(video_filename)
                print(f"视频文件已删除: {video_filename}")
        else:
            print("未能从链接中提取视频ID")
    else:
        print("未找到 href 属性")
else:
    print("未找到指定的链接")
