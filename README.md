# JableTVDownload

## 下載JableTV好幫手

每次看正要爽的時候就給我卡住轉圈圈  

直接下載到電腦看沒煩惱

### vitual env
```
python3 -m venv jable
source jable/bin/activate. # MacOS
```

### requirements
`pip install -r requirements.txt`

安裝 [FFmpeg] (未安裝也能下載 但影片拖拉時間軸會有卡幀情況發生)

### 執行程式(Execute)
`python main.py`

### 輸入影片網址(Input video url)
`https://jable.tv/videos/ipx-486/`    
![image](https://github.com/hcjohn463/JableDownload/blob/main/img/input.PNG)  

### 等待下載(Wait download)  
![image](https://github.com/hcjohn463/JableDownload/blob/main/img/download.PNG)

### 完成(Finish)
![image](https://github.com/hcjohn463/JableDownload/blob/main/img/3.PNG)

如果覺得好用 再麻煩給個星星好評 謝謝!!


[FFmpeg]:<https://www.gyan.dev/ffmpeg/builds/ffmpeg-git-full.7z>  

### Argument parser
`$python main.py -h`

![](https://i.imgur.com/qgyS5sf.png)

`$python main.py --random True`

可以直接下載隨機熱門影片

![](https://i.imgur.com/dSsdB7Y.png)

可以直接在cmd line指定url。

![](https://i.imgur.com/DKFrD7T.png)

### 更新日誌(Update log)

 🦈 2022/04/19 新增自動轉碼 v1.8.1

 🚗 2022/1/25 下載結束後抓封面 v1.8   
 🐶 2021/6/4 更改m3u8得到方法(正則表達式) v1.7  
 🌏 2021/5/28 更新代碼讓Unix系統(Mac,linux等)能使用 v1.6  
 🍎 2021/5/27 更新爬蟲網頁方法 v1.5  
 🌳 2021/5/20 修改編碼問題 v1.4  
 🌈 2021/5/6 增加下載進度提示、修改Crypto問題 v1.3  
 ⭐ 2021/5/5 更新穩定版本 v1.2  
